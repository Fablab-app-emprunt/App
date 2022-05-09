import sys
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets, QtSql
from PyQt5.uic import loadUi

from PyQt5.uic import *



from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QWidget, QMessageBox, QTableWidgetItem

from PyQt5.QtSql import QSql, QSqlQuery, QSqlDatabase
import mysql.connector


state = ''
requete_Outils = ''
Data = []
Lelec = []

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
        print("Index rendreoutils : ",widget.currentIndex())
    def goToEmprunterOutils(self):
        widget.setCurrentIndex(1)
        global state
        state = 'Emprunter'
        print("Index emprunteroutils : ",widget.currentIndex())



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
        global requete_Outils
        requete_Outils = 'ELEC'
        page_choix_outils = EmpruntAjout()
        widget.addWidget(page_choix_outils)
        widget.setCurrentIndex(2)
        print("Index elec : ",widget.currentIndex())

    def bois(self):
        global requete_Outils
        requete_Outils = 'BOIS'
        page_choix_outils = EmpruntAjout()
        widget.addWidget(page_choix_outils)
        widget.setCurrentIndex(3)
        print("Index bois : ",widget.currentIndex())

    def usinage(self):
        global requete_Outils
        requete_Outils = 'USINAGE'
        page_choix_outils = EmpruntAjout()
        widget.addWidget(page_choix_outils)
        widget.setCurrentIndex(4)
        print("Index usinage : ",widget.currentIndex())

    def validate(self):
        global Lelec
        print(Lelec)

class EmpruntAjout(QWidget, QSqlDatabase):
    def __init__(self):

        super(EmpruntAjout, self).__init__()
        loadUi('empruntAjout.ui',self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.today.clicked.connect(self.date)
        self.rendreOutils_4.clicked.connect(self.recupdata)
        self.dateemprunt.clicked.connect(self.date)


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

        count_tools = "select * from Outils where departOutils_Outils = '"+requete_Outils+"'"
        cursor = connection.cursor()
        cursor.execute(count_tools)
        Data = cursor.fetchall()

        self.boutonvalider.clicked.connect(self.goToPopUpListeEmprunts)

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
        for row in range(self.table_Emprunt.rowCount()-1):
            L=[]
            if self.table_Emprunt.item(row,3).checkState() == QtCore.Qt.CheckState.Checked:
                for col in range(self.table_Emprunt.columnCount()-1):
                    L.append(self.table_Emprunt.item(row,0).text())
                if requete_Outils == 'ELEC':
                    Lelec.append(L[0])
        print(Lelec)

    def accueil(self):
       widget.setCurrentIndex(0)

    def date(self):
        value = self.today.selectedDate()
        date_in_string = str(value.toPyDate())
        print(date_in_string)





    def goToPopUpListeEmprunts(self):
        widget.setCurrentIndex(5)
        global state
        state = 'PopUpListeEmprunts'
        popUpListeEmprunt = PopUpListeEmpruntsWidget()
        widget.addWidget(popUpListeEmprunt)
        print("Index PopUpListeEmprunts : ",widget.currentIndex())









class PopUpListeEmpruntsWidget(QWidget, QSqlDatabase):
    def __init__(self):
        super(PopUpListeEmpruntsWidget, self).__init__()
        loadUi('popUpListeEmprunts.ui', self)
        self.boutoncroix.clicked.connect(self.reponseCroix)
        self.boutonconfirmer.clicked.connect(self.reponseConfirmer)
        self.pageAccueil = PageAccueil()


    def reponseConfirmer(self):

        self.pageAccueil.show()
        self.close()

    def reponseCroix(self):
        self.close()




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
    print("Index Accueil : ",widget.currentIndex())
    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")

.