import math
from PyQt5 import QtCore, QtGui, QtWidgets
import globals
from PyQt5.QtWidgets import QPushButton, QTableWidgetItem, QMessageBox
from shared_data import SharedData
import pandas as pd
import numpy as np

class zhenduanjiemian1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1554, 865)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:rgb(234, 242, 255)\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color:rgb(238, 238, 238);\n"
"}\n"
"QTableWidget::item {\n"
"    color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 90, 1561, 761))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:rgb(203, 203, 203)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_kaishizhenduan = QtWidgets.QPushButton(self.frame)
        self.pushButton_kaishizhenduan.setGeometry(QtCore.QRect(480, 640, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_kaishizhenduan.setFont(font)
        self.pushButton_kaishizhenduan.setObjectName("pushButton_kaishizhenduan")
        self.tableWidget_duquwenjian = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_duquwenjian.setGeometry(QtCore.QRect(100, 30, 581, 531))
        self.tableWidget_duquwenjian.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_duquwenjian.setAutoFillBackground(True)
        self.tableWidget_duquwenjian.setStyleSheet("QtableWidget\n"
"{\n"
"    background-color:white\n"
"}\n"
"\n"
"\n"
"QTableWidget::item {\n"
"    color: black;\n"
"}\n"
"")
        self.tableWidget_duquwenjian.setShowGrid(True)
        self.tableWidget_duquwenjian.setRowCount(0)
        self.tableWidget_duquwenjian.setColumnCount(0)
        self.tableWidget_duquwenjian.setObjectName("tableWidget_duquwenjian")
        self.tableWidget_duquwenjian.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_duquwenjian.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_duquwenjian.verticalHeader().setStretchLastSection(False)
        self.pushButton_kaishiyuce = QtWidgets.QPushButton(self.frame)
        self.pushButton_kaishiyuce.setGeometry(QtCore.QRect(970, 640, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_kaishiyuce.setFont(font)
        self.pushButton_kaishiyuce.setObjectName("pushButton_kaishiyuce")
        self.tableWidget_tezhengzhi = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_tezhengzhi.setGeometry(QtCore.QRect(770, 30, 761, 531))
        self.tableWidget_tezhengzhi.setObjectName("tableWidget_tezhengzhi")
        self.tableWidget_tezhengzhi.setColumnCount(6)
        self.tableWidget_tezhengzhi.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_tezhengzhi.setHorizontalHeaderItem(5, item)
        self.tableWidget_tezhengzhi.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tezhengzhi.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_tezhengzhi.verticalHeader().setStretchLastSection(True)
        self.tableWidget_tezhengzhi.setStyleSheet("QtableWidget\n"
                                                   "{\n"
                                                   "    background-color:white\n"
                                                   "}\n"
                                                   "\n"
                                                   "\n"
                                                   "QTableWidget::item {\n"
                                                   "    color: black;\n"
                                                   "}\n"
                                                   "")
        self.frame_menu = QtWidgets.QFrame(Dialog)
        self.frame_menu.setGeometry(QtCore.QRect(0, 0, 1561, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setStyleSheet("QFrame{\n"
"    background-color:rgb(226, 226, 226)\n"
"}")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.label_2 = QtWidgets.QLabel(self.frame_menu)
        self.label_2.setGeometry(QtCore.QRect(710, 20, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_fanhui = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_fanhui.setGeometry(QtCore.QRect(50, 30, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_fanhui.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_fanhui.setFont(font)
        self.pushButton_fanhui.setStyleSheet("QPushButton{\n"
"    border:none\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color:rgb(189, 189, 189);\n"
"}\n"
"")
        self.pushButton_fanhui.setObjectName("pushButton_fanhui")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_kaishizhenduan.setText(_translate("Dialog", "开始诊断"))
        self.tableWidget_duquwenjian.setSortingEnabled(False)
        self.pushButton_kaishiyuce.setText(_translate("Dialog", "开始预测"))
        self.label_2.setText(_translate("Dialog", "故障诊断及预测"))
        self.pushButton_fanhui.setText(_translate("Dialog", "返回"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "均值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "方差"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "标准差"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "最大值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "最小值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "峰值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "均方根值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "方根幅值"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "波形指标"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "峰值指标"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "脉冲指标"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "裕度指标"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "偏斜度"))
        item = self.tableWidget_tezhengzhi.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "峭度"))

        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "大气舱绝压(kPaA)\n"
                                          ""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "高度(m)\n"
                                          ""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "座舱绝压(kPaA)\n"
                                          ""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "座舱余压(kPaA)\n"
                                          ""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "总流量(kg/h)\n"
                                          ""))
        item = self.tableWidget_tezhengzhi.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "控制腔压力(kPaA)\n"
                                          ""))


        self.selectedFile = None

    def populate_table(self):
            if globals.filepaths:
                tablewidget = self.tableWidget_duquwenjian
                tablewidget.setRowCount(len(globals.filepaths))
                tablewidget.setColumnCount(3)
                for index, filepath in enumerate(globals.filepaths):
                        self.selectedFile = filepath
                        item = QTableWidgetItem(str(index+1))
                        tablewidget.setItem(index, 0, item)

                        item = QTableWidgetItem(filepath)
                        tablewidget.setItem(index, 1, item)

                        Button_chakan = QPushButton('选择')
                        Button_chakan.clicked.connect(lambda _, row=index: self.remember_choose_filepath(row))
                        Button_chakan.clicked.connect(self.write_to_tezheng_table)
                        tablewidget.setCellWidget(index, 2, Button_chakan)


    def remember_choose_filepath(self, row):
            filePath = self.tableWidget_duquwenjian.item(row, 1).text()  # 获取当前行文件路径列的值
            SharedData().set_file_path(filePath)
            try:
                    pd.read_excel(filePath)
                    self.showMessage("成功", f"读取文件成功")
            except Exception as e:
                    self.showMessage("错误", f"未选择到文件")


    def showMessage(self, title, message):
        # 显示消息框
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec_()



    def get_excel_feature(self,path):
        '''
        :param column: 需要读取的excel列
        :param data: excel表格数据
        :return:
        '''
        feature = []
        column = ['大气舱绝压(kPaA)', '高度(m)', '座舱绝压(kPaA)', '座舱余压(kPaA)', '总流量(kg/h)', '控制腔压力(kPaA)']

        # 定义获取某一列的时域特征的函数，输入为一维的Dataframe格式的数据
        def get_time_domain_features(data):
            '''data为一维振动信号'''
            fea = []
            len_ = len(data)
            mean_ = data.mean()  # 1.均值
            var_ = data.var()  # 2.方差
            std_ = data.std()  # 3.标准差
            max_ = data.max()  # 4.最大值
            min_ = data.min()  # 5.最小值
            x_p = max(abs(max_), abs(min_))  # 峰值
            x_rms = math.sqrt((data ** 2).sum() / len_)  # 均方根值
            x_r = ((abs(data) ** 0.5).sum() / len_) ** 2  # 方根幅值
            W = x_rms / mean_  # 波形指标
            C = x_p / x_rms  # 峰值指标
            I = x_p / mean_  # 脉冲指标
            L = x_p / x_r  # 裕度指标
            S = ((data - mean_) ** 3).sum() / ((len_ - 1) * std_ ** 3)  # 偏斜度
            K = ((data - mean_) ** 4).sum() / ((len_ - 1) * std_ ** 4)  # 峭度
            fea = [mean_, var_, std_, max_, min_, x_p, x_rms, x_r, W, C, I, L, S, K]
            return fea
        data = pd.read_excel(path)
        for i in column:
            feature.append(get_time_domain_features(data[i]))
        feature = np.concatenate(feature, axis=0)
        return feature.reshape(14, 6)



    def write_to_tezheng_table(self):
        if SharedData().get_file_path():
            data = self.get_excel_feature(SharedData().get_file_path())
            for i in range(self.tableWidget_tezhengzhi.rowCount()):
                for j in range(self.tableWidget_tezhengzhi.columnCount()):
                    if i < data.shape[0] and j < data.shape[1]:
                        item = QTableWidgetItem(str(data[i, j]))
                        self.tableWidget_tezhengzhi.setItem(i, j, item)
