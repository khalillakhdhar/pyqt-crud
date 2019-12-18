import sys
import mysql.connector

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from users import *

class User(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)
        self.lister()
        self.ui.ajout.clicked.connect(self.add)
        self.show()
    def add(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="formation"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO `candidat`( `nom`, `prenom`, `tel`, `niveau`) VALUES (%s, %s,%s,%s)"
        val = (self.ui.n.text(),self.ui.p.text(),self.ui.t.text(),str(self.ui.nv.currentText))
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    def lister(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="formation"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM candidat")
        myresult = mycursor.fetchall()
       
        self.ui.liste.setRowCount(len(myresult)) ##set number of rows
        
        self.ui.liste.setColumnCount(4)
        i=0 ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns
        for x in myresult:
            print(x[0])
            self.ui.liste.setItem(i,0, QTableWidgetItem(x[0]))
            self.ui.liste.setItem(i,1, QTableWidgetItem(x[1]))
            self.ui.liste.setItem(i,2, QTableWidgetItem(x[2]))
            self.ui.liste.setItem(i,3, QTableWidgetItem(x[3]))
            i+=1

        
      

    
        

            
        
if __name__=="__main__":   

    app = QApplication(sys.argv)

    w = User()

    w.show()

    sys.exit(app.exec_())
    
