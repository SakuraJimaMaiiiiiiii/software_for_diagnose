from PyQt5.QtWidgets import QMessageBox, QGraphicsScene
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLineEdit
import matplotlib
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QLabel, QTableWidgetItem


matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class zhenduanguanli(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1554, 865)
        Dialog.setStyleSheet("QDialog{\n"
                             "    background-color:white\n"
                             "}\n"
                             "\n"
                             "QTableWidget::item {\n"
                             "   color:black;\n"
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
        self.label_biaoti = QtWidgets.QLabel(self.frame_menu)
        self.label_biaoti.setGeometry(QtCore.QRect(700, 20, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_biaoti.setFont(font)
        self.label_biaoti.setObjectName("label_biaoti")
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
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, 90, 1571, 771))
        self.frame.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("QFrame{\n"
                                 "    background-color:rgb(203, 203, 203)\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 0, 1001, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(110, 30, 1300, 250))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(3)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_canshushuru = QtWidgets.QLabel(self.frame)
        self.label_canshushuru.setGeometry(QtCore.QRect(110, 330, 140, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_canshushuru.setFont(font)
        self.label_canshushuru.setObjectName("label_suanfaxiangqing")

        self.QTextEdit = QtWidgets.QTextEdit(self)
        self.QTextEdit.setGeometry(QtCore.QRect(105, 480, 1300, 300))
        self.QTextEdit.setStyleSheet(f"QTextEdit {{ font-size: {25}px; }}")




        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        for row in range(self.tableWidget.rowCount()):
            btn = QPushButton('查看')
            btn.clicked.connect(self.viewButtonClicked)
            self.tableWidget.setCellWidget(row, 4, btn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_biaoti.setText(_translate("Dialog", "系统诊断算法管理"))
        self.pushButton_fanhui.setText(_translate("Dialog", "返回"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "支持向量机"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "随机森林"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "阈值诊断算法"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "版本号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "导入人"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "导入日期"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "推荐程度"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "算法查看"))

        item = QtWidgets.QTableWidgetItem("V1.0")
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem("小谢")
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem("2024/6/24")
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem("⭐⭐⭐⭐⭐")
        self.tableWidget.setItem(0, 3, item)

        item = QtWidgets.QTableWidgetItem("V1.0")
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem("小刘")
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem("2024/6/24")
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem("⭐⭐⭐⭐⭐")
        self.tableWidget.setItem(1, 3, item)

        item = QtWidgets.QTableWidgetItem("V1.0")
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem("小席")
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem("2024/6/24")
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem("⭐⭐")
        self.tableWidget.setItem(2, 3, item)

        self.label_canshushuru.setText(_translate("Dialog", "当前参数输入："))


    def viewButtonClicked(self):
        # 获取按钮所在的行
        button = self.sender()
        if button:
            index = self.tableWidget.indexAt(button.pos())
            if index.isValid():
                row = index.row()
                QMessageBox.information(self, '算法查看', f'查看算法：{self.tableWidget.verticalHeaderItem(row).text()}')
                if row == 0:
                    pixmap = QPixmap("pic/SVMpic.png")
                    if not pixmap.isNull():
                        scene = QGraphicsScene()
                        scene.addPixmap(pixmap)


                        self.image_dialog = QDialog()
                        self.image_dialog.setWindowTitle("算法流程图")
                        layout = QVBoxLayout()
                        label = QLabel(self.image_dialog)
                        pic_path = pixmap
                        pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                        label.setPixmap(pixmap)
                        layout.addWidget(label)
                        self.image_dialog.setLayout(layout)
                        self.image_dialog.exec_()

                        self.QTextEdit.setText("核函数:{}\n正则化参数:{}\nGamma:{}\n多项式核的次数:{}".format('rbf', 1000, 1, 1))

                if row == 1:
                    pixmap = QPixmap("pic/RFPIC.jpg")
                    if not pixmap.isNull():
                        scene = QGraphicsScene()
                        scene.addPixmap(pixmap)


                        self.image_dialog = QDialog()
                        self.image_dialog.setWindowTitle("算法流程图")
                        layout = QVBoxLayout()
                        label = QLabel(self.image_dialog)
                        pic_path = pixmap
                        pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                        label.setPixmap(pixmap)
                        layout.addWidget(label)
                        self.image_dialog.setLayout(layout)
                        self.image_dialog.exec_()

                        self.QTextEdit.setText("决策树数量:{}\n最大深度:{}\n最大特征数:{}\n".format(1, 2, 3))


                if row == 2:
                    pixmap = QPixmap("pic/阈值诊断流程图.png")
                    # pixmap = QPixmap("pic/tes.png")

                    if not pixmap.isNull():
                        scene = QGraphicsScene()
                        scene.addPixmap(pixmap)
                        self.image_dialog = QDialog()
                        self.image_dialog.setWindowTitle("算法流程图")
                        layout = QVBoxLayout()
                        label = QLabel(self.image_dialog)
                        pic_path = pixmap
                        pixmap = QPixmap(pic_path)  # 替换为你的图片路径
                        label.setPixmap(pixmap)
                        layout.addWidget(label)
                        self.image_dialog.setLayout(layout)
                        self.image_dialog.exec_()
                        self.QTextEdit.setText('var_pressure_high1(绝压区绝对压力偏高):cockpit_pressure>=76.69770476\n'
                                               'var_pressure_low1(绝压区绝对压力偏低):cockpit_pressure<=72.5949401807504\n'
                                               'var_pressure_low4(绝压区绝对压力过低):cockpit_pressure<=65\n'
                                               'var_pressure_low5(高度保护):cockpit_pressure<=40.0857960325781\n'
                                               'var_pressure_low6(高度保护):cockpit_pressure>=38.2165644250258\n'
                                               'var_pressure_high2(自由通风区绝对压力偏高):cockpit_residual_pressure>=4.77311684196114\n'
                                               'var_pressure_low2(自由通风区绝对压力偏低):cockpit_residual_pressure<=-4.36430860862337\n'
                                               'var_pressure_high3(余压区绝对压力偏高):cockpit_residual_pressure>=37.1443939413015\n'
                                               'var_pressure_low3(余压区绝对压力偏低):cockpit_residual_pressure<=33.9215843169342\n'
                                               'var_residual_high(余压偏高):cockpit_residual_pressure>40\n'
                                               'var_residual_low(余压偏低):cockpit_residual_pressure<14.2297\n'
                                               'var_up_overrun(座舱压力变化率最高):pressure_rate_of_change>0.600124213\n'
                                               'var_down_overrun(座舱压力变化率最低):pressure_rate_of_change<-1.10371071804501\n'
                                               'var_rate_up(座舱压力变化率上升):pressure_rate_of_change>0\n'
                                               'var_residual_pressure_rate_of_change(余压变化率):residual_pressure_rate_of_change>0.68563\n'
                                               'var_nomal_pressure(自由通风):atmospheric_pressure>75.3\n'
                                               'var_residual_pressure(余压区):atmospheric_pressure<40.8\n'
                                               'var_altitude_low(绝压区高度限制):altitude<=2750.43096094306\n'
                                               'var_altitude_high(绝压区高度限制):altitude>=6856.84766377059\n'
                                               'var_altitude_toohigh(绝压区高度限制):altitude>=11849.2870252768\n'
                                               'var_up_overrun(座舱压力变化率最高):chamber_pressure>0.600124213\n'
                                               'var_chamber1(控制腔压力):chamber_pressure<=75.57516989\n'
                                               'var_chamber2(控制腔压力):chamber_pressure>=71.18857645\n'
                                               'var_chamber_rate(控制腔压力变化率):chamber_pressure_rate_of_change<0.01\n'
                                               'var_rate1(座舱压力变化率受限):pressure_rate_of_change>0.595869282400302\n'
                                               'var_rate2(座舱压力变化率受限):pressure_rate_of_change<0.235496048407197\n'
                                               'var_gas_flow_high(进气流量过大):gas_flow>652.2815\n'
                                               'var_gas_flow_low(进气流量不足):gas_flow<243.444')
