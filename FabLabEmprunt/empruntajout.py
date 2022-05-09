import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtSql import QSql, QSqlQuery, QSqlDatabase

# from FabLabEmprunt.pageAccueil import PageAccueil

class EmpruntAjout(QWidget, QSqlDatabase):
    def __init__(self):
        super(EmpruntAjout, self).__init__()
        loadUi('empruntAjout.ui',self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.today.clicked.connect(self.date)
        self.dateemprunt.clicked.connect(self.date)


    def accueil(self):
        widget.setCurrentIndex(0)

    def date(self):
        value = self.today.selectedDate()
        return value

if __name__== "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    emprunt_retour = EmpruntAjout()
    widget.addWidget(emprunt_retour)
    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()

    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")