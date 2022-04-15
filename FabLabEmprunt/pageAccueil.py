from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox
from PyQt5.uic import loadUi
from FabLabEmprunt.empruntTypeOutils import EmpruntTypeOutils

class PageAccueil(QWidget):
    def __init__(self):
        super(PageAccueil,self).__init__()
        loadUi('pageAccueil.ui',self)
        self.rendreoutils.clicked.connect(self.rendreOutils)
        self.emprunteroutils.clicked.connect(self.emprunterOutils)
        self.type_outils = EmpruntTypeOutils()

    def rendreOutils(self):
        print("rendre outils")
        self.type_outils.show()
        self.close()


    def emprunterOutils(self):
        print("emprunter outils")
        self.type_outils.show()
        self.close()




if __name__ == "__main__":
    app = QApplication([])
    monIHM = PageAccueil()
    monIHM.show()
    app.exec_()