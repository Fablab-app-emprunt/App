from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QRadioButton, QPushButton
from PyQt5.uic import loadUi


class EmpruntTypeOutils(QWidget):
    def __init__(self):
        super(EmpruntTypeOutils, self).__init__()
        loadUi('empruntTypeOutils.ui', self)










if __name__== "__main__":
    app = QApplication([])
    empruntTypeOutils = EmpruntTypeOutils()
    empruntTypeOutils.show()
    app.exec_()

