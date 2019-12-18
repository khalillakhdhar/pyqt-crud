# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userfinale.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(902, 473)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("")
        self.ajout = QtWidgets.QPushButton(Dialog)
        self.ajout.setGeometry(QtCore.QRect(110, 270, 111, 41))
        self.ajout.setStyleSheet("color:rgb(44, 75, 255);\n"
"height:30px;\n"
"font: 75 14pt \"Times New Roman\";\n"
"background-color:rgb(255, 255, 255);")
        self.ajout.setObjectName("ajout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 351, 41))
        self.label_2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"color:rgb(170, 84, 147);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 111, 41))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 111, 41))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 111, 41))
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 170, 111, 41))
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.n = QtWidgets.QLineEdit(Dialog)
        self.n.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.n.setStyleSheet("border-color:#000;\n"
"border-size:4px")
        self.n.setObjectName("n")
        self.p = QtWidgets.QLineEdit(Dialog)
        self.p.setGeometry(QtCore.QRect(130, 110, 113, 20))
        self.p.setStyleSheet("\n"
"border-color:#000;\n"
"border-size:4px")
        self.p.setObjectName("p")
        self.t = QtWidgets.QLineEdit(Dialog)
        self.t.setGeometry(QtCore.QRect(130, 150, 113, 20))
        self.t.setStyleSheet("border-color:#000;\n"
"border-size:4px")
        self.t.setObjectName("t")
        self.nv = QtWidgets.QComboBox(Dialog)
        self.nv.setGeometry(QtCore.QRect(130, 180, 111, 21))
        self.nv.setObjectName("nv")
        self.nv.addItem("")
        self.nv.addItem("")
        self.nv.addItem("")
        self.formation = QtWidgets.QCommandLinkButton(Dialog)
        self.formation.setGeometry(QtCore.QRect(300, 120, 251, 41))
        self.formation.setObjectName("formation")
        self.liste = QtWidgets.QTableWidget(Dialog)
        self.liste.setGeometry(QtCore.QRect(300, 200, 601, 201))
        self.liste.setStyleSheet("font-color:black")
        self.liste.setObjectName("liste")
        self.liste.setColumnCount(5)
        self.liste.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.liste.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.liste.setHorizontalHeaderItem(4, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ajout.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; color:#0000ff;\">Ceci sauvegarde un candidat dans votre base</span></p></body></html>"))
        self.ajout.setText(_translate("Dialog", "Ajouter"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Gestion des candidats</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nom</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Prenom:</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Téléphone:</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">niveau:</span></p></body></html>"))
        self.nv.setItemText(0, _translate("Dialog", "Lycee"))
        self.nv.setItemText(1, _translate("Dialog", "Université"))
        self.nv.setItemText(2, _translate("Dialog", "enfant"))
        self.formation.setText(_translate("Dialog", "Ajouter une formation"))
        item = self.liste.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Id"))
        item = self.liste.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "nom"))
        item.setWhatsThis(_translate("Dialog", "identifiant auto"))
        item = self.liste.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "prenom"))
        item = self.liste.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "telephone"))
        item = self.liste.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "niveau"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
