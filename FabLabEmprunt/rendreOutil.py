from PyQt5.QtWidgets import QWidget
from PyQt5.QtSql import QSqlDatabase

class RendreOutils(QWidget, QSqlDatabase):
    def __init__(self):
        from PyQt5.uic import loadUi
        from PyQt5.QtWidgets import QTableWidgetItem, QComboBox
        from PyQt5 import QtGui, QtCore, QtWidgets
        import mysql.connector
        super(RendreOutils, self).__init__()
        loadUi('rendreOutils.ui', self)
        self.boutonaccueil.clicked.connect(self.accueil)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('Capture d’écran 2022-04-14 153417.png'))
        self.boutonaccueil.setIcon(icon)
        self.return_bouton.clicked.connect(self.accueil)
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
        from main import widget
        widget.setCurrentIndex(0)
