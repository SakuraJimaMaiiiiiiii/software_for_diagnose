from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton
from window_main import Mainwindow
from window_shujuguanli import shujuguanli
from window_shujuguanli2 import shujuguanli2
from window_shujuguanli3 import shujuguanli3
from window_suanfaguanli import suanfaguanli
from window_zhenduanjiemian_1 import zhenduanjiemian1
from window_zhenduanjiemian_2 import zhenduanjiemian2
from window_zhenduanjiemian_3 import zhenduanjiemian3
from window_zhenduansuanfaguanli import zhenduanguanli
from window_yucesuanfaguanli import yuceguanli
import sys

'''
主界面
'''


class Main(QMainWindow, Mainwindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        # 主界面按钮管理
        self.pushButton_shujuku.clicked.connect(self.button_to_shujuku)
        self.pushButton_suanfa.clicked.connect(self.button_to_suanfa)
        self.pushButton_zhenduan.clicked.connect(self.button_to_zhenduanjiemian1)


    def button_to_shujuku(self):
        self.close()
        shujukuguanli_child.show()

    def button_to_suanfa(self):
        suanfaguali_child.show()

    def button_to_zhenduanjiemian1(self):
        self.close()
        zhenduanjiemian_1_child.show()


'''
数据库管理
'''


class shujukuguanli(QMainWindow, shujuguanli):
    def __init__(self, shujuguanli2,zhenduanjiemian1):
        super(shujukuguanli, self).__init__()
        self.setupUi(self)
        self.pushButton_fanhui.clicked.connect(self.button_to_main)
        self.pushButton_chakanshuju.clicked.connect(self.button_to_shujuguanli2)
        self.pushButton_chakanshuju.clicked.connect(shujuguanli2.loadData)
        self.pushButton_chakanshuju.clicked.connect(shujuguanli2.write_to_tezheng_table)
        self.pushButton_fanhui.clicked.connect(zhenduanjiemian1.populate_table)



    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_main(self):
        self.close()
        main.show()

    def button_to_shujuguanli2(self):
        self.close()
        shujukuguanli2_child.show()




'''
数据库管理2
'''


class shujukuguanli2(QMainWindow, shujuguanli2):
    def __init__(self,shujuguanli3):
        super(shujukuguanli2, self).__init__()
        self.setupUi(self)
        self.pushButton_fanhui.clicked.connect(self.button_to_shujuguanli)
        self.pushButton_huitu.clicked.connect(self.button_to_shujuguanli3)
        self.pushButton_huitu.clicked.connect(shujuguanli3.pushButton_huitu.clicked)
    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_shujuguanli(self):
        self.close()
        shujukuguanli_child.show()

    def button_to_shujuguanli3(self):
        self.close()
        shujukuguanli3_child.show()


'''
数据库管理3
'''


class shujukuguanli3(QMainWindow, shujuguanli3):
    def __init__(self):
        super(shujukuguanli3, self).__init__()
        self.setupUi(self)
        self.pushButton_fanhui.clicked.connect(self.button_to_shujuguanli2)

    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_shujuguanli2(self):
        self.close()
        shujukuguanli2_child.show()


'''
算法管理
'''


class suanfaguali(QMainWindow, suanfaguanli):
    def __init__(self):
        super(suanfaguali, self).__init__()
        self.setupUi(self)
        self.pushButton_zhenduanguanli.clicked.connect(self.button_to_zhenduanguanli)
        self.pushButton_yucesuanfaguanli.clicked.connect(self.button_to_yuceguanli)

    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_zhenduanguanli(self):
        self.close()
        main.close()
        zhenduansuanfaguanli_child.show()

    def button_to_yuceguanli(self):
        main.close()
        self.close()
        yucesuanfaguanli_child.show()




'''
诊断算法管理
'''


class zhenduansuanfaguanli(QMainWindow, zhenduanguanli):
    def __init__(self):
        super(zhenduansuanfaguanli, self).__init__()
        self.setupUi(self)
        self.pushButton_fanhui.clicked.connect(self.button_to_suanfaguali_child)

    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_suanfaguali_child(self):
        self.close()
        main.show()
        suanfaguali_child.show()







'''
预测算法管理
'''


class yucesuanfaguanli(QMainWindow, yuceguanli):
    def __init__(self):
        super(yucesuanfaguanli, self).__init__()
        self.setupUi(self)
        self.pushButton_fanhui.clicked.connect(self.button_to_suanfaguali_child)

    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_suanfaguali_child(self):
        self.close()
        main.show()
        suanfaguali_child.show()


'''
诊断界面1
'''


class zhenduanjiemian_1(QMainWindow, zhenduanjiemian1):
    def __init__(self):
        super(zhenduanjiemian_1, self).__init__()
        self.setupUi(self)
        self.pushButton_fanhui.clicked.connect(self.button_to_main)

        self.pushButton_kaishizhenduan.clicked.connect(self.button_to_zhenduanjiemian2)
        self.pushButton_kaishiyuce.clicked.connect(self.button_to_zhenduanjiemian3)


    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_main(self):
        self.close()
        main.show()

    def button_to_zhenduanjiemian2(self):
        self.close()
        zhenduanjiemian_2_child.show()

    def button_to_zhenduanjiemian3(self):
        self.close()
        zhenduanjiemian_3_child.show()



'''
诊断界面2
'''


class zhenduanjiemian_2(QMainWindow, zhenduanjiemian2):
    def __init__(self):
        super(zhenduanjiemian_2, self).__init__()
        self.setupUi(self)
        self.pushButton_fanhui.clicked.connect(self.button_to_zhenduanjiemian1)
        self.pushButton_fanhuishujuxuanze.clicked.connect(self.button_to_zhenduanjiemian1)
        # self.pushButton_chakanyucejieguo.clicked.connect(self.button_to_zhenduanjiemian3)


    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_zhenduanjiemian1(self):
        self.close()
        zhenduanjiemian_1_child.show()

    #
    # def button_to_zhenduanjiemian3(self):
    #     self.close()
    #     zhenduanjiemian_3_child.show()




'''
诊断界面3
'''

class zhenduanjiemian_3(QMainWindow, zhenduanjiemian3):
    def __init__(self):
        super(zhenduanjiemian_3, self).__init__()
        self.setupUi(self)
        self.pushButton_fanhui.clicked.connect(self.button_to_zhenduanjiemian1)
        self.pushButton_fanhuishujuxuanze.clicked.connect(self.button_to_zhenduanjiemian1)

    def Open(self):
        self.show()

    def Close(self):
        self.close()

    def button_to_zhenduanjiemian1(self):
        self.close()
        zhenduanjiemian_1_child.show()




##############################################################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)


    file_path = ''


    # 实例化


    zhenduanjiemian_2_child = zhenduanjiemian_2()

    zhenduanjiemian_3_child = zhenduanjiemian_3()

    shujukuguanli3_child = shujukuguanli3()

    shujukuguanli2_child = shujukuguanli2(shujukuguanli3_child)

    zhenduanjiemian_1_child = zhenduanjiemian_1()

    shujukuguanli_child = shujukuguanli(shujukuguanli2_child,zhenduanjiemian_1_child)





    zhenduansuanfaguanli_child = zhenduansuanfaguanli()

    yucesuanfaguanli_child = yucesuanfaguanli()

    suanfaguali_child = suanfaguali()







    main = Main()

    main.show()


    sys.exit(app.exec_())

