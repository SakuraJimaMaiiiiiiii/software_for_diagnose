from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QLabel, QTableWidgetItem,QMessageBox
from PyQt5.QtGui import QPixmap
from shared_data import SharedData
from jizaizhenduansuanfa import jizaizhenduan
from SVM import SvM
from RF import RFzhenduan

class zhenduanjiemian2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1554, 865)
        Dialog.setStyleSheet("QDialog{\n"
                             "    background-color:rgb(234, 242, 255)\n"
                             "}\n"
                             "\n"
                             "QTableWidget::item {\n"
                             "    background-color:white;\n"
                             "}\n"
                             "QTableWidget::item {\n"
                             "    color: black;\n"
                             "}\n"
                             "\n"
                             "\n"
                             "\n"
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
        self.label = QtWidgets.QLabel(self.frame_menu)
        self.label.setGeometry(QtCore.QRect(740, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_fanhui = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_fanhui.setGeometry(QtCore.QRect(100, 30, 81, 41))
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
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, 90, 1571, 771))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    background-color:rgb(203, 203, 203)\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(90, 180, 851, 400))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(3)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_fanhuishujuxuanze = QtWidgets.QPushButton(self.frame)
        self.pushButton_fanhuishujuxuanze.setGeometry(QtCore.QRect(700, 650, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_fanhuishujuxuanze.setFont(font)
        self.pushButton_fanhuishujuxuanze.setObjectName("pushButton_fanhuishujuxuanze")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_kaishizhenduan = QtWidgets.QPushButton(self.frame)
        self.pushButton_kaishizhenduan.setGeometry(QtCore.QRect(450, 90, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_kaishizhenduan.setFont(font)
        self.pushButton_kaishizhenduan.setObjectName("pushButton_kaishizhenduan")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(240, 90, 120, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frame.raise_()
        self.frame_menu.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_kaishizhenduan.clicked.connect(self.diagnosis)
        self.pushButton_fanhuishujuxuanze.clicked.connect(self.clear_table)

        self.SVM =SvM()

        self.RF = RFzhenduan()

        self.jiezaizhenduan = jizaizhenduan()

        self.zhenduanjieguo = None

        self.QTextEdit = QtWidgets.QTextEdit(self)
        self.QTextEdit.setGeometry(QtCore.QRect(1000, 268, 500, 400))
        self.QTextEdit.setStyleSheet(f"QTextEdit {{ font-size: {25}px; }}")



        self.show_selected_text()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "诊断结果"))
        self.pushButton_fanhui.setText(_translate("Dialog", "返回"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "故障名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "维护信息描述"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "帮助排故信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "当前算法"))
        self.pushButton_fanhuishujuxuanze.setText(_translate("Dialog", "返回数据选择"))
        self.label_2.setText(_translate("Dialog", "当前诊断算法"))
        self.pushButton_kaishizhenduan.setText(_translate("Dialog", "开始诊断"))
        self.comboBox.setItemText(0, _translate("Dialog", "SVM"))
        self.comboBox.setItemText(1, _translate("Dialog", "RF"))
        self.comboBox.setItemText(2, _translate("Dialog", "阈值诊断"))
        self.comboBox.currentIndexChanged.connect(self.show_selected_text)


    # # 获取文件路径
    # def use_file_path(self):
    #     print(f"Using file path: {SharedData().get_file_path()}")

    # 填写表格
    # def write_table(self):
    #     # self.tableWidget.setItem(0, 0, QTableWidgetItem("故障!"))
    #     self.tableWidget.setItem(0, 1, QTableWidgetItem("好好修!"))
    #     self.tableWidget.setItem(0, 2, QTableWidgetItem("加油"))

    # def show_image(self):
    #     self.image_dialog = QDialog(self)
    #     self.image_dialog.setWindowTitle("故障示意图")
    #
    #     a = 1
    #     layout = QVBoxLayout()
    #     label = QLabel(self.image_dialog)
    #     if a:
    #         pic_path = 'pic/RFPIC.jpg'
    #         pixmap = QPixmap(pic_path)  # 替换为你的图片路径
    #         label.setPixmap(pixmap)
    #         layout.addWidget(label)
    #
    #     self.image_dialog.setLayout(layout)
    #     self.image_dialog.exec_()




    def show_selected_text(self):
        # 获取当前选中项的文字
        # type:str
        current_comboBoxText = self.comboBox.currentText()
        self.current_comboBoxText = current_comboBoxText
        if self.current_comboBoxText == 'SVM':
            self.QTextEdit.setText('支持向量机（SVM）通过在高维空间中寻找最佳分割超平面来进行分类\n'
                                   '适用于特征关系复杂但数据采集时间较短的情况，在座舱压力调节系统中诊断的准确率高达91.7%。\n'
                                   '如果您的数据中飞机高度变化较多，座舱压力的变化情况较为复杂，推荐选择支持向量机算法，以获得精确的分类结果。')

        elif self.current_comboBoxText == 'RF':
            self.QTextEdit.setText('随机森林是（RF）一种集成多棵决策树的算法，通过综合多个模型的预测结果来提高诊断的准确性，\n'
                                   '它对噪声和异常值有较强的鲁棒性，适用于数据量较大且噪声较多的情况，在座舱压力调节系统中诊断的准确率高达93.1%。\n'
                                   '如果飞机飞行的时间较长，且在采集数据的过程中存在噪声干扰，推荐选择随机森林算法，以获得高准确率和稳定的诊断结果。')
        else:
            self.QTextEdit.setText('阈值判断基于预设的参数阈值进行故障诊断，适合用于数据变化明显、波动较小且参数稳定的情况，\n'
                                   '在座舱压力调节系统中诊断的准确率高达83.5%。\n'
                                   '如果您的数据特征变化明确且稳定，并且需要实时快速的诊断结果，推荐选择阈值判断算法。')



    def clear_table(self):
        self.tableWidget.clearContents()


    def diagnosis(self):
        if SharedData().get_file_path():
            if self.comboBox.currentText() == 'SVM':
                self.zhenduanjieguo = self.SVM.forward(SharedData().get_file_path())
                self.tableWidget.setItem(0, 1, QTableWidgetItem(self.zhenduanjieguo))
                self.tableWidget.setItem(0, 0, QTableWidgetItem('SVM'))
                if self.zhenduanjieguo == '进气量不足':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('进气不足故障,往往表现为座舱压力偏低'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '进气量过多':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('进气过量故障,往往表现为座舱压力偏高和座舱余压偏高'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '进气量波动':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('进气波动故障,往往表现为座舱压力波动'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '高度保护堵塞':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('高度保护机构堵塞故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查高度保护机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/高度保护故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '减震器漏气':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('增压速率控制机构堵塞故障,往往表现为座舱压力变化速率超标'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查增压速率控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/减震器故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '绝压堵塞':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('绝对压力控制机构堵塞故障,往往表现为座舱压力偏高'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查绝对压力控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/绝压故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '定径孔堵塞':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('定径孔堵塞故障,往往表现为座舱压力偏低'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查绝对压力控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/定径孔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '控制腔泄露到大气':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('控制腔泄漏到大气故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查控制腔泄露点'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/控制腔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '控制腔泄露到高保':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('控制腔泄漏到高度保护机构故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查控制腔泄露点'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/控制腔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '排气活门堵塞':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('排气管路堵塞故障,往往表现为座舱压力偏高，座舱余压偏高'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查排气管路及排气活门'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/排气活门故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '余压堵塞':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('余压控制机构堵塞故障,往往表现为座舱压力偏高，座舱余压偏高，座舱压力变化速率超标'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查余压控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/余压故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '座舱泄露':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('余压控制机构堵塞故障,往往表现为座舱压力偏高，座舱余压偏高，座舱压力变化速率超标'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('排查余压控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/座舱故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '正常':
                    self.tableWidget.setItem(0, 2, QTableWidgetItem('一切正常'))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem('一切正常'))
                else:
                    pass

            elif self.comboBox.currentText() == 'RF':
                self.zhenduanjieguo = self.RF.zhenduan(filename=SharedData().get_file_path(), modelname='rf.model')
                self.tableWidget.setItem(1, 1, QTableWidgetItem(self.zhenduanjieguo))
                self.tableWidget.setItem(1, 0, QTableWidgetItem('RF'))
                if self.zhenduanjieguo == '进气量不足':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('进气不足故障,往往表现为座舱压力偏低'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '进气量过多':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('进气过量故障,往往表现为座舱压力偏高和座舱余压偏高'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '进气量波动':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('进气波动故障,往往表现为座舱压力波动'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '高度保护堵塞':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('高度保护机构堵塞故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查高度保护机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/高度保护故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '减震器漏气':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('增压速率控制机构堵塞故障,往往表现为座舱压力变化速率超标'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查增压速率控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/减震器故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '绝压堵塞':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('绝对压力控制机构堵塞故障,往往表现为座舱压力偏高'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查绝对压力控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/绝压故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '定径孔堵塞':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('定径孔堵塞故障,往往表现为座舱压力偏低'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查绝对压力控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/定径孔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '控制腔泄露到大气':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('控制腔泄漏到大气故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查控制腔泄露点'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/控制腔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '控制腔泄露到高保':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('控制腔泄漏到高度保护机构故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查控制腔泄露点'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/控制腔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '排气活门堵塞':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('排气管路堵塞故障,往往表现为座舱压力偏高，座舱余压偏高'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查排气管路及排气活门'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/排气活门故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '余压堵塞':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('余压控制机构堵塞故障,往往表现为座舱压力偏高，座舱余压偏高，座舱压力变化速率超标'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查余压控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/余压故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '座舱泄露':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('余压控制机构堵塞故障,往往表现为座舱压力偏高，座舱余压偏高，座舱压力变化速率超标'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('排查余压控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/座舱故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '正常':
                    self.tableWidget.setItem(1, 2, QTableWidgetItem('一切正常'))
                    self.tableWidget.setItem(1, 3, QTableWidgetItem('一切正常'))
                else:
                    pass


            elif self.comboBox.currentText() == '阈值诊断':
                locations, _ = jizaizhenduan().run(SharedData().get_file_path())
                self.zhenduanjieguo = locations
                self.zhenduanjieguo = ','.join(self.zhenduanjieguo)
                self.tableWidget.setItem(2, 1, QTableWidgetItem(self.zhenduanjieguo))
                self.tableWidget.setItem(2, 0, QTableWidgetItem('阈值诊断'))
                if self.zhenduanjieguo == '进气量不足':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('进气不足故障,往往表现为座舱压力偏低'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '进气量过多':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('进气过量故障,往往表现为座舱压力偏高和座舱余压偏高'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '进气量波动':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('进气波动故障,往往表现为座舱压力波动'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查供气管路'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/引气系统故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '高度保护堵塞':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('高度保护机构堵塞故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查高度保护机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/高度保护故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '减震器漏气':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('增压速率控制机构堵塞故障,往往表现为座舱压力变化速率超标'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查增压速率控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/减震器故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '绝压堵塞':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('绝对压力控制机构堵塞故障,往往表现为座舱压力偏高'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查绝对压力控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/绝压故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '定径孔堵塞':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('定径孔堵塞故障,往往表现为座舱压力偏低'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查绝对压力控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/定径孔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '控制腔泄露到大气':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('控制腔泄漏到大气故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查控制腔泄露点'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/控制腔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '控制腔泄露到高保':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('控制腔泄漏到高度保护机构故障,往往表现为座舱压力偏低，漏气量超差，座舱失密'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查控制腔泄露点'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/控制腔故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '排气活门堵塞':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('排气管路堵塞故障,往往表现为座舱压力偏高，座舱余压偏高'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查排气管路及排气活门'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/排气活门故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '余压堵塞':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('余压控制机构堵塞故障,往往表现为座舱压力偏高，座舱余压偏高，座舱压力变化速率超标'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查余压控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/余压故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '座舱泄露':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('余压控制机构堵塞故障,往往表现为座舱压力偏高，座舱余压偏高，座舱压力变化速率超标'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('排查余压控制机构'))

                    self.image_dialog = QDialog()
                    self.image_dialog.setWindowTitle("故障示意图")
                    layout = QVBoxLayout()
                    label = QLabel(self.image_dialog)
                    pic_path = 'pic/座舱故障.png'
                    pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                    label.setPixmap(pixmap)
                    layout.addWidget(label)
                    self.image_dialog.setLayout(layout)
                    self.image_dialog.exec_()


                elif self.zhenduanjieguo == '正常':
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('一切正常'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('一切正常'))


                else:
                    self.tableWidget.setItem(2, 2, QTableWidgetItem('检测到多个故障'))
                    self.tableWidget.setItem(2, 3, QTableWidgetItem('检测到多个故障'))

        elif not SharedData().get_file_path():
            QMessageBox.warning(self, '警告', '请选择故障数据！')
            return


