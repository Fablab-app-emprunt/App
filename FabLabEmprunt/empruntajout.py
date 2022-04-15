from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox
from PyQt5.uic import loadUi

class empruntajout(QWidget):
    def __init__(self):
        super(empruntajout, self).__init__()
        loadUi('empruntAjout.ui',self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.today.clicked.connect(self.date)
        self.dateemprunt.clicked.connect(self.date)

    def accueil(self):
        QMessageBox.about(self, "Title", "Message")

    def date(self):
        value = self.today.selectedDate()
        print(value)
app = QApplication([])
emprunt = empruntajout()
emprunt.show()
app.exec_()
