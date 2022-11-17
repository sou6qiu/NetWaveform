import binascii
import socket
import threading
import time

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

import stopThreading
from gui.ui_MainWindow import Ui_MainWindow
from tcp_ui import Tcp_Ui


class Tcp(Tcp_Ui, Ui_MainWindow):
    def __init__(self):
        print('TCP is running...')
        super().__init__()
        self.buf_size = 5000  # 一次发送的内容最大大小
        self.tcp_socket = None  # tcp socket
        self.tcp_socket_thread = None  # tcp socket 线程
        self.client_thread = None
        self.accept_thread = None
        self.client_socket_list = list()
        self.link = False  # 连接状态
        self.working = False  # 工作状态
        self.voltage = None  # 电压值

    def open_server_tcp_socket(self):
        """
        功能函数，TCP服务端开启的方法
        :return: None
        """
        """
            打开监听后直接按X关闭软件，会导致socket没有关闭，有隐患
            问题已解决：对MainWindow的函数closeEvent进行重构,或者将每个子线程设置为守护线程即可
        """
        self.close_port_button.setEnabled(True)
        self.connect_button.setEnabled(False)
        self.working = True

        ip = self.ip_box.currentText()
        port = self.port_edit.text()
        ip_port = (ip, int(port))
        # 创建 TCP Socket
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.tcp_socket.bind(ip_port)  # 绑定地址
            self.tcp_socket.listen(5)  # 监听地址，listen中的参数表示能同时处理连接的socket数量
        except Exception as ret:
            print('Error: ', ret)
            # 关闭socket
            self.close_socket()
            QMessageBox.critical(self, '错误', '端口已被占用')
        else:
            print('server is listening...')
            self.accept_thread = threading.Thread(target=self.accept_concurrency)
            # 设置线程为守护线程，防止退出主线程时，子线程仍在运行
            self.accept_thread.setDaemon(True)
            self.accept_thread.start()

    def close_socket(self):
        """
        关闭TCP网络的方法
        :return:
        """
        self.clients_list.clear()
        # 当软件工作在TCP Server模式下
        self.protocol_box.setEnabled(1)  # 使通信协议下拉框重新可选
        if self.protocol_box.currentIndex() == 0:
            try:
                for client, address in self.client_socket_list:
                    # 关闭所有的conn
                    client.close()
                    # 从conn连接列表中移除每个conn，以防下次进入监听状态时conn列表不为空，影响data_send_t按钮的判断，
                    self.client_socket_list.remove((client, address))
                self.tcp_socket.close()  # 关闭套接字
                self.working = False
                self.connect_button.setEnabled(True)
                print('server closed!')
            except Exception as ret:
                pass
        # 当软件工作在TCP Client模式下
        if self.protocol_box.currentIndex() == 1:
            try:
                self.tcp_socket.close()
                self.working = False
                self.protocol_box.setEnabled(True)
                print('TCP connection closed...')
            except Exception as ret:
                pass
        try:
            # 关闭线程
            stopThreading.stop_thread(self.tcp_socket_thread)
            self.link = False
        except Exception:
            pass
        try:
            # 关闭线程
            stopThreading.stop_thread(self.client_thread)
            self.link = False
        except Exception:
            pass

    def accept_concurrency(self):
        """
        创建监听线程，使GUI主线程继续运行，以免造成未响应
        :return:
        """
        while True:  # 无限等待连接
            try:
                client_socket, client_addr = self.tcp_socket.accept()  # 接受客户端连接
            except Exception as ret:
                time.sleep(0.001)
            else:
                self.link = True  # 连接建立标志位True，为下面的data_send_t做准备
                self.client_socket_list.append((client_socket, client_addr))  # 将连接到本服务器的客户端添加到列表中
                # 将连接到本服务器的客户端信息显示在客户端列表下拉框中
                statusbar_client_info = f'{client_addr[0]}:{client_addr[1]}'
                self.clients_list.addItem(statusbar_client_info)
                # 状态栏显示客户端连接成功信息
                self.signal_status_connected.emit(statusbar_client_info)
                # 为每个连接创建一个进程
                self.tcp_socket_thread = threading.Thread(target=self.tcp_server_concurrency,
                                                          args=(client_socket, client_addr))
                # 设置线程为守护线程，防止退出主线程时，子线程仍在运行
                self.tcp_socket_thread.setDaemon(True)
                self.tcp_socket_thread.start()

    def tcp_server_concurrency(self, client_socket, client_addr):
        """
        功能函数，为每个tcp连接创建一个线程；
        使用子线程用于创建连接，使每个tcp client可以单独地与server通信
        :return:None
        """
        # 这里的show_client_info标志位的作用：仅在收到客户端发送的第一次消息前面加上客户端的ip，port信息
        show_client_info = True
        # 将连接到本服务器的客户端信息显示在客户端列表下拉框中
        statusbar_client_info = f'{client_addr[0]}:{client_addr[1]}'
        # 将连接成功的信息打印在接收框内
        connect_info = f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}] ' \
                       f'Client {client_addr[0]}:{client_addr[1]} gets online.\n'
        self.signal_add_clientstatus_info.emit(connect_info)
        while True:
            try:
                recv_msg = client_socket.recv(self.buf_size)

            except ConnectionResetError as con_reset:
                """
                    这里要写成 ConnectionResetError ，
                    如果写成 Expection ，会导致软件进入监听状态，并且有客户端连入后，
                    点击 “断开” 按钮一次，出现 'Remote Client disconnected' 提示信息
                    单机 “断开” 按钮第二次，才会真正断开服务器的socket
                    （总结成一句话，写成Expection会导致点两次 “断开” 才能关闭服务器）
                """
                print('Error:', con_reset)
                client_socket.close()
                print(self.client_socket_list)
                # 将当前客户端的连接从socket列表中删除
                self.client_socket_list.remove((client_socket, client_addr))
                print(self.client_socket_list)
                # 判断socket列表是否已经清空，如果清空，那么self.link置为空
                if self.client_socket_list:
                    pass
                else:
                    self.link = False
                # 将已断开连接的客户端信息从客户端列表下拉box中删除
                self.comboBox_removeItem_byName(
                    self.clients_list, statusbar_client_info)
                # 状态栏显示客户端断开信息
                self.signal_status_removed.emit(statusbar_client_info)
                """
                   下面的break会导致跳出当前接收消息的循环，从而进入监听循环，等待下一个conn。
                   这样的好处是，当客户端断开连接后，服务器并不会断开socket，而是仅仅断开conn。
                   当客户端再一次连接到服务器时，服务器仍可以为其开辟新的conn，并且服务器发送消息的功能运行正确。
                   """
                break
            else:
                print(recv_msg)
                if recv_msg:
                    # 16进制显示功能检测
                    if self.recv_hex_radio.isChecked():
                        msg = binascii.b2a_hex(recv_msg).decode('utf-8')
                        # 例子：str(binascii.b2a_hex(b'\x01\x0212'))[2:-1] == >
                        # 01023132
                        print(msg, type(msg), len(msg))  # msg为 str 类型
                        # 将解码后的16进制数据按照两个字符+'空字符'发送到接收框中显示
                        msg = self.hex_show(msg)
                        # 解析16进制数据，换算成电压值
                        self.voltage = self.hex_data_to_voltage(msg,
                                                                voltage_reference=int(self.voltage_reference.text()))
                        # 每接收到新的数据都会将更新后的电压值可视化在chart上
                        self.update_chart_data()
                        # 每接收到新的数据都会将更新表格中的电压值
                        self.set_table_voltage_data()
                        if show_client_info is True:
                            # 将接收到的消息发送到接收框中进行显示，附带客户端信息
                            msg = f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}] ' \
                                  f'RECV FROM {client_addr[0]}:{client_addr[1]}\n' + msg
                            self.signal_write_msg.emit(msg)
                        else:
                            self.signal_write_msg.emit(msg)
                    else:
                        try:
                            # 尝试对接收到的数据解码，如果解码成功，即使解码后的数据是ascii可显示字符也直接发送，
                            msg = recv_msg.decode('utf-8')
                            print(msg)
                            if show_client_info is True:
                                msg = f'[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}] ' \
                                      f'RECV FROM {client_addr[0]}:{client_addr[1]}\n' + msg
                                self.signal_write_msg.emit(msg)
                            else:
                                self.signal_write_msg.emit(msg)
                        except Exception as ret:
                            # 如果出现解码错误，提示用户选中16进制显示
                            self.signal_messagebox_info.emit('解码错误，请尝试16进制显示')

                    # 将接收到的数据字节数显示在状态栏的计数区域
                    self.rx_count += len(recv_msg)
                    self.statusbar_dict['rx'].setText(
                        '接收计数：%s' % self.rx_count)

                else:
                    # 当前客户端连接主动关闭，但服务器socket并不关闭
                    client_socket.close()
                    # 将当前客户端的连接从列表中删除
                    self.client_socket_list.remove((client_socket, client_addr))
                    # 将已断开连接的客户端信息从客户端列表下拉box中删除
                    self.comboBox_removeItem_byName(
                        self.clients_list, statusbar_client_info)
                    # 状态栏显示客户端断开信息
                    self.signal_status_removed.emit(statusbar_client_info)
                    break

    def date_send_tcp(self):
        """
        功能函数，用于TCP服务端和TCP客户端发送消息
        :return: None
        """
        if self.working is False:
            QMessageBox.critical(self, '警告', '请先设置TCP网络')
        else:
            if self.link:
                get_msg = self.send_content.toPlainText()  # 从发送区获取数据
                # 判断是否是16进制发送
                send_msg = self.if_hex_send(get_msg)
                print('send msg: ', send_msg)
                # 判断发送是否为空
                if get_msg:
                    try:
                        # 发送为All connections，表示服务器向所有连入的客户端发送消息
                        if self.clients_list.currentIndex() == 0:
                            for client, address in self.client_socket_list:
                                client.sendall(send_msg)
                        else:
                            # 服务器向选中的特定客户端发送消息
                            for client, address in self.client_socket_list:
                                address_info = f'{address[0]}:{address[1]}'
                                if self.clients_list.currentText() == address_info:
                                    client.sendall(send_msg)
                        self.tx_count += len(send_msg)
                        self.statusbar_dict['tx'].setText(f'发送计数：{self.tx_count}')
                    except Exception as e_crst:
                        # QMessageBox.critical(self, '错误', '当前没有任何连接')
                        pass
                else:
                    QMessageBox.critical(self, '警告', '发送不可为空')

            else:
                QMessageBox.critical(self, '警告', '当前无任何连接')

    # chart 数据更新
    def update_chart_data(self):
        self.ch1.clear()
        self.ch2.clear()
        self.ch3.clear()
        self.ch4.clear()
        self.ch5.clear()
        self.ch6.clear()
        self.ch7.clear()
        self.ch8.clear()
        count = 0
        print('voltage: ', self.voltage)
        for i, data in enumerate(self.voltage[0]):
            self.ch1.append(i, data)
            count += 1
        for i, data in enumerate(self.voltage[1]):
            self.ch2.append(i, data)
        for i, data in enumerate(self.voltage[2]):
            self.ch3.append(i, data)
        for i, data in enumerate(self.voltage[3]):
            self.ch4.append(i, data)
        for i, data in enumerate(self.voltage[4]):
            self.ch5.append(i, data)
        for i, data in enumerate(self.voltage[5]):
            self.ch6.append(i, data)
        for i, data in enumerate(self.voltage[6]):
            self.ch7.append(i, data)
        for i, data in enumerate(self.voltage[7]):
            self.ch8.append(i, data)

        print('ch1: ', self.ch1.points())
        print('ch2: ', self.ch2.points())
        print('ch3: ', self.ch3.points())
        print('ch8: ', self.ch8.points())
        print(count)

    # 设置表格中的电压值
    def set_table_voltage_data(self):
        max_data = []
        for i in self.voltage:
            max_data.append(max(i))
        self.recv_table.item(0, 1).setText(str(round(max_data[0], 2)))
        self.recv_table.item(1, 1).setText(str(round(max_data[1], 2)))
        self.recv_table.item(2, 1).setText(str(round(max_data[2], 2)))
        self.recv_table.item(3, 1).setText(str(round(max_data[3], 2)))
        self.recv_table.item(4, 1).setText(str(round(max_data[4], 2)))
        self.recv_table.item(5, 1).setText(str(round(max_data[5], 2)))
        self.recv_table.item(6, 1).setText(str(round(max_data[6], 2)))
        self.recv_table.item(7, 1).setText(str(round(max_data[7], 2)))

    # 是否在chart中显示数据
    def if_show_in_chart(self):
        if self.recv_table.item(0, 0).checkState() == Qt.Unchecked:
            self.ch1.hide()
        else:
            self.ch1.show()
        if self.recv_table.item(1, 0).checkState() == Qt.Unchecked:
            self.ch2.hide()
        else:
            self.ch2.show()
        if self.recv_table.item(2, 0).checkState() == Qt.Unchecked:
            self.ch3.hide()
        else:
            self.ch3.show()
        if self.recv_table.item(3, 0).checkState() == Qt.Unchecked:
            self.ch4.hide()
        else:
            self.ch4.show()
        if self.recv_table.item(4, 0).checkState() == Qt.Unchecked:
            self.ch5.hide()
        else:
            self.ch5.show()
        if self.recv_table.item(5, 0).checkState() == Qt.Unchecked:
            self.ch6.hide()
        else:
            self.ch6.show()
        if self.recv_table.item(6, 0).checkState() == Qt.Unchecked:
            self.ch7.hide()
        else:
            self.ch7.show()
        if self.recv_table.item(7, 0).checkState() == Qt.Unchecked:
            self.ch8.hide()
        else:
            self.ch8.show()
