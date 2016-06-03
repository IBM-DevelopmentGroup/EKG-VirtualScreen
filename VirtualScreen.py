#!/usr/bin/python
"""Python 3.4.4
PyQt 4.8.7
Pillow 3.2.0
"""

import sys
from PIL import Image
from PyQt4.QtGui import *
import time


def main():
    img_file = "my_image.png"
    img = Image.new('RGB', (800, 480), "black")  # create a new black image
    pixels = img.load()  # create the pixel map

    for i in range(img.size[0]):  # for every pixel:
        for j in range(img.size[1]):
            pixels[i, j] = (i, j, 100)  # set the colour accordingly

    img.save(img_file, "png")
    image = Image.open(img_file)

    app = QApplication(sys.argv)
    win = QWidget()
    l1 = QLabel()
    l1.setPixmap(QPixmap(img_file))

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    win.setLayout(vbox)
    win.setWindowTitle("QPixmap Demo")
    win.show()

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    sys.exit(main())