# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jhelison\Documents\full python Projects\Impressão de etiquetas\src\ui\DatabaseConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 450)
        Dialog.setMinimumSize(QtCore.QSize(450, 450))
        Dialog.setMaximumSize(QtCore.QSize(450, 450))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalGroupBox = QtWidgets.QGroupBox(Dialog)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leDBFile = QtWidgets.QLineEdit(self.horizontalGroupBox)
        self.leDBFile.setObjectName("leDBFile")
        self.horizontalLayout.addWidget(self.leDBFile)
        self.pbEncontrar = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.pbEncontrar.setObjectName("pbEncontrar")
        self.horizontalLayout.addWidget(self.pbEncontrar)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox)
        self.horizontalGroupBox_3 = QtWidgets.QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox_3.setObjectName("horizontalGroupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leLogin = QtWidgets.QLineEdit(self.horizontalGroupBox_3)
        self.leLogin.setText("")
        self.leLogin.setObjectName("leLogin")
        self.horizontalLayout_3.addWidget(self.leLogin)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox_3)
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self.verticalGroupBox)
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lePassword = QtWidgets.QLineEdit(self.horizontalGroupBox_2)
        self.lePassword.setText("")
        self.lePassword.setObjectName("lePassword")
        self.horizontalLayout_2.addWidget(self.lePassword)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox_2)
        self.verticalLayout.addWidget(self.verticalGroupBox)
        self.horizontalGroupBox1 = QtWidgets.QGroupBox(Dialog)
        self.horizontalGroupBox1.setObjectName("horizontalGroupBox1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalGroupBox1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.leOutuput = QtWidgets.QLineEdit(self.horizontalGroupBox1)
        self.leOutuput.setObjectName("leOutuput")
        self.horizontalLayout_4.addWidget(self.leOutuput)
        self.pdFindOutput = QtWidgets.QPushButton(self.horizontalGroupBox1)
        self.pdFindOutput.setObjectName("pdFindOutput")
        self.horizontalLayout_4.addWidget(self.pdFindOutput)
        self.verticalLayout.addWidget(self.horizontalGroupBox1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pbCancel = QtWidgets.QPushButton(Dialog)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_5.addWidget(self.pbCancel)
        self.pbApply = QtWidgets.QPushButton(Dialog)
        self.pbApply.setObjectName("pbApply")
        self.horizontalLayout_5.addWidget(self.pbApply)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Banco de dados"))
        self.verticalGroupBox.setTitle(_translate("Dialog", "Banco de dados Firebird"))
        self.horizontalGroupBox.setTitle(_translate("Dialog", "Local do banco de dados"))
        self.pbEncontrar.setText(_translate("Dialog", "Encontrar"))
        self.horizontalGroupBox_3.setTitle(_translate("Dialog", "Login"))
        self.horizontalGroupBox_2.setTitle(_translate("Dialog", "Senha"))
        self.horizontalGroupBox1.setTitle(_translate("Dialog", "Pasta de Saída dos arquivos"))
        self.pdFindOutput.setText(_translate("Dialog", "Encontrar"))
        self.pbCancel.setText(_translate("Dialog", "Cancelar"))
        self.pbApply.setText(_translate("Dialog", "Aplicar"))
