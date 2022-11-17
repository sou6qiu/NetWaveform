from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtCore import Signal
from gui.ui_MainWindow import Ui_MainWindow
from time import ctime
from PySide6.QtWidgets import QFileDialog, QMessageBox, QDialog
import binascii


class Tcp_ucpUi(Ui_MainWindow):
    # 主线程属性继承自Ui_MainWindow
    # 信号槽机制：设置一个信号，用于触发接收区写入动作
    signal_write_msg = Signal(str)
    signal_status_connected = Signal(str)
    signal_status_removed = Signal(str)
    signal_add_clientstatus_info = Signal(str)
    signal_messagebox_info = Signal(str)

    # statusbar上添加的控件
    # 使用字典方式进行管理
    statusbar_dict = {}
    rx_count = 0
    tx_count = 0
    # statusbar End
    tail_ok = False

    def __init__(self):
        super(Tcp_ucpUi, self).__init__()

    def custom_connect(self):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        self.signal_write_msg.connect(self.write_msg)
        self.signal_status_connected.connect(self.statusbar_connect)
        self.signal_status_removed.connect(self.statusbar_remove)
        self.signal_add_clientstatus_info.connect(self.add_clientstatus_plain)
        self.signal_messagebox_info.connect(self.messagebox_info)

    def add_clientstatus_plain(self, info):
        # signal_add_clientstatus_info信号会触发本函数
        """
        向接收框发送客户端连接信息
        :param info:
        :return:
        """
        self.send_content.insertPlainText(info)

    def messagebox_info(self, info):
        # signal_messagebox_info信号会触发本函数
        """
        弹出消息框
        :param info:
        :return:
        """
        QMessageBox.critical(self, '错误', info)

    def write_msg(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        # 为接收到的数据加上时间戳并且显示在接收框中
        self.send_content.insertPlainText(f'{ctime()}\n')
        self.send_content.insertPlainText(f'{msg}\n')

        # 滚动条移动到结尾
        self.send_content.moveCursor(QtGui.QTextCursor.End)

    def comboBox_removeItem_byName(self, combo, name):
        """
        QComboBox中删除特定名字的项目
        """
        for i in range(0, combo.count()):
            if name == combo.itemText(i):
                # 找到对应的项目
                combo.removeItem(i)

    def statusbar_connect(self, statusbar_client_info):
        # signal_messagebox_info信号会触发本函数
        self.statusbar.showMessage(
            f'客户端：{statusbar_client_info} 成功连接！', msecs=2000)

    def statusbar_remove(self, statusbar_client_info):
        # signal_status_removed信号会触发本函数
        self.statusbar.showMessage(
            f'客户端：{statusbar_client_info} 断开连接！', msecs=2000)

    def str_to_hex(self, s):
        """
        字符串转16进制显示
        :param s:
        :return:
        """
        return ' '.join([hex(ord(c)).replace('0x', '') for c in s])

    def hex_to_str(self, s):
        """
        16进制转字符串显示
        :param s:
        :return:
        """
        return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

    def str_to_bin(self, s):
        """
        字符串转二进制显示
        :param s:
        :return:
        """
        return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

    def bin_to_str(self, s):
        """
        二进制转字符串显示
        :param s:
        :return:
        """
        return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

    def hex_show(self, str):
        """
        将字符串转换为大写字母并每隔2个字符用空格分割处理后得到一个新字符串
        如：faa5fbb5fcc5fdd5010200000028000001900000000a002d00000000017d7840000003e800005fa55fb55fc55fd5
            FA A5 FB B5 FC C5 FD D5 01 02 00 00 00 28 00 00 01 90 00 00 00 0A 00 2D 00 00 00 00 01 7D 78 40 00 00 03 E8 00 00 5F A5 5F B5 5F C5 5F D5
        :param str:
        :return:
        """
        t = str.upper()
        return ' '.join([t[2 * i:2 * (i + 1)] for i in range(len(t) // 2)])
        # / 是精确除法， // 是向下取整除法， % 是求模

    def if_hex_send(self, pre_msg):
        """
        判断是否以16进制发送并处理
        :param pre_msg:
        :return:
        """
        try:
            if self.send_hex_radio.isChecked():
                send_msg = pre_msg.replace(' ', '')  # 删除无效的空格
                if len(send_msg) % 2 != 0:
                    # 十六进制发送输入的长度必须是2的倍数
                    raise Exception('十六进制输入的长度必须是2的倍数')
                send_msg = binascii.a2b_hex(send_msg)
            else:
                send_msg = pre_msg.encode('utf-8')
            return send_msg

        except binascii.Error as e:
            QMessageBox.critical(self, '错误', '十六进制数中包含非法字符！')
        except Exception as e:
            QMessageBox.critical(self, '错误', '%s' % e)

    def if_hex_show_tcpc_udp(self, pre_msg):
        """
        判断是否以16进制显示并处理
        :param pre_msg:
        :return:
        """
        if self.recv_hex_radio.isChecked():
            msg = binascii.b2a_hex(pre_msg).decode('utf-8')
            print(msg, type(msg), len(msg))  # msg为 str 类型
            msg = self.hex_show(msg)  # 将解码后的16进制数据按照两个字符+'空字符'发送到接收框中显示
            self.signal_write_msg.emit(msg)
        else:
            try:
                # 尝试对接收到的数据解码，如果解码成功，即使解码后的数据是ascii可显示字符也直接发送，
                msg = pre_msg.decode('utf-8')
                print(msg)
                self.signal_write_msg.emit(msg)
            except Exception as ret:
                # 如果出现解码错误，提示用户选中16进制显示
                self.signal_messagebox_info.emit('解码错误，请尝试16进制显示')