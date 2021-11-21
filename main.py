import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QColor


class Taskform(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn_show.clicked.connect(self.sshow)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def sshow(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(0, 0, 0))
        d = randint(50, 250)
        qp.drawEllipse(randint(-50, 600), randint(-50, 220), d, d)
        d = randint(50, 250)
        qp.drawEllipse(randint(-50, 600), randint(-50, 220), d, d)
        d = randint(50, 250)
        qp.drawEllipse(randint(-50, 600), randint(-50, 220), d, d)
        d = randint(50, 250)
        d = randint(50, 250)
        qp.drawEllipse(randint(-50, 600), randint(-50, 220), d, d)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Taskform()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
