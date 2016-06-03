#!/usr/bin/python
"""Python 3.4.4
PyQt 4.8.7
"""

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time


class MainWindow(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        screen = QLabel()
        screen_img = QImage(800, 480, QImage.Format_RGB32)
        for i in range(800):
            for j in range (480):
                screen_img.setPixel(i, j, qRgb(0,0,0))

        screen_img = QPixmap.fromImage(screen_img)
        screen.setPixmap(screen_img)

        layout.addWidget(screen)

        self.setLayout(layout)

        self.setWindowTitle("EKG Virtual Screen")
        self.setFocus()


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