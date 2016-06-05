#!/usr/bin/python
"""Python 3.4.4
PyQt 4.8.7
pySerial 3.1
"""

import sys
import serial
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MainWindow(QDialog):
    received_msg = pyqtSignal()

    def __init__(self, serial_port):
        QDialog.__init__(self)
        self.x = self.y = None
        self.serial_port = serial_port

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
        self.send_click_xy()

    def mouse_moved(self, event):
        self.x = event.pos().x()
        self.y = event.pos().y()
        self.mouse_xy.setText('x = {}, y = {}'.format(self.x, self.y))

    def send_click_xy(self):
        msg = u'TXY X{} Y{}\r\n'.format(self.x, self.y)
        print(msg, end='')
        self.serial_port.write(msg.encode())

    def read_from_device(self):
        self.received_msg.connect(self.print_msg)
        msg = b''
        while 1:
            if self.serial_port.inWaiting():
                msg = self.serial_port.readline().decode()
                self.received_msg.emit()
                if msg == 'exit\r\n':
                    break

    def print_msg(self):
        print('fuck yeah')


def main():
    with serial.Serial('COM1', 9600) as ser:
        app = QApplication(sys.argv)
        win = MainWindow(ser)
        win.show()
        win.read_from_device()
        app.exec()


if __name__ == "__main__":
    sys.exit(main())