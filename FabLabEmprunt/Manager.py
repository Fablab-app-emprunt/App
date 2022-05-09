import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtSql
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox
from PyQt5.QtSql import QSql, QSqlQuery, QSqlDatabase
import mysql.connector

global requete_Outils

class PageAccueil(QWidget):
    def __init__(self):
        super(PageAccueil,self).__init__()
        loadUi('pageAccueil.ui',self)
        self.rendreoutils.clicked.connect(self.goToRendreOutils)
        self.emprunteroutils.clicked.connect(self.goToEmprunterOutils)


    def goToRendreOutils(self):
        widget.setCurrentIndex(1)

    def goToEmprunterOutils(self):
        widget.setCurrentIndex(1)


class EmpruntTypeOutils(QWidget):
    def __init__(self):
        super(EmpruntTypeOutils, self).__init__()
        loadUi('empruntTypeOutils.ui', self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.bouton_electronique.clicked.connect(self.elec)
        self.bouton_bois.clicked.connect(self.bois)
        self.bouton_usinage.clicked.connect(self.usinage)
        self.boutonaccueil.clicked.connect(self.accueil)

    def accueil(self):
        widget.setCurrentIndex(0)

    def conn_BDD(self, requete_Outils):
        #---------BDD----------------

        #-----------Déclaration de la connexion---------
        connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                             host='145.14.151.101',
                                             database='u556968436_fablab')
        # sql_select_Query = "select * from Personnes"
        # cursor = connection.cursor()
        # cursor.execute(sql_select_Query)
        # # get all records
        # records = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        #
        # print("\nPrinting each row")
        # for row in records:
        #     print("Id = ", row[1], )
        #
        # connection.close()
        count_tools = "select count(*) from Outils where departOutils_Outils = '" + requete_Outils + "'"
        cursor = connection.cursor()
        cursor.execute(count_tools)
        outils = cursor.fetchall()
        for row in outils:
            print("Id = ", row[0], )
        connection.close()
        #----------Requêtes de modification------------

        # query = QSqlQuery("insert into Utilisateur (login) values ('david')")

        #                OU

        #         # query = QSqlQuery()
        #         # query.exec_("insert into Utilisateur (login) values ('david')")
        #
        #     #----------Requêtes préparées------------ (utile lorsqu'on utilise des variables)
        #
        #         # query = QSqlQuery()
        #         # query.prepare("insert into Utilisateur (login) values (:nom)")
        # query.bindValue(":nom", "david")
        # query.exec_()

        #-----------Gestion des erreurs---------------

        # db.open("login", "motdepasse")
        # if db.isOpenError():
        #     error = db.lastError()


    def bois(self):
        widget.setCurrentIndex(2)
        requete_Outils = 'BOIS'

    def elec(self):
        widget.setCurrentIndex(2)
        requete_Outils = 'ELEC'
        self.conn_BDD(requete_Outils)

    def usinage(self):
        widget.setCurrentIndex(2)
        requete_Outils = 'USINAGE'

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

if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    # from FabLabEmprunt.pageAccueil import *
    # from FabLabEmprunt.empruntTypeOutils import *
    # from FabLabEmprunt.empruntajout import *

    page_accueil = PageAccueil()
    page_choix_type_outils = EmpruntTypeOutils()
    page_choix_outils = EmpruntAjout()

    widget.addWidget(page_accueil)
    widget.addWidget(page_choix_type_outils)
    widget.addWidget(page_choix_outils)

    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()

    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")