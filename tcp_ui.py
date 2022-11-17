import binascii
import time

from PySide6 import QtGui
from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QMessageBox

from gui.ui_MainWindow import Ui_MainWindow


class Tcp_Ui(Ui_MainWindow):
    """
    TCP连接逻辑的处理模块，界面和功能解耦合
    """
    # 信号槽机制：设置一个信号，用于触发接收区写入动作
    signal_write_msg = Signal(str)
    signal_status_connected = Signal(str)
    signal_status_removed = Signal(str)
    signal_add_clientstatus_info = Signal(str)
    signal_messagebox_info = Signal(str)

    def __init__(self):
        print('TCP_UI is running...')
        super().__init__()
        # 主线程属性继承自Ui_MainWindow

        # statusbar上添加的控件
        # 使用字典方式进行管理
        self.statusbar_dict = {}
        self.rx_count = 0
        self.tx_count = 0
        # statusbar End
        self.tail_ok = False
    #
    # # QChart 相关初始化
    # def init_chart(self):
    #     self.chart = QChart()
    #     self.ch1 = QSplineSeries()
    #     self.ch2 = QSplineSeries()
    #     self.ch3 = QSplineSeries()
    #     self.ch4 = QSplineSeries()
    #     self.ch5 = QSplineSeries()
    #     self.ch6 = QSplineSeries()
    #     self.ch7 = QSplineSeries()
    #     self.ch8 = QSplineSeries()
    #     self.recv_data_chartview.setChart(self.chart)
    #     self.chart.setTitle("AD多通道波形显示")
    #     self.axisX = QValueAxis()
    #     self.axisX.setRange(0, 80)  # 设置坐标轴范围
    #     self.axisX.setLabelFormat("%d")  # 标签格式
    #     self.axisX.setTickCount(5)  # 主分隔个数
    #     # axisX.setMinorTickCount(4)
    #     self.axisX.setTitleText("点数")  # 标题
    #     self.axisX.setGridLineVisible(True)
    #     self.axisX.setMinorGridLineVisible(False)
    #     self.axisY = QValueAxis()
    #     self.axisY.setRange(-10, 10)
    #     self.axisY.setLabelFormat("%d")  # 标签格式
    #     self.axisY.setTickCount(5)
    #     # axisY.setMinorTickCount(4)
    #     self.axisY.setTitleText("V")
    #     # self.axisY.setGridLineVisible(True)
    #     self.axisY.setMinorGridLineVisible(False)
    #     # 将X和Y轴添加到chart上
    #     self.chart.addAxis(self.axisX, Qt.AlignBottom)
    #     self.chart.addAxis(self.axisY, Qt.AlignLeft)
    #     # 将8个series添加到chart上
    #     self.chart.addSeries(self.ch1)
    #     self.chart.addSeries(self.ch2)
    #     self.chart.addSeries(self.ch3)
    #     self.chart.addSeries(self.ch4)
    #     self.chart.addSeries(self.ch5)
    #     self.chart.addSeries(self.ch6)
    #     self.chart.addSeries(self.ch7)
    #     self.chart.addSeries(self.ch8)
    #     # 分别设置8个series的name
    #     self.ch1.setName('ch1')
    #     self.ch2.setName('ch2')
    #     self.ch3.setName('ch3')
    #     self.ch4.setName('ch4')
    #     self.ch5.setName('ch5')
    #     self.ch6.setName('ch6')
    #     self.ch7.setName('ch7')
    #     self.ch8.setName('ch8')
    #     # 设置series的线条颜色
    #     self.ch1.setColor(QColor('red'))
    #     self.ch2.setColor(QColor('green'))
    #     self.ch3.setColor(QColor('blue'))
    #     self.ch4.setColor(QColor('blueviolet'))
    #     self.ch5.setColor(QColor('black'))
    #     self.ch6.setColor(QColor('yellow'))
    #     self.ch7.setColor(QColor('purple'))
    #     self.ch8.setColor(QColor('brown'))
    #     # 设置主题颜色
    #     # self.chart.setTheme(QChart.ChartThemeDark)
    #     # 将X和Y轴附加到series上（这个设置要放在数据后面，不然会不能正常工作，不知道为什么）
    #     self.ch1.attachAxis(self.axisX)
    #     self.ch1.attachAxis(self.axisY)
    #     self.ch2.attachAxis(self.axisX)
    #     self.ch2.attachAxis(self.axisY)
    #     self.ch3.attachAxis(self.axisX)
    #     self.ch3.attachAxis(self.axisY)
    #     self.ch4.attachAxis(self.axisX)
    #     self.ch4.attachAxis(self.axisY)
    #     self.ch5.attachAxis(self.axisX)
    #     self.ch5.attachAxis(self.axisY)
    #     self.ch6.attachAxis(self.axisX)
    #     self.ch6.attachAxis(self.axisY)
    #     self.ch7.attachAxis(self.axisX)
    #     self.ch7.attachAxis(self.axisY)
    #     self.ch8.attachAxis(self.axisX)
    #     self.ch8.attachAxis(self.axisY)

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

    def write_msg(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PySide程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        # 为接收到的数据加上时间戳并且显示在接收框中
        # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # self.recv_data_text.insertPlainText(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}\n')
        self.recv_data_text.insertPlainText(f'{msg}\n')

        # 滚动条移动到结尾
        self.recv_data_text.moveCursor(QtGui.QTextCursor.End)

    def statusbar_connect(self, statusbar_client_info):
        # signal_messagebox_info信号会触发本函数
        self.statusbar.showMessage(f'客户端：{statusbar_client_info} 成功连接！', 2000)

    def statusbar_remove(self, statusbar_client_info):
        # signal_status_removed信号会触发本函数
        self.statusbar.showMessage(f'客户端：{statusbar_client_info} 断开连接！', 2000)

    def add_clientstatus_plain(self, info):
        # signal_add_clientstatus_info信号会触发本函数
        """
        向接收框发送客户端连接信息
        :param info:
        :return:
        """
        self.recv_data_text.insertPlainText(info)

    def messagebox_info(self, info):
        # signal_messagebox_info信号会触发本函数
        """
        弹出消息框
        :param info:
        :return:
        """
        QMessageBox.critical(self, '错误', info)

    def comboBox_removeItem_byName(self, combo, name):
        """
        QComboBox中删除特定名字的项目
        """
        for i in range(0, combo.count()):
            if name == combo.itemText(i):
                # 找到对应的项目
                combo.removeItem(i)

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

    # 接收数据到通道电压值的换算
    def hex_data_to_voltage(self, hex_data, voltage_reference):
        """
        根据要求进行计算：
        前4个字节为帧头  其余数据为真实数据，数据量应该为8的倍数，即8个通道的数，每个通道160个数据（320个字节）
        即8X320=2560 + 4 （上面帧头）= 2564 个数，为一包
        计算公式：
        16位转换数据范围为0-65535，对应电压计算：
        设：data为16位转换结果
        当data>=32768 时
        通道电压值 = （（data X 10.0）/ 32768 - 20.0）X 2.5）/基准电压值
        当data<32768 时
        通道电压值 = （（data X 10.0）/ 32768) X 2.5）/基准电压值（单位V）
        基准电压值：每个板子都有一个测量过的基准电压值
        :return:
        """
        # 丢弃前4个字节
        hex_data = hex_data.replace(' ', '')[8:]
        # 每隔4个字节分割
        hex_data = [hex_data[i:i + 4] for i in range(0, len(hex_data), 4)]
        voltage = []
        for i in range(8):
            # 当data>=32768 时
            #         通道电压值 = （（data X 10.0）/ 32768 - 20.0）X 2.5）/基准电压值
            # 当data<32768 时
            #         通道电压值 = （（data X 10.0）/ 32768) X 2.5）/基准电压值（单位V）
            voltage.append([(int(j, 16) * 10.0 / 32768 - 20.0) * 2.5 / voltage_reference if int(j, 16) >= 32768
                            else (int(j, 16) * 10.0 / 32768) * 2.5 / voltage_reference for j in hex_data[i::8]])
        return voltage
