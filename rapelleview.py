# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rapp.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(485, 478)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 251, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 91, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 121, 31))
        self.label_5.setObjectName("label_5")
        self.aj = QtWidgets.QPushButton(Dialog)
        self.aj.setGeometry(QtCore.QRect(100, 330, 75, 23))
        self.aj.setObjectName("aj")
        self.t = QtWidgets.QLineEdit(Dialog)
        self.t.setGeometry(QtCore.QRect(192, 80, 151, 20))
        self.t.setObjectName("t")
        self.ty = QtWidgets.QComboBox(Dialog)
        self.ty.setGeometry(QtCore.QRect(200, 122, 151, 20))
        self.ty.setObjectName("ty")
        self.ty.addItem("")
        self.ty.addItem("")
        self.ty.addItem("")
        self.ty.addItem("")
        self.ty.addItem("")
        self.ty.addItem("")
        self.d = QtWidgets.QPlainTextEdit(Dialog)
        self.d.setGeometry(QtCore.QRect(210, 180, 151, 51))
        self.d.setObjectName("d")
        self.dh = QtWidgets.QDateTimeEdit(Dialog)
        self.dh.setGeometry(QtCore.QRect(213, 260, 161, 22))
        self.dh.setObjectName("dh")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#00007f;\">Gestion des rapelles</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Titre:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">type</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">description</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Date et heure</span></p></body></html>"))
        self.aj.setText(_translate("Dialog", "Ajouter"))
        self.ty.setItemText(0, _translate("Dialog", "Sortie"))
        self.ty.setItemText(1, _translate("Dialog", "Loisir"))
        self.ty.setItemText(2, _translate("Dialog", "Santé"))
        self.ty.setItemText(3, _translate("Dialog", "Travaille"))
        self.ty.setItemText(4, _translate("Dialog", "Education"))
        self.ty.setItemText(5, _translate("Dialog", "Autres"))
