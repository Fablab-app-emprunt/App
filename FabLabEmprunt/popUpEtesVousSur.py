
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.uic import *
# importation de la classe pyqtSignal afin de permettre à la fenêtre d'envoyer des données vers une autre fenêtre
from PyQt5.QtCore import pyqtSignal


class PopUpEtesVousSurWidget(QWidget):
    def __init__(self):
        super(PopUpEtesVousSurWidget, self).__init__()
        loadUi('popUpEtesVousSur.ui', self)
        self.boutonoui.clicked.connect(self.reponseOui)
        self.boutonnon.clicked.connect(self.reponseNon)
        self.empruntTypeOutils = EmpruntTypeOutils()


    def reponseOui(self):

        self.empruntTypeOutils.show()
        self.close()

    def reponseNon(self):
        pass








if __name__== "__main__":
    app = QApplication([])
    popUpEtesVousSur = PopUpEtesVousSurWidget()
    popUpEtesVousSur.show()
    app.exec_()


