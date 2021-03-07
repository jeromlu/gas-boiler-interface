#
# Created on Sun Mar 07 2021
#
# Copyright (c) 2021 Your Company
# Name: Luka Jeromel
#
# ******************************Python imports***********************************
import sys

# ******************************PyQt5 imports*************************************
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QDesktopWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget

from PyQt5.QtGui import QIcon

from PyQt5.QtCore import Qt, pyqtSlot

# ******************************Other third party imports************************
import PyViCare

# ******************************My modules***************************************
import data_aquisition


class CareViForm(QMainWindow):
    def __init__(self, parent=None):
        super(CareViForm, self).__init__(parent)

        self.__data = data_aquisition.DataCollector(".")

        self.resize(1024, 768)
        self.setWindowTitle("CareVi")

        self.main_frame = QWidget()
        self.setCentralWidget(self.main_frame)
        self.create_layout()

        # Connections.
        self.pb_show_outside_temp.clicked.connect(self.on_pb_get_out_temp)

    def create_layout(self):

        self.pb_show_outside_temp = QPushButton("Get outside temperature")

        self.lbl_outside_temp = QLabel("TEmp")

        final_layout = QVBoxLayout()
        final_layout.addWidget(self.lbl_outside_temp)
        final_layout.addWidget(self.pb_show_outside_temp)
        self.main_frame.setLayout(final_layout)

    @pyqtSlot(bool)
    def on_pb_get_out_temp(self, clicked):
        temp = self.__data.get_boiler().get_outside_temp()
        self.lbl_outside_temp.setText(f"{temp} \u2103")


def main():
    application = QApplication(sys.argv)
    window = CareViForm()
    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) // 2
    height = (desktop.height() - window.height()) // 2
    window.show()
    window.move(width, height)
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
