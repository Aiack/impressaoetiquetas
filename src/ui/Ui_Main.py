# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jhelison\Documents\full python Projects\Impressão de etiquetas\src\ui\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vlInputTW = QtWidgets.QVBoxLayout()
        self.vlInputTW.setObjectName("vlInputTW")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.horizontalGroupBox)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.vlInputTW.addWidget(self.tableWidget_2)
        self.horizontalLayout.addLayout(self.vlInputTW)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pbAdd = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.pbAdd.setObjectName("pbAdd")
        self.verticalLayout_3.addWidget(self.pbAdd)
        self.pbRemove = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.pbRemove.setObjectName("pbRemove")
        self.verticalLayout_3.addWidget(self.pbRemove)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.twOutputItens = QtWidgets.QTableWidget(self.horizontalGroupBox)
        self.twOutputItens.setObjectName("twOutputItens")
        self.twOutputItens.setColumnCount(0)
        self.twOutputItens.setRowCount(0)
        self.verticalLayout_2.addWidget(self.twOutputItens)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        self.verticalGroupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalGroupBox_4.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_4.setSizePolicy(sizePolicy)
        self.verticalGroupBox_4.setObjectName("verticalGroupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalGroupBox_4)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.verticalGroupBox_4)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.sbHorizontalPos = QtWidgets.QSpinBox(self.verticalGroupBox_4)
        self.sbHorizontalPos.setMinimum(1)
        self.sbHorizontalPos.setMaximum(3)
        self.sbHorizontalPos.setObjectName("sbHorizontalPos")
        self.horizontalLayout_2.addWidget(self.sbHorizontalPos)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.sbVerticalPos = QtWidgets.QSpinBox(self.verticalGroupBox_4)
        self.sbVerticalPos.setMinimum(1)
        self.sbVerticalPos.setMaximum(6)
        self.sbVerticalPos.setObjectName("sbVerticalPos")
        self.horizontalLayout_5.addWidget(self.sbVerticalPos)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.verticalGroupBox_4)
        self.tableWidget_3.setMinimumSize(QtCore.QSize(147, 210))
        self.tableWidget_3.setMaximumSize(QtCore.QSize(147, 210))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tableWidget_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.verticalGroupBox_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.pbOpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pbOpenFolder.setObjectName("pbOpenFolder")
        self.horizontalLayout_6.addWidget(self.pbOpenFolder)
        self.pbGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.pbGenerate.setObjectName("pbGenerate")
        self.horizontalLayout_6.addWidget(self.pbGenerate)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 20))
        self.menubar.setObjectName("menubar")
        self.menuConfigura_es = QtWidgets.QMenu(self.menubar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionBanco_de_dados = QtWidgets.QAction(MainWindow)
        self.actionBanco_de_dados.setObjectName("actionBanco_de_dados")
        self.actionFolha = QtWidgets.QAction(MainWindow)
        self.actionFolha.setObjectName("actionFolha")
        self.actionEtiqueta = QtWidgets.QAction(MainWindow)
        self.actionEtiqueta.setObjectName("actionEtiqueta")
        self.menuConfigura_es.addAction(self.actionBanco_de_dados)
        self.menuConfigura_es.addAction(self.actionFolha)
        self.menuConfigura_es.addAction(self.actionEtiqueta)
        self.menuSobre.addAction(self.actionSobre)
        self.menubar.addAction(self.menuConfigura_es.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.horizontalGroupBox.setTitle(_translate("MainWindow", "Itens à gerar etiqueta"))
        self.pbAdd.setText(_translate("MainWindow", "Adicionar >>"))
        self.pbRemove.setText(_translate("MainWindow", "<< Remover"))
        self.verticalGroupBox_4.setTitle(_translate("MainWindow", "Posição inicial da etiqueta"))
        self.label.setText(_translate("MainWindow", "Posição Inicial Horizontal"))
        self.label_2.setText(_translate("MainWindow", "Posição Inicial Vertical"))
        self.pbOpenFolder.setText(_translate("MainWindow", "Abrir Pasta"))
        self.pbGenerate.setText(_translate("MainWindow", "Gerar"))
        self.menuConfigura_es.setTitle(_translate("MainWindow", "Configurações"))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.actionBanco_de_dados.setText(_translate("MainWindow", "Banco de dados"))
        self.actionFolha.setText(_translate("MainWindow", "Folha"))
        self.actionEtiqueta.setText(_translate("MainWindow", "Etiqueta"))
