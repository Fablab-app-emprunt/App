from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QRadioButton, QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtGui,QtCore

class EmpruntTypeOutils(QWidget):
    def __init__(self):
        super(EmpruntTypeOutils, self).__init__()
        loadUi('empruntTypeOutils.ui', self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)










if __name__== "__main__":
    app = QApplication([])
    empruntTypeOutils = EmpruntTypeOutils()
    empruntTypeOutils.show()
    app.exec_()

