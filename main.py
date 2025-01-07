from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
import sys
import random

SCREEN_SIZE = [680, 480]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.setFixedSize(*SCREEN_SIZE)
        self.setWindowTitle('Случайные окружности')
        self.pushButton = QPushButton('Рисовать', self)
        self.pushButton.clicked.connect(self.draw)
        self.coords = []

    def draw(self):
        self.size = random.randint(10, 100)
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(self.color)
            qp.setBrush(self.color)
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
