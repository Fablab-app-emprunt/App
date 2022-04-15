from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox
from PyQt5.uic import loadUi

from FabLabEmprunt.IHM import PageAccueil

class Empruntajout(QWidget):
    def __init__(self):
        super(Empruntajout, self).__init__()
        loadUi('empruntAjout.ui',self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.today.clicked.connect(self.date)
        self.dateemprunt.clicked.connect(self.date)
        self.monIHM = PageAccueil()

    def accueil(self):
        self.monIHM.show()
        self.close()

    def date(self):
        value = self.today.selectedDate()
        return value

if __name__ == "__main__":
    app = QApplication([])
    emprunt = Empruntajout()
    emprunt.show()
    app.exec_()