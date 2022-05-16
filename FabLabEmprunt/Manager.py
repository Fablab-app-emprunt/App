# import os
# os.system('pip install -r requirements.txt')
import sys
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QComboBox, QMessageBox
from PyQt5.QtSql import QSqlDatabase
import mysql.connector


requete_Outils = ''
Requete_Outils = ['ELEC','BOIS','USINAGE']
page_choix_outils = ['page_choix_outils_elec','page_choix_outils_bois','page_choix_outils_usinage']
Data = []
Lelec = []
Lbois = []
Lusinage = []
Lfinal=[]

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
        if mail != '' and mdp != '':
            widget.setCurrentWidget(page_accueil)
            self.line_mail.setText('')
            self.line_mdp.setText('')
        else :
            error = QMessageBox()
            error.setText("Veuillez renseigner les champs")
            error.exec()


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
        mail = self.line_mail.text()
        mdp = self.line_mdp.text()
        if mail != '' and mdp != '':
            sucess = QMessageBox()
            sucess.setText("Inscription réussie !")
            sucess.exec()
            self.line_mail.setText('')
            self.line_mdp.setText('')
        else :
            error = QMessageBox()
            error.setText("Veuillez renseigner les champs")
            error.exec()

    def goToConnexion(self):
        widget.setCurrentWidget(espace_connection)

class PageAccueil(QWidget):
    def __init__(self):
        super(PageAccueil,self).__init__()
        loadUi('pageAccueil.ui',self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.boutonaccueil.clicked.connect(self.accueil)
        self.rendreoutils.clicked.connect(self.goToRendreOutils)
        self.emprunteroutils.clicked.connect(self.goToEmprunterOutils)

    def goToRendreOutils(self):
        print("Index rendreoutils : ",widget.indexOf(page_choix_type_outils))
        page_rendre_outils = RendreOutils()
        widget.insertWidget(2,page_rendre_outils)
        widget.setCurrentWidget(page_rendre_outils)

    def goToEmprunterOutils(self):
        widget.setCurrentWidget(page_choix_type_outils)
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
            widget.addWidget(page_choix_outils[i])
            print("Index of : ", requete_Outils,' is ', widget.indexOf(page_choix_outils[i]))

    def accueil(self):
        widget.setCurrentWidget(espace_connection)
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
        widget.setCurrentWidget(espace_connection)

    def elec(self):
        widget.setCurrentWidget(page_choix_outils[0])
        global requete_Outils
        requete_Outils = 'ELEC'

    def bois(self):
        widget.setCurrentWidget(page_choix_outils[1])
        global requete_Outils
        requete_Outils = 'BOIS'

    def usinage(self):
        widget.setCurrentWidget(page_choix_outils[2])
        global requete_Outils
        requete_Outils = 'USINAGE'

    def validate(self):
        global Lelec
        global Lbois
        global Lusinage
        global Lfinal
        Lfinal = []
        for i in range(len(Lelec)):
            Lfinal.append(Lelec[i])
        for i in range(len(Lbois)):
            Lfinal.append(Lbois[i])
        for i in range(len(Lusinage)):
            Lfinal.append(Lusinage[i])
        print("Lfinal",Lfinal)
        pop_up = PopUpListeEmpruntsWidget()
        widget.insertWidget(5,pop_up)
        print("Index of : pop up is ", widget.indexOf(pop_up))
        widget.setCurrentIndex(5)

class EmpruntAjout(QWidget, QSqlDatabase):
    def __init__(self):

        super(EmpruntAjout, self).__init__()
        loadUi('empruntAjout.ui',self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.boutonvalider.clicked.connect(self.recupdata)
        self.dateemprunt.clicked.connect(self.date)
        self.boutonvalider.clicked.connect(self.goToChoixTypeOutils)
        self.return_bouton.clicked.connect(self.returntypeoutils)

        global requete_Outils
        global Data
        self.table_Emprunt.setColumnCount(4)
        self.table_Emprunt.rowCount()
        self.table_Emprunt.setHorizontalHeaderLabels(['id',"Nom de l'outils",'Quantité','Emprunter'])
        row = self.table_Emprunt.rowCount()
        self.table_Emprunt.setRowCount(row+1)
        col = 0
        connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                             host='145.14.151.101',
                                             database='u556968436_fablab')


        count_tools = "select * from Outils where departOutils_Outils = '"+requete_Outils+"' and `quantiteEmprunte_Outils`!= quantiteOutils_Outils"

        cursor = connection.cursor()
        cursor.execute(count_tools)
        Data = cursor.fetchall()

#-------------REMPLIR LES TABLEAUX---------------------
        for item in Data:
            cell = QTableWidgetItem(str(item[0]))
            self.table_Emprunt.setItem(row, col, cell)

            cell = QTableWidgetItem(str(item[1]))
            self.table_Emprunt.setItem(row, col+1, cell)
#-----------3EME COLONNE : FAIRE UNE LISTE DEROULANTE POUR CHOISIR LA QUANTITE DE CHAQUE OUTIL A EMPRUNTER---------------
            L = []
            for i in range(item[3] - item[5] + 1):
                L.append(str(i))
                i+=1
            combo = QComboBox()
            for i in L:
                combo.addItem(i)
            self.table_Emprunt.setCellWidget(row, col+2, combo)

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
        connection.close()

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
                    L.append(self.table_Emprunt.item(row,1).text())
                    # L.append(self.table_Emprunt.item(row,2).currentText())
                    print("quantite",int(self.table_Emprunt.cellWidget(row,2).currentText()))
                    print(L)
                if requete_Outils == 'ELEC':
                    Lelec.append(L[0])
                    Lelec.append(int(self.table_Emprunt.cellWidget(row,2).currentText()))
                elif requete_Outils == 'BOIS':
                    Lbois.append(L[0])
                    Lbois.append(int(self.table_Emprunt.cellWidget(row,2).currentText()))
                elif requete_Outils == 'USINAGE':
                    Lusinage.append(L[0])
                    Lusinage.append(int(self.table_Emprunt.cellWidget(row,2).currentText()))
        print('Lelec',Lelec)
        print('Lbois',Lbois)
        print('Lusinage',Lusinage)

    def accueil(self):
       widget.setCurrentWidget(espace_connection)

    def returntypeoutils(self):
        widget.setCurrentWidget(page_choix_type_outils)

    def date(self):
        value = self.dateemprunt.selectedDate()
        date_in_string = str(value.toPyDate())
        print(date_in_string)

    def goToChoixTypeOutils(self):
        widget.setCurrentWidget(page_choix_type_outils)

class RendreOutils(QWidget, QSqlDatabase):
    def __init__(self):
        super(RendreOutils, self).__init__()
        loadUi('rendreOutils.ui', self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.return_bouton.clicked.connect(self.accueil)
        self.boutonvalider.clicked.connect(self.rendre)
        self.return_bouton_2.clicked.connect(self.Selectall)
        self.table_Emprunt.setColumnCount(4)
        self.table_Emprunt.rowCount()
        self.table_Emprunt.setHorizontalHeaderLabels(['id',"Nom de l'outils",'Quantité','Rendre'])

        row = self.table_Emprunt.rowCount()
        self.table_Emprunt.setRowCount(row+1)
        col = 0
        connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                             host='145.14.151.101',
                                             database='u556968436_fablab')

        count_tools = "select * from Outils where quantiteEmprunte_Outils != 0"
        cursor = connection.cursor()
        cursor.execute(count_tools)
        Data = cursor.fetchall()

        #-------------REMPLIR LES TABLEAUX---------------------
        for item in Data:
            cell = QTableWidgetItem(str(item[0]))
            self.table_Emprunt.setItem(row, col, cell)

            cell = QTableWidgetItem(str(item[1]))
            self.table_Emprunt.setItem(row, col+1, cell)
            #-----------3EME COLONNE : FAIRE UNE LISTE DEROULANTE POUR CHOISIR LA QUANTITE DE CHAQUUE OUTIL A RENDRE---------------
            L = []
            for i in range(item[5] + 1):
                L.append(str(i))
                i+=1
            self.combo = QComboBox()
            for i in L:
                self.combo.addItem(i)
            self.table_Emprunt.setCellWidget(row, col+2, self.combo)

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

    def accueil(self):
        widget.setCurrentWidget(espace_connection)

    def rendre(self):
        Lrendre=[]
        for row in range(self.table_Emprunt.rowCount()-1):
            L=[]
            if self.table_Emprunt.item(row,3).checkState() == QtCore.Qt.CheckState.Checked:
                for col in range(self.table_Emprunt.columnCount()-3):
                    L.append(self.table_Emprunt.item(row,1).text())
                    L.append(self.table_Emprunt.cellWidget(row,2).currentText())
                    Lrendre.append(L[0])
                    Lrendre.append(L[1])
        print(Lrendre)
        for i in range(0,len(Lrendre),2):
            connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                                 host='145.14.151.101',
                                                 database='u556968436_fablab')
            req = "UPDATE `Outils` SET `quantiteEmprunte_Outils`=`quantiteEmprunte_Outils` - %s WHERE `nomOutils_Outils`= %s "
            tuple=(Lrendre[i+1], Lrendre[i])
            cursor = connection.cursor()
            cursor.execute(req,tuple)
            connection.commit()
            connection.close()
        widget.setCurrentWidget(page_accueil)

    def Selectall(self):
        for row in range(self.table_Emprunt.rowCount()-1):
            self.table_Emprunt.item(row,3).setCheckState(QtCore.Qt.Checked)
            self.table_Emprunt.cellWidget(row,2).setCurrentIndex(self.table_Emprunt.cellWidget(row,2).count()-1)

class PopUpListeEmpruntsWidget(QWidget, QSqlDatabase):
    def __init__(self):
        global Lfinal
        super(PopUpListeEmpruntsWidget, self).__init__()
        loadUi('popUpListeEmprunts.ui', self)
        self.boutoncroix.clicked.connect(self.reponseCroix)
        self.boutonconfirmer.clicked.connect(self.reponseConfirmer)
        self.table_Recap.setColumnCount(2)
        self.table_Recap.rowCount()
        self.table_Recap.setHorizontalHeaderLabels(["Nom de l'outils",'Quantité'])
        row = self.table_Recap.rowCount()
        self.table_Recap.setRowCount(len(Lfinal))
        col = 0
        header = self.table_Recap.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

#------------------------------------REMPLIR LES TABLEAUX------------------------------------------------------------
        for item in range(0,len(Lfinal),2):
            print("row",row)
            print("item", item)
            cell = QTableWidgetItem(str(Lfinal[item]))
            self.table_Recap.setItem(row, col, cell)
            cell = QTableWidgetItem(str(Lfinal[item+1]))
            self.table_Recap.setItem(row, col+1, cell)
            row+=1


    def reponseConfirmer(self):
        global Lfinal
        print("longueur liste",len(Lfinal))
        for i in range(0,len(Lfinal),2):
            connection = mysql.connector.connect(user='u556968436_LaTeamDeLoick', password='LoickRaison2022',
                                                 host='145.14.151.101',
                                                 database='u556968436_fablab')
            print("quantite :",Lfinal[i],"nom outil :",Lfinal[i-1])
            req = "UPDATE `Outils` SET `quantiteEmprunte_Outils`=`quantiteEmprunte_Outils` + %s WHERE `nomOutils_Outils`= %s "
            tuple=(Lfinal[i+1], Lfinal[i])
            cursor = connection.cursor()
            cursor.execute(req,tuple)
            connection.commit()
            connection.close()
        widget.setCurrentWidget(page_accueil)

    def reponseCroix(self):
        widget.setCurrentWidget(page_choix_type_outils)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    espace_connection = Connection()
    espace_inscription = Inscription()
    page_accueil = PageAccueil()
    page_choix_type_outils = EmpruntTypeOutils()

    widget.addWidget(espace_connection)
    widget.addWidget(espace_inscription)
    widget.addWidget(page_accueil)
    widget.addWidget(page_choix_type_outils)


    widget.setFixedHeight(700)
    widget.setFixedWidth(1000)
    widget.show()
    print("Index Accueil : ",widget.indexOf(page_accueil))

    try:
        sys.exit(app.exec_())
    except :
        print("Exiting")
