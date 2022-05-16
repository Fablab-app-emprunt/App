import sys

import mysql.connector
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
from FabLabEmprunt.Manager import PageAccueil

class Connection(QWidget):
    def __init__(self):
        super(Connection,self).__init__()
        loadUi('espace_connection.ui', self)
        self.bouton_connection.clicked.connect(self.seConnecter)
        self.linkbouton_inscription.clicked.connect(self.goToInscription)
        self.line_mdp.setEchoMode(2)

    def seConnecter(self):
        mail = self.line_mail.text()
        mdp = self.line_mdp.text()
        widget.setCurrentWidget(page_accueil)

    def goToInscription(self):
        widget.setCurrentWidget(espace_inscription)

class Inscription(QWidget):
    def __init__(self):
        super(Inscription,self).__init__()
        loadUi('espace_inscription.ui', self)
        self.bouton_inscription.clicked.connect(self.InscrireUser)
        self.linkbouton_connection.clicked.connect(self.goToConnexion)
        self.line_mdp.setEchoMode(2)

    def InscrireUser(self):
        widget.setCurrentWidget(espace_connection)

    def goToConnexion(self):
        widget.setCurrentWidget(espace_connection)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    espace_connection = Connection()
    espace_inscription = Inscription()
    page_accueil = PageAccueil()

    widget.addWidget(espace_connection)
    widget.addWidget(espace_inscription)
    widget.addWidget(page_accueil)

    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("exiting")