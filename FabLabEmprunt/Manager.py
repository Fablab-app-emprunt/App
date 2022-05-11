import sys
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets, QtSql
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox, QTableWidgetItem, QCheckBox, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox, QVBoxLayout

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox, QTableWidgetItem

from PyQt5.QtSql import QSql, QSqlQuery, QSqlDatabase
import mysql.connector


state = ''
requete_Outils = ''
Requete_Outils = ['ELEC','BOIS','USINAGE']
page_choix_outils = ['page_choix_outils_elec','page_choix_outils_bois','page_choix_outils_usinage']
pop_up = ['pop_up_elec','pop_up_bois','pop_up_usinage']
Data = []
Lelec = []
Lbois = []
Lusinage = []

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
        print("Index rendreoutils : ",widget.indexOf(page_choix_type_outils))
        self.creationPages()

    def goToEmprunterOutils(self):
        widget.setCurrentIndex(1)
        global state
        state = 'Emprunter'
        print("Index emprunteroutils : ",widget.indexOf(page_choix_type_outils))
        self.creationPages()

    def creationPages(self):
#----------------CREATION PAGES ELEC BOIS USINAGE ET LES POPUPS--------------------------------
        global requete_Outils
        global Requete_Outils
        global page_choix_outils
        global pop_up
        print(requete_Outils)
        for i in range(3):
            requete_Outils = Requete_Outils[i]
            print(requete_Outils)
            page_choix_outils[i] = EmpruntAjout()
            widget.insertWidget(2*i+2,page_choix_outils[i])
            print("Index of : ", requete_Outils,' is ', widget.indexOf(page_choix_outils[i]))
            pop_up[i] = PopUpListeEmpruntsWidget()
            widget.insertWidget(2*i+3,pop_up[i])
            print("Index of : pop up ", requete_Outils,' is ', widget.indexOf(pop_up[i]))


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
        self.rendreOutils_4.clicked.connect(self.validate)

    def accueil(self):
        widget.setCurrentIndex(0)

    def elec(self):
        widget.setCurrentIndex(2)
        global requete_Outils
        requete_Outils = 'ELEC'

    def bois(self):
        widget.setCurrentIndex(4)
        global requete_Outils
        requete_Outils = 'BOIS'

    def usinage(self):
        widget.setCurrentIndex(6)
        global requete_Outils
        requete_Outils = 'USINAGE'

    def validate(self):
        global Lelec
        global Lbois
        global Lusinage
        Lfinal=[]
        for i in range(len(Lelec)):
            Lfinal.append(Lelec[i])
        for i in range(len(Lbois)):
            Lfinal.append(Lbois[i])
        for i in range(len(Lusinage)):
            Lfinal.append(Lusinage[i])
        print(Lfinal)

class EmpruntAjout(QWidget, QSqlDatabase):
    def __init__(self):

        super(EmpruntAjout, self).__init__()
        loadUi('empruntAjout.ui',self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.today.clicked.connect(self.date)
        self.boutonvalider.clicked.connect(self.recupdata)
        self.dateemprunt.clicked.connect(self.date)
        self.boutonvalider.clicked.connect(self.goToPopUpListeEmprunts)
        self.rendreOutils_6.clicked.connect(self.returntypeoutils)

        global state
        global requete_Outils
        global Data
        self.table_Emprunt.setColumnCount(4)
        self.table_Emprunt.rowCount()
        self.table_Emprunt.setHorizontalHeaderLabels(['id','Name','Quantity',state])
        row = self.table_Emprunt.rowCount()
        self.table_Emprunt.setRowCount(row+1)
        col = 0
        connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                             host='145.14.151.101',
                                             database='u556968436_fablab')
        if state == 'Emprunter':
            count_tools = "select * from Outils where departOutils_Outils = '"+requete_Outils+"'"
        elif state == 'Rendre':
            count_tools = "select * from Outils where departOutils_Outils = '"+requete_Outils+"'"
            print("Pas encore fait")
        cursor = connection.cursor()
        cursor.execute(count_tools)
        Data = cursor.fetchall()

#-------------REMPLIR LES TABLEAUX---------------------
        for item in Data:
            cell = QTableWidgetItem(str(item[0]))
            self.table_Emprunt.setItem(row, col, cell)

            cell = QTableWidgetItem(str(item[1]))
            self.table_Emprunt.setItem(row, col+1, cell)

            cell = QTableWidgetItem(str(item[3]))
            self.table_Emprunt.setItem(row, col+2, cell)

            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.table_Emprunt.setItem(row,col+3,chkBoxItem)
            row += 1
            self.table_Emprunt.setRowCount(row+1)

            header = self.table_Emprunt.horizontalHeader()
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

    def recupdata(self):
        global requete_Outils
        global Lelec
        global Lbois
        global Lusinage
        if requete_Outils == 'ELEC':
            Lelec = []
        elif requete_Outils == 'BOIS':
            Lbois = []
        elif requete_Outils == 'USINAGE':
            Lusinage = []
        for row in range(self.table_Emprunt.rowCount()-1):
            L=[]
            if self.table_Emprunt.item(row,3).checkState() == QtCore.Qt.CheckState.Checked:
                for col in range(self.table_Emprunt.columnCount()-3):
                    L.append(self.table_Emprunt.item(row,0).text())
                    print(L)
                if requete_Outils == 'ELEC':
                    Lelec.append(L[0])
                elif requete_Outils == 'BOIS':
                    Lbois.append(L[0])
                elif requete_Outils == 'USINAGE':
                    Lusinage.append(L[0])
        print(Lelec)
        print(Lbois)
        print(Lusinage)

    def accueil(self):
       widget.setCurrentIndex(0)

    def returntypeoutils(self):
        global state
        if state == 'Emprunter':
            widget.setCurrentIndex(1)
        elif state == 'Rendre' :
            widget.setCurrentIndex(1)

    def date(self):
        value = self.today.selectedDate()
        date_in_string = str(value.toPyDate())
        print(date_in_string)

    def goToPopUpListeEmprunts(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        print("Index PopUpListeEmprunts : ",widget.currentIndex())



class PopUpListeEmpruntsWidget(QWidget, QSqlDatabase):
    def __init__(self):
        super(PopUpListeEmpruntsWidget, self).__init__()
        loadUi('popUpListeEmprunts.ui', self)
        self.boutoncroix.clicked.connect(self.reponseCroix)
        self.boutonconfirmer.clicked.connect(self.reponseConfirmer)
        # self.pageAccueil = PageAccueil()


    def reponseConfirmer(self):

        # self.pageAccueil.show()
        # self.close()
        widget.setCurrentIndex(1)

    def reponseCroix(self):
        widget.setCurrentIndex(widget.currentIndex()-1)




    # def validate(self):
    #     pass

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
    print("Index Accueil : ",widget.indexOf(page_accueil))

    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")
