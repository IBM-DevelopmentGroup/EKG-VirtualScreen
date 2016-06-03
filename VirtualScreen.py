#!/usr/bin/python
"""Python 3.4.4
PyQt 4.8.7
"""

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MainWindow(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.x = self.y = None

        layout = QVBoxLayout()

        # init screen label and layout
        self.screen = QLabel()
        self.mouse_xy = QLabel()
        layout.addWidget(self.screen)
        layout.addWidget(self.mouse_xy)
        self.setLayout(layout)
        self.screen.setMouseTracking(True)

        self.setWindowTitle("EKG Virtual Screen")
        self.setFocus()

        # initiate screen
        self.screen_img = QImage(800, 480, QImage.Format_RGB32)
        for i in range(self.screen_img.width()):
            for j in range(self.screen_img.height()):
                self.screen_img.setPixel(i, j, qRgb(0, 0, 0))

        self.screen.mouseMoveEvent = self.mouse_moved
        self.screen.mousePressEvent = self.xy_clicked

        self.screen.setPixmap(QPixmap.fromImage(self.screen_img))

    def esc_pressed(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def xy_clicked(self, event):
        self.screen_img.setPixel(self.x, self.y, qRgb(255, 0, 0))
        self.screen.setPixmap(QPixmap.fromImage(self.screen_img))

    def mouse_moved(self, event):
        self.x = event.pos().x()
        self.y = event.pos().y()
        self.mouse_xy.setText('x = {}, y = {}'.format(self.x, self.y))


def main():
    """main function

    :return: None
    """

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())