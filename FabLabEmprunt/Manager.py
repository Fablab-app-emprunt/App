from PyQt5.QtWidgets import *

from FabLabEmprunt.empruntTypeOutils import *
from FabLabEmprunt.empruntajout import *
from FabLabEmprunt.pageAccueil import *


class Manager():
    def __init__(self):
        # self.third = EmpruntAjout()
        self.second = EmpruntTypeOutils() #self.third
        self.first = PageAccueil(self.second) #, self.third
        self.second.signal.connect(self.choixAction)

        self.first.show()        #Lancement de la page principale

    def choixAction(self, choix): #Lancemement de la page empruntTypeOutils
        self.first.show()


    # def ajout(self): #Lancemement de la page empruntajout
    #     pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())