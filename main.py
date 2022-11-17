import os
import socket
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QSizePolicy, QLabel, QPushButton

from gui.ui_MainWindow import Ui_MainWindow
from tcp import Tcp
from tcp_ui import Tcp_Ui


class MainWindow(QMainWindow, Tcp, Tcp_Ui, Ui_MainWindow):
    def __init__(self):

        print('MainWindow is running...')
        super().__init__()
        Tcp.__init__(self)

        self.interval = None
        self.timer = None
        # UI setup
        self.setupUi(self)

        # 功能 setup
        self.init()
        self.setWindowTitle('网络波形图')

        self.show()

    def init(self):
        # 暂未实现TCP Client 和 UDP 通信功能
        self.protocol_box.setItemText(1, self.protocol_box.itemText(1) + '暂不可用')
        self.protocol_box.setItemText(2, self.protocol_box.itemText(2) + '暂不可用')
        self.protocol_box.model().item(1).setEnabled(False)
        self.protocol_box.model().item(2).setEnabled(False)
        # 设置通信协议
        self.protocol_box.currentIndexChanged.connect(self.protocol_change)
        # 设置主机地址，获取本地IP
        ip = self.get_host_ip()
        self.ip_box.addItem(ip)
        self.ip_box.addItem('127.0.0.1')
        self.ip_box.addItem('0.0.0.0')
        # 设置监听端口按钮功能
        self.connect_button.clicked.connect(self.connect_btn_setup)
        # 设置断开连接按钮功能
        self.close_port_button.clicked.connect(self.close_btn_setup)
        # 设置接收设置里的显示模式
        self.show_mode_change()
        self.recv_log_checkbox.stateChanged.connect(self.show_mode_change)
        self.recv_waveform_checkbox.stateChanged.connect(self.show_mode_change)
        # 关闭socket
        self.close_port_button.clicked.connect(self.close_btn_setup)
        # 清空接收区显示
        self.recv_clear_button.clicked.connect(self.recv_dataclear)
        # 设置发送按钮
        self.send_button.clicked.connect(self.data_send_select)
        # 定时器启动检测
        self.send_loop.toggled.connect(self.checktimer)
        # 按下保存数据按钮，进行保存操作
        self.recv_save_button.clicked.connect(self.datasave2file)
        # 设置信号与槽
        self.custom_connect()
        # 设置状态栏
        self.init_statusbar()

        self.recv_table.clicked.connect(self.set_table_voltage_data)
        self.recv_table.itemClicked.connect(self.if_show_in_chart)
        self.init_chart()

    def get_host_ip(self):
        """
        查询本机ip地址
        :return: ip
        """
        # 获取本机ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = '127.0.0.1'
        try:
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except Exception as ret:
            # 若无法连接互联网使用，会调用以下方法
            try:
                ip = socket.gethostbyname(socket.gethostname())
            except Exception as ret_e:
                QMessageBox.critical(self, '错误', "无法获取ip，请连接网络！\n")
                self.signal_write_msg.emit("无法获取ip，请连接网络！\n")
        finally:
            s.close()
        return ip

    def protocol_change(self):
        index = self.protocol_box.currentIndex()
        print(index)
        if index == 0:  # TCP Server
            self.ip_label.setText('本地主机地址：')
            self.port_label.setText('本地主机端口号：')
            self.connect_button.setText('监听端口')
        elif index == 1:  # TCP Client
            self.ip_label.setText('远程主机地址：')
            self.port_label.setText('远程主机端口号：')
            self.connect_button.setText('发起连接')
        elif index == 2:  # UDP
            self.ip_label.setText('本地主机地址：')
            self.port_label.setText('本地主机端口号：')
            self.connect_button.setText('监听端口')

    def connect_btn_setup(self):
        """
        启动按钮功能选择
        :return:
        """
        self.protocol_box.setEnabled(0)
        if self.protocol_box.currentIndex() == 0:
            # 创建TCP Server
            self.open_server_tcp_socket()
            self.clients_list.addItem('All Connections')
        # if self.protocol_box.currentIndex() == 1:
        #     # 创建TCP Client
        #     self.socket_open_tcpc()
        # if self.protocol_box.currentIndex() == 2:
        #     # 创建UDP Client socket
        #     self.socket_open_udp()
        if self.working is True:
            self.statusbar_dict['status'].setText('状态：打开')

    def close_btn_setup(self):
        """
        断开按钮功能选择
        :return:
        """
        # TODO: 断开所有连接
        self.close_socket()

    def close_connection_btn_setup(self):
        if self.protocol_box.currentIndex() == 0:
            # 关闭TCPServer
            self.close_socket()
        # if self.protocol_box.currentIndex() == 1:
        #     # 断开TCPClient
        #     self.socket_close()
        # if self.protocol_box.currentIndex() == 2:
        #     # 关闭UDP socket
        #     self.socket_close_u()

    def init_statusbar(self):
        """
        程序下方状态栏设置
        :return:
        """
        # 设置statusbar所有控件自动延伸
        self.statusbar.setSizePolicy(QSizePolicy.Expanding,
                                     QSizePolicy.Expanding)
        # 设置status隐藏控制点（靠齐最右边）
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar_dict['status'] = QLabel()
        self.statusbar_dict['status'].setText('状态：Ready')
        self.statusbar_dict['tx'] = QLabel()
        self.statusbar_dict['tx'].setText('发送计数：0')
        self.statusbar_dict['rx'] = QLabel()
        self.statusbar_dict['rx'].setText('接收计数：0')
        self.statusbar_dict['clear'] = QPushButton()
        self.statusbar_dict['clear'].setText('清除')
        self.statusbar_dict['clear'].setToolTip('清除发送和接收计数')
        self.statusbar_dict['clear'].pressed.connect(self.statusbar_clear_pressed)

        for i, w in enumerate(self.statusbar_dict.values()):
            if i != len(self.statusbar_dict) - 1:
                self.statusbar.addWidget(w, 20)
            else:
                # 最后一个控件不拉伸
                self.statusbar.addWidget(w)

    def statusbar_clear_pressed(self):
        self.statusbar_dict['tx'].setText('发送计数：0')
        self.statusbar_dict['rx'].setText('接收计数：0')
        self.rx_count = 0
        self.tx_count = 0

    def checktimer(self):
        """
        检测Timer是否需要开启
        :return:
        """
        if self.send_loop.isChecked():
            self.timer = QTimer(self)
            try:
                self.interval = int(self.send_loop_interval.text())
                self.timer.timeout.connect(self.data_send_select)
                self.timer.start(self.interval)
            except Exception as ret:
                self.messagebox_info('请输入合法的时间间隔/ms')
                self.send_loop.setChecked(0)
        else:
            self.timer.stop()

    def data_send_select(self):
        """ 发送按钮功能选择
        :return:
        """
        if self.protocol_box.currentIndex() == 0:
            self.date_send_tcp()
        # if self.protocol_box.currentIndex() == 1:
        #     self.data_send_t_c()
        # if self.protocol_box.currentIndex() == 2:
        #     self.data_send_u()

    def recv_dataclear(self):
        """
        pushbutton_clear控件点击触发的槽
        :return: None
        """
        # 清空接收区屏幕
        self.recv_data_text.clear()

    def rfilechoose(self):
        '''
        选择要保存的文件名
        :return:
        '''
        '''接收转向文件'''
        file_name, ok = QFileDialog.getSaveFileName(
            self, u'保存文件', './', u'所有文件(*.*)')
        print(file_name)
        if ok:
            self.save_file_name = file_name
        else:
            self.save_file_name = None

    def datasave2file(self):
        '''
        将接收框中的消息保存到文件
        :return:
        '''
        if not self.recv_data_text.toPlainText():
            QMessageBox.critical(self, '警告', '当前没有需要的数据')
        else:
            file_name, state = QFileDialog.getSaveFileName(self, '保存文件', './',
                                                           'Text文件(*.txt)')
            if state:
                with open(file_name, 'a', encoding='utf-8') as f_obj:
                    f_obj.write(self.recv_data_text.toPlainText())
                QMessageBox.information(self, '成功', '%s文件保存成功! ' % file_name)

    # 接收设置：选择显示模式
    def show_mode_change(self):
        if self.recv_log_checkbox.isChecked():
            self.recv_data_text.show()
        else:
            self.recv_data_text.hide()
        if self.recv_waveform_checkbox.isChecked():
            self.recv_data_chartview.show()
        else:
            self.recv_data_chartview.hide()

    def closeEvent(self, event):
        """
        对MainWindow的函数closeEvent进行重构
        退出软件时结束所有进程
        :param event:
        :return:
        """
        reply = QMessageBox.question(self,
                                     '网络波形图',
                                     "是否要退出程序？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            os._exit(0)
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
