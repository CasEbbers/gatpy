# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\products-dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(800, 600)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeView = QtGui.QTreeView(Dialog)
        self.treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeView.setRootIsDecorated(False)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.horizontalLayout.addWidget(self.treeView)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.categoryLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.categoryLabel.setObjectName(_fromUtf8("categoryLabel"))
        self.gridLayout_2.addWidget(self.categoryLabel, 5, 0, 1, 1)
        self.nameLineEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.gridLayout_2.addWidget(self.nameLineEdit, 1, 1, 1, 1)
        self.groupLineEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupLineEdit.sizePolicy().hasHeightForWidth())
        self.groupLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupLineEdit.setFont(font)
        self.groupLineEdit.setObjectName(_fromUtf8("groupLineEdit"))
        self.gridLayout_2.addWidget(self.groupLineEdit, 3, 1, 1, 1)
        self.nameLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.gridLayout_2.addWidget(self.nameLabel, 1, 0, 1, 1)
        self.newButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newButton.sizePolicy().hasHeightForWidth())
        self.newButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.newButton.setFont(font)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.gridLayout_2.addWidget(self.newButton, 8, 1, 1, 1)
        self.quitButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout_2.addWidget(self.quitButton, 10, 1, 1, 1)
        self.deleteButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.gridLayout_2.addWidget(self.deleteButton, 8, 0, 1, 1)
        self.saveButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout_2.addWidget(self.saveButton, 6, 0, 1, 2)
        self.priceLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.priceLabel.setFont(font)
        self.priceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.priceLabel.setObjectName(_fromUtf8("priceLabel"))
        self.gridLayout_2.addWidget(self.priceLabel, 2, 0, 1, 1)
        self.priceLineEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceLineEdit.sizePolicy().hasHeightForWidth())
        self.priceLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.priceLineEdit.setFont(font)
        self.priceLineEdit.setObjectName(_fromUtf8("priceLineEdit"))
        self.gridLayout_2.addWidget(self.priceLineEdit, 2, 1, 1, 1)
        self.groupLabel = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupLabel.setFont(font)
        self.groupLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.groupLabel.setObjectName(_fromUtf8("groupLabel"))
        self.gridLayout_2.addWidget(self.groupLabel, 3, 0, 1, 1)
        self.categoryLineEdit = QtGui.QLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryLineEdit.sizePolicy().hasHeightForWidth())
        self.categoryLineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryLineEdit.setFont(font)
        self.categoryLineEdit.setObjectName(_fromUtf8("categoryLineEdit"))
        self.gridLayout_2.addWidget(self.categoryLineEdit, 5, 1, 1, 1)
        self.exportButton = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportButton.sizePolicy().hasHeightForWidth())
        self.exportButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exportButton.setFont(font)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.gridLayout_2.addWidget(self.exportButton, 10, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Producten", None))
        self.categoryLabel.setText(_translate("Dialog", "Categorie", None))
        self.nameLabel.setText(_translate("Dialog", "Naam", None))
        self.newButton.setText(_translate("Dialog", "Opslaan als nieuw", None))
        self.quitButton.setText(_translate("Dialog", "Sluiten", None))
        self.deleteButton.setText(_translate("Dialog", "Verwijderen", None))
        self.saveButton.setText(_translate("Dialog", "Opslaan", None))
        self.priceLabel.setText(_translate("Dialog", "Prijs", None))
        self.groupLabel.setText(_translate("Dialog", "Kostenplaats", None))
        self.exportButton.setText(_translate("Dialog", "Exporteer DB", None))
