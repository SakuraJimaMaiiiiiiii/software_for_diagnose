import sys
from PyQt5.QtWidgets import QApplication, QLabel,QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap


def showpic():
    app = QApplication(sys.argv)

    # 创建一个标签
    label = QLabel()

    # 加载图片
    pixmap = QPixmap('pic/SVMpic.png')  # 替换为你的图片路径
    label.setPixmap(pixmap)

    # 调整标签大小以适应图片
    label.resize(pixmap.width(), pixmap.height())

    # 显示标签
    label.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    showpic()
