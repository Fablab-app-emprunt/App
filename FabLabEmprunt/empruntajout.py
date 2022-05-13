from PyQt5.QtWidgets import QWidget
from PyQt5.QtSql import QSqlDatabase
# from FabLabEmprunt.pageAccueil import PageAccueil

class EmpruntAjout(QWidget, QSqlDatabase):
    def __init__(self):
        from PyQt5.uic import loadUi
        from PyQt5 import QtGui, QtCore, QtWidgets
        from PyQt5.QtWidgets import QTableWidgetItem, QComboBox
        import mysql.connector
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


        count_tools = "select * from Outils where departOutils_Outils = '"+requete_Outils+"'"

        cursor = connection.cursor()
        cursor.execute(count_tools)
        Data = cursor.fetchall()

        #-------------REMPLIR LES TABLEAUX---------------------
        for item in Data:
            cell = QTableWidgetItem(str(item[0]))
            self.table_Emprunt.setItem(row, col, cell)

            cell = QTableWidgetItem(str(item[1]))
            self.table_Emprunt.setItem(row, col+1, cell)
            #-----------3EME COLONNE : FAIRE UNE LISTE DEROULANTE POUR CHOISIR LA QUANTITE DE CHAQUUE OUTIL A EMPRUNTER---------------
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
        from PyQt5 import QtCore
        from main import requete_Outils,Lelec,Lbois,Lusinage

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
        from main import widget
        widget.setCurrentIndex(0)

    def returntypeoutils(self):
        from main import widget
        widget.setCurrentIndex(1)

    def date(self):
        value = self.dateemprunt.selectedDate()
        date_in_string = str(value.toPyDate())
        print(date_in_string)

    def goToChoixTypeOutils(self):
        from main import widget
        widget.setCurrentIndex(1)