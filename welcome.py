import sys
import mysql.connector

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from rapelleview import * # importation de code de l'interface
class welcome(QDialog): #(QDialog) permet l'héritage de QDialog
    def __init__(self):
        super().__init__() # applé le constructeur de l'interface
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.aj.clicked.connect(self.ajout)
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = welcome()

    w.show()

    sys.exit(app.exec_())
