import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtSql
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox, QVBoxLayout

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox, QTableWidgetItem

from PyQt5.QtSql import QSql, QSqlQuery, QSqlDatabase
import mysql.connector


state = ''
requete_Outils = ''
Data = []

class PageAccueil(QWidget):
    def __init__(self):
        super(PageAccueil,self).__init__()
        loadUi('pageAccueil.ui',self)
        self.rendreoutils.clicked.connect(self.goToRendreOutils)
        self.emprunteroutils.clicked.connect(self.goToEmprunterOutils)


    def goToRendreOutils(self):
        widget.setCurrentIndex(1)
        global state
        state = 'Rendre'
        print(state)

    def goToEmprunterOutils(self):
        widget.setCurrentIndex(1)
        global state
        state = 'Emprunter'
        print(state)


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
        print("Index Accueil : ",widget.currentIndex())

    def bois(self):
        global requete_Outils
        requete_Outils = 'BOIS'
        page_choix_outils = EmpruntAjout()
        widget.addWidget(page_choix_outils)
        widget.setCurrentIndex(2)

    def elec(self):
        global requete_Outils
        requete_Outils = 'ELEC'
        page_choix_outils = EmpruntAjout()
        widget.addWidget(page_choix_outils)
        widget.setCurrentIndex(2)

    def usinage(self):
        global requete_Outils
        widget.setCurrentIndex(2)
        requete_Outils = 'USINAGE'
        page_choix_outils = EmpruntAjout()
        widget.addWidget(page_choix_outils)
        widget.setCurrentIndex(2)

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

        global state
        global requete_Outils
        global Data
        print(requete_Outils)
        print("valeur : ",state)
        self.table_Emprunt.setColumnCount(4)
        self.table_Emprunt.rowCount()
        self.table_Emprunt.setHorizontalHeaderLabels(['id','Name','Quantity',state])
        row = self.table_Emprunt.rowCount()
        self.table_Emprunt.setRowCount(row+1)
        col = 0
        connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                             host='145.14.151.101',
                                             database='u556968436_fablab')

        count_tools = "select * from Outils where departOutils_Outils = '"+requete_Outils+"'"
        cursor = connection.cursor()
        cursor.execute(count_tools)
        Data = cursor.fetchall()
        for item in Data:
            cell = QTableWidgetItem(str(item[0]))
            self.table_Emprunt.setItem(row, col, cell)

            cell = QTableWidgetItem(str(item[3]))
            self.table_Emprunt.setItem(row, col+1, cell)

            row += 1
            self.table_Emprunt.setRowCount(row+1)

    def accueil(self):
       widget.setCurrentIndex(0)

    def date(self):
        value = self.today.selectedDate()
        date_in_string = str(value.toPyDate())
        print(date_in_string)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    page_accueil = PageAccueil()
    page_choix_type_outils = EmpruntTypeOutils()
    # page_choix_outils = EmpruntAjout()

    widget.addWidget(page_accueil)
    widget.addWidget(page_choix_type_outils)
    # widget.addWidget(page_choix_outils)

    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()

    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")