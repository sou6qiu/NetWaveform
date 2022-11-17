# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowbXKNnQ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView, QValueAxis, QSplineSeries, QChart, QLineSeries
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(764, 838)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 800))
        self.frame.setMaximumSize(QSize(150, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 200))
        self.groupBox.setMaximumSize(QSize(200, 200))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.protocol_box = QComboBox(self.groupBox)
        self.protocol_box.addItem("")
        self.protocol_box.addItem("")
        self.protocol_box.addItem("")
        self.protocol_box.setObjectName(u"protocol_box")

        self.gridLayout_3.addWidget(self.protocol_box, 1, 0, 1, 2)

        self.ip_label = QLabel(self.groupBox)
        self.ip_label.setObjectName(u"ip_label")

        self.gridLayout_3.addWidget(self.ip_label, 2, 0, 1, 2)

        self.ip_box = QComboBox(self.groupBox)
        self.ip_box.setObjectName(u"ip_box")

        self.gridLayout_3.addWidget(self.ip_box, 3, 0, 1, 2)

        self.port_label = QLabel(self.groupBox)
        self.port_label.setObjectName(u"port_label")

        self.gridLayout_3.addWidget(self.port_label, 4, 0, 1, 2)

        self.port_edit = QSpinBox(self.groupBox)
        self.port_edit.setObjectName(u"port_edit")
        self.port_edit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.port_edit.setMaximum(65535)
        self.port_edit.setValue(8888)

        self.gridLayout_3.addWidget(self.port_edit, 5, 0, 1, 2)

        self.connect_button = QPushButton(self.groupBox)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(60, 24))

        self.gridLayout_3.addWidget(self.connect_button, 6, 0, 1, 1)

        self.close_port_button = QPushButton(self.groupBox)
        self.close_port_button.setObjectName(u"close_port_button")
        self.close_port_button.setEnabled(False)
        self.close_port_button.setMinimumSize(QSize(60, 24))

        self.gridLayout_3.addWidget(self.close_port_button, 6, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(150, 450))
        self.groupBox_2.setMaximumSize(QSize(150, 16777215))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.recv_ascii_radio = QRadioButton(self.groupBox_2)
        self.recv_ascii_radio.setObjectName(u"recv_ascii_radio")
        self.recv_ascii_radio.setMinimumSize(QSize(0, 20))
        self.recv_ascii_radio.setMaximumSize(QSize(16777215, 20))
        self.recv_ascii_radio.setChecked(False)

        self.gridLayout.addWidget(self.recv_ascii_radio, 1, 0, 1, 1)

        self.recv_hex_radio = QRadioButton(self.groupBox_2)
        self.recv_hex_radio.setObjectName(u"recv_hex_radio")
        self.recv_hex_radio.setMinimumSize(QSize(0, 20))
        self.recv_hex_radio.setMaximumSize(QSize(16777215, 20))
        self.recv_hex_radio.setChecked(True)

        self.gridLayout.addWidget(self.recv_hex_radio, 1, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.recv_log_checkbox = QCheckBox(self.groupBox_2)
        self.recv_log_checkbox.setObjectName(u"recv_log_checkbox")
        self.recv_log_checkbox.setMaximumSize(QSize(16777215, 20))
        self.recv_log_checkbox.setChecked(True)

        self.gridLayout.addWidget(self.recv_log_checkbox, 3, 0, 1, 2)

        self.recv_waveform_checkbox = QCheckBox(self.groupBox_2)
        self.recv_waveform_checkbox.setObjectName(u"recv_waveform_checkbox")
        self.recv_waveform_checkbox.setMaximumSize(QSize(16777215, 20))
        self.recv_waveform_checkbox.setChecked(True)

        self.gridLayout.addWidget(self.recv_waveform_checkbox, 4, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.voltage_reference = QSpinBox(self.groupBox_2)
        self.voltage_reference.setObjectName(u"voltage_reference")
        self.voltage_reference.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.voltage_reference.setMaximum(10000)
        self.voltage_reference.setValue(1)

        self.gridLayout.addWidget(self.voltage_reference, 6, 0, 1, 2)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 2, 1, 1)

        self.recv_table = QTableWidget(self.groupBox_2)
        if (self.recv_table.columnCount() < 2):
            self.recv_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(204, 204, 204));
        self.recv_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setBackground(QColor(204, 204, 204));
        self.recv_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.recv_table.rowCount() < 8):
            self.recv_table.setRowCount(8)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.recv_table.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.recv_table.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.recv_table.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.recv_table.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.recv_table.setVerticalHeaderItem(4, __qtablewidgetitem6)
        icon = QIcon()
        iconThemeName = u"media-playback-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"C:/Users/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)
        
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setIcon(icon);
        self.recv_table.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.recv_table.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.recv_table.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setCheckState(Qt.Checked);
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setCheckState(Qt.Checked);
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setCheckState(Qt.Checked);
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(2, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(2, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setCheckState(Qt.Checked);
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setCheckState(Qt.Checked);
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(4, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(4, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setCheckState(Qt.Checked);
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(5, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(5, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setCheckState(Qt.Checked);
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(6, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(6, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setCheckState(Qt.Checked);
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(7, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.recv_table.setItem(7, 1, __qtablewidgetitem25)
        self.recv_table.setObjectName(u"recv_table")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recv_table.sizePolicy().hasHeightForWidth())
        self.recv_table.setSizePolicy(sizePolicy)
        self.recv_table.setMinimumSize(QSize(130, 260))
        self.recv_table.setMaximumSize(QSize(130, 260))
        self.recv_table.setFrameShape(QFrame.NoFrame)
        self.recv_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.recv_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.recv_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.recv_table.setAlternatingRowColors(True)
        self.recv_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.recv_table.horizontalHeader().setMinimumSectionSize(30)
        self.recv_table.horizontalHeader().setDefaultSectionSize(60)
        self.recv_table.horizontalHeader().setStretchLastSection(True)
        self.recv_table.verticalHeader().setVisible(False)
        self.recv_table.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.recv_table, 7, 0, 1, 3)

        self.recv_save_button = QPushButton(self.groupBox_2)
        self.recv_save_button.setObjectName(u"recv_save_button")
        self.recv_save_button.setMinimumSize(QSize(60, 0))
        self.recv_save_button.setMaximumSize(QSize(60, 24))

        self.gridLayout.addWidget(self.recv_save_button, 8, 0, 1, 1)

        self.recv_clear_button = QPushButton(self.groupBox_2)
        self.recv_clear_button.setObjectName(u"recv_clear_button")
        self.recv_clear_button.setMinimumSize(QSize(60, 0))
        self.recv_clear_button.setMaximumSize(QSize(60, 24))

        self.gridLayout.addWidget(self.recv_clear_button, 8, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(150, 100))
        self.groupBox_3.setMaximumSize(QSize(150, 100))
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.send_ascii_radio = QRadioButton(self.groupBox_3)
        self.send_ascii_radio.setObjectName(u"send_ascii_radio")
        self.send_ascii_radio.setChecked(True)

        self.gridLayout_2.addWidget(self.send_ascii_radio, 1, 0, 1, 1)

        self.send_hex_radio = QRadioButton(self.groupBox_3)
        self.send_hex_radio.setObjectName(u"send_hex_radio")

        self.gridLayout_2.addWidget(self.send_hex_radio, 1, 1, 1, 2)

        self.send_loop = QCheckBox(self.groupBox_3)
        self.send_loop.setObjectName(u"send_loop")
        self.send_loop.setMinimumSize(QSize(70, 0))

        self.gridLayout_2.addWidget(self.send_loop, 2, 0, 1, 2)

        self.send_loop_interval = QSpinBox(self.groupBox_3)
        self.send_loop_interval.setObjectName(u"send_loop_interval")
        self.send_loop_interval.setMaximumSize(QSize(35, 16777215))
        self.send_loop_interval.setAlignment(Qt.AlignCenter)
        self.send_loop_interval.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.send_loop_interval.setMaximum(100000)
        self.send_loop_interval.setValue(1000)

        self.gridLayout_2.addWidget(self.send_loop_interval, 2, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_2.addWidget(self.label_4, 2, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.groupBox_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(568, 525))
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.recv_data_text = QTextBrowser(self.frame_3)
        self.recv_data_text.setObjectName(u"recv_data_text")

        self.verticalLayout_3.addWidget(self.recv_data_text)

        self.recv_data_chartview = QChartView(self.frame_3)
        self.recv_data_chartview.setObjectName(u"recv_data_chartview")

        self.verticalLayout_3.addWidget(self.recv_data_chartview)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 20))
        self.label_2.setMaximumSize(QSize(50, 20))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.clients_list = QComboBox(self.groupBox_4)
        self.clients_list.setObjectName(u"clients_list")
        self.clients_list.setMinimumSize(QSize(0, 22))
        self.clients_list.setMaximumSize(QSize(16777215, 22))

        self.horizontalLayout_3.addWidget(self.clients_list)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.send_content = QTextEdit(self.groupBox_5)
        self.send_content.setObjectName(u"send_content")
        self.send_content.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.send_content)

        self.send_button = QPushButton(self.groupBox_5)
        self.send_button.setObjectName(u"send_button")
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.send_button)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u534f\u8bae\u7c7b\u578b\uff1a", None))
        self.protocol_box.setItemText(0, QCoreApplication.translate("MainWindow", u"TCP Server", None))
        self.protocol_box.setItemText(1, QCoreApplication.translate("MainWindow", u"TCP Client", None))
        self.protocol_box.setItemText(2, QCoreApplication.translate("MainWindow", u"UDP", None))

        self.ip_label.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u4e3b\u673a\u5730\u5740\uff1a", None))
        self.port_label.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u4e3b\u673a\u7aef\u53e3\uff1a", None))
        self.connect_button.setText(QCoreApplication.translate("MainWindow", u"\u76d1\u542c\u7aef\u53e3", None))
        self.close_port_button.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u7aef\u53e3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u8bbe\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u683c\u5f0f\uff1a", None))
        self.recv_ascii_radio.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.recv_hex_radio.setText(QCoreApplication.translate("MainWindow", u"HEX", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u6a21\u5f0f\uff1a", None))
        self.recv_log_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u6a21\u5f0f\u663e\u793a", None))
        self.recv_waveform_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u5f62\u56fe\u53ef\u89c6\u5316\u663e\u793a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7535\u538b\u57fa\u51c6\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"V", None))
        ___qtablewidgetitem = self.recv_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u901a\u9053", None));
        ___qtablewidgetitem1 = self.recv_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7535\u538b\u503c", None));
        ___qtablewidgetitem2 = self.recv_table.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem3 = self.recv_table.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem4 = self.recv_table.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem5 = self.recv_table.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem6 = self.recv_table.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem7 = self.recv_table.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem8 = self.recv_table.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem9 = self.recv_table.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"8", None));

        __sortingEnabled = self.recv_table.isSortingEnabled()
        self.recv_table.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.recv_table.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1ch", None));
        ___qtablewidgetitem11 = self.recv_table.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"2ch", None));
        ___qtablewidgetitem12 = self.recv_table.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"3ch", None));
        ___qtablewidgetitem13 = self.recv_table.item(3, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"4ch", None));
        ___qtablewidgetitem14 = self.recv_table.item(4, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"5ch", None));
        ___qtablewidgetitem15 = self.recv_table.item(5, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"6ch", None));
        ___qtablewidgetitem16 = self.recv_table.item(6, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"7ch", None));
        ___qtablewidgetitem17 = self.recv_table.item(7, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"8ch", None));
        self.recv_table.setSortingEnabled(__sortingEnabled)

        self.recv_save_button.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.recv_clear_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u663e\u793a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u683c\u5f0f\uff1a", None))
        self.send_ascii_radio.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.send_hex_radio.setText(QCoreApplication.translate("MainWindow", u"HEX", None))
        self.send_loop.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u53d1\u9001", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u63a5\u6536", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u6237\u7aef\uff1a", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u53d1\u9001", None))
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
    # retranslateUi

    # QChart 相关初始化
    def init_chart(self):
        self.chart = QChart()
        self.recv_data_chartview.setRenderHint(QPainter.Antialiasing)
        self.ch1 = QLineSeries()
        self.ch2 = QLineSeries()
        self.ch3 = QLineSeries()
        self.ch4 = QLineSeries()
        self.ch5 = QLineSeries()
        self.ch6 = QLineSeries()
        self.ch7 = QLineSeries()
        self.ch8 = QLineSeries()
        self.recv_data_chartview.setChart(self.chart)
        self.chart.setTitle("AD多通道波形显示")
        self.axisX = QValueAxis()
        self.axisX.setRange(0, 160)  # 设置坐标轴范围
        self.axisX.setLabelFormat("%d")  # 标签格式
        self.axisX.setTickCount(5)  # 主分隔个数
        # axisX.setMinorTickCount(4)
        self.axisX.setTitleText("点数")  # 标题
        self.axisX.setGridLineVisible(True)
        self.axisX.setMinorGridLineVisible(False)
        self.axisY = QValueAxis()
        self.axisY.setRange(-10, 10)
        self.axisY.setLabelFormat("%d")  # 标签格式
        self.axisY.setTickCount(5)
        # axisY.setMinorTickCount(4)
        self.axisY.setTitleText("V")
        # self.axisY.setGridLineVisible(True)
        self.axisY.setMinorGridLineVisible(False)
        # 将X和Y轴添加到chart上
        self.chart.addAxis(self.axisX, Qt.AlignBottom)
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        # 将8个series添加到chart上
        self.chart.addSeries(self.ch1)
        self.chart.addSeries(self.ch2)
        self.chart.addSeries(self.ch3)
        self.chart.addSeries(self.ch4)
        self.chart.addSeries(self.ch5)
        self.chart.addSeries(self.ch6)
        self.chart.addSeries(self.ch7)
        self.chart.addSeries(self.ch8)
        # 分别设置8个series的name
        self.ch1.setName('ch1')
        self.ch2.setName('ch2')
        self.ch3.setName('ch3')
        self.ch4.setName('ch4')
        self.ch5.setName('ch5')
        self.ch6.setName('ch6')
        self.ch7.setName('ch7')
        self.ch8.setName('ch8')
        # 设置series的线条颜色
        self.ch1.setColor(QColor('red'))
        self.ch2.setColor(QColor('green'))
        self.ch3.setColor(QColor('blue'))
        self.ch4.setColor(QColor('blueviolet'))
        self.ch5.setColor(QColor('black'))
        self.ch6.setColor(QColor('yellow'))
        self.ch7.setColor(QColor('purple'))
        self.ch8.setColor(QColor('brown'))
        # 设置主题颜色
        # self.chart.setTheme(QChart.ChartThemeDark)
        # 将X和Y轴附加到series上（这个设置要放在数据后面，不然会不能正常工作，不知道为什么）
        self.ch1.attachAxis(self.axisX)
        self.ch1.attachAxis(self.axisY)
        self.ch2.attachAxis(self.axisX)
        self.ch2.attachAxis(self.axisY)
        self.ch3.attachAxis(self.axisX)
        self.ch3.attachAxis(self.axisY)
        self.ch4.attachAxis(self.axisX)
        self.ch4.attachAxis(self.axisY)
        self.ch5.attachAxis(self.axisX)
        self.ch5.attachAxis(self.axisY)
        self.ch6.attachAxis(self.axisX)
        self.ch6.attachAxis(self.axisY)
        self.ch7.attachAxis(self.axisX)
        self.ch7.attachAxis(self.axisY)
        self.ch8.attachAxis(self.axisX)
        self.ch8.attachAxis(self.axisY)
