# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\gui.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(862, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("*{\n"
"    color: #f8f8f2;\n"
"    background: #272822;\n"
"}\n"
"QPushButton{\n"
"    background: #141411;\n"
"}\n"
"QLineEdit{\n"
"    background: #383830;\n"
"    border: 1px solid #595959;\n"
"}\n"
"QListView{\n"
"    background: #383830;\n"
"}\n"
"QListView::item:selected {\n"
"    background: #141411;\n"
"}\n"
"QListView::item:selected:!active {\n"
"    color: white;\n"
"}\n"
"QMenuBar{\n"
"    background: #383830;\n"
"}\n"
"QMenuBar::item{\n"
"    background-color: transparent;\n"
"}\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leftVL = QtGui.QVBoxLayout()
        self.leftVL.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.leftVL.setObjectName(_fromUtf8("leftVL"))
        self.listHL = QtGui.QHBoxLayout()
        self.listHL.setSpacing(0)
        self.listHL.setObjectName(_fromUtf8("listHL"))
        self.amountList = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.amountList.setFont(font)
        self.amountList.setFrameShape(QtGui.QFrame.NoFrame)
        self.amountList.setObjectName(_fromUtf8("amountList"))
        self.listHL.addWidget(self.amountList)
        self.productList = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.productList.setFont(font)
        self.productList.setFrameShape(QtGui.QFrame.NoFrame)
        self.productList.setObjectName(_fromUtf8("productList"))
        self.listHL.addWidget(self.productList)
        self.priceList = QtGui.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.priceList.setFont(font)
        self.priceList.setFrameShape(QtGui.QFrame.NoFrame)
        self.priceList.setTextElideMode(QtCore.Qt.ElideLeft)
        self.priceList.setObjectName(_fromUtf8("priceList"))
        self.listHL.addWidget(self.priceList)
        self.listHL.setStretch(0, 1)
        self.listHL.setStretch(1, 3)
        self.listHL.setStretch(2, 2)
        self.leftVL.addLayout(self.listHL)
        self.totalHL = QtGui.QHBoxLayout()
        self.totalHL.setSpacing(0)
        self.totalHL.setObjectName(_fromUtf8("totalHL"))
        self.totalAmountLineEdit = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.totalAmountLineEdit.setFont(font)
        self.totalAmountLineEdit.setReadOnly(True)
        self.totalAmountLineEdit.setObjectName(_fromUtf8("totalAmountLineEdit"))
        self.totalHL.addWidget(self.totalAmountLineEdit)
        self.totalLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalLabel.sizePolicy().hasHeightForWidth())
        self.totalLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.totalLabel.setFont(font)
        self.totalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalLabel.setObjectName(_fromUtf8("totalLabel"))
        self.totalHL.addWidget(self.totalLabel)
        self.totalPriceLineEdit = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.totalPriceLineEdit.setFont(font)
        self.totalPriceLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.totalPriceLineEdit.setReadOnly(True)
        self.totalPriceLineEdit.setObjectName(_fromUtf8("totalPriceLineEdit"))
        self.totalHL.addWidget(self.totalPriceLineEdit)
        self.totalHL.setStretch(0, 1)
        self.totalHL.setStretch(1, 1)
        self.totalHL.setStretch(2, 1)
        self.leftVL.addLayout(self.totalHL)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.leftVL.addWidget(self.line_5)
        self.numpadLineEdit = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.numpadLineEdit.setFont(font)
        self.numpadLineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numpadLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numpadLineEdit.setReadOnly(True)
        self.numpadLineEdit.setObjectName(_fromUtf8("numpadLineEdit"))
        self.leftVL.addWidget(self.numpadLineEdit)
        self.npGrid = QtGui.QGridLayout()
        self.npGrid.setVerticalSpacing(12)
        self.npGrid.setObjectName(_fromUtf8("npGrid"))
        self.npBtn4 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn4.sizePolicy().hasHeightForWidth())
        self.npBtn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn4.setFont(font)
        self.npBtn4.setObjectName(_fromUtf8("npBtn4"))
        self.npGrid.addWidget(self.npBtn4, 1, 0, 1, 1)
        self.npBtn3 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn3.sizePolicy().hasHeightForWidth())
        self.npBtn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn3.setFont(font)
        self.npBtn3.setObjectName(_fromUtf8("npBtn3"))
        self.npGrid.addWidget(self.npBtn3, 0, 2, 1, 1)
        self.numpadClearButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numpadClearButton.sizePolicy().hasHeightForWidth())
        self.numpadClearButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.numpadClearButton.setFont(font)
        self.numpadClearButton.setObjectName(_fromUtf8("numpadClearButton"))
        self.npGrid.addWidget(self.numpadClearButton, 3, 0, 1, 1)
        self.numpadBackspaceButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numpadBackspaceButton.sizePolicy().hasHeightForWidth())
        self.numpadBackspaceButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.numpadBackspaceButton.setFont(font)
        self.numpadBackspaceButton.setObjectName(_fromUtf8("numpadBackspaceButton"))
        self.npGrid.addWidget(self.numpadBackspaceButton, 3, 2, 1, 1)
        self.npBtn6 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn6.sizePolicy().hasHeightForWidth())
        self.npBtn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn6.setFont(font)
        self.npBtn6.setObjectName(_fromUtf8("npBtn6"))
        self.npGrid.addWidget(self.npBtn6, 1, 2, 1, 1)
        self.npBtn9 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn9.sizePolicy().hasHeightForWidth())
        self.npBtn9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn9.setFont(font)
        self.npBtn9.setObjectName(_fromUtf8("npBtn9"))
        self.npGrid.addWidget(self.npBtn9, 2, 2, 1, 1)
        self.npBtn1 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn1.sizePolicy().hasHeightForWidth())
        self.npBtn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn1.setFont(font)
        self.npBtn1.setObjectName(_fromUtf8("npBtn1"))
        self.npGrid.addWidget(self.npBtn1, 0, 0, 1, 1)
        self.npBtn0 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn0.sizePolicy().hasHeightForWidth())
        self.npBtn0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn0.setFont(font)
        self.npBtn0.setObjectName(_fromUtf8("npBtn0"))
        self.npGrid.addWidget(self.npBtn0, 3, 1, 1, 1)
        self.npBtn5 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn5.sizePolicy().hasHeightForWidth())
        self.npBtn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn5.setFont(font)
        self.npBtn5.setObjectName(_fromUtf8("npBtn5"))
        self.npGrid.addWidget(self.npBtn5, 1, 1, 1, 1)
        self.npBtn2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn2.sizePolicy().hasHeightForWidth())
        self.npBtn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn2.setFont(font)
        self.npBtn2.setObjectName(_fromUtf8("npBtn2"))
        self.npGrid.addWidget(self.npBtn2, 0, 1, 1, 1)
        self.npBtn7 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn7.sizePolicy().hasHeightForWidth())
        self.npBtn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn7.setFont(font)
        self.npBtn7.setObjectName(_fromUtf8("npBtn7"))
        self.npGrid.addWidget(self.npBtn7, 2, 0, 1, 1)
        self.npBtn8 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.npBtn8.sizePolicy().hasHeightForWidth())
        self.npBtn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.npBtn8.setFont(font)
        self.npBtn8.setObjectName(_fromUtf8("npBtn8"))
        self.npGrid.addWidget(self.npBtn8, 2, 1, 1, 1)
        self.npGrid.setRowStretch(0, 1)
        self.npGrid.setRowStretch(1, 1)
        self.npGrid.setRowStretch(2, 1)
        self.npGrid.setRowStretch(3, 1)
        self.leftVL.addLayout(self.npGrid)
        self.gridLayout.addLayout(self.leftVL, 0, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 0, 1, 1, 1)
        self.rightVL = QtGui.QVBoxLayout()
        self.rightVL.setObjectName(_fromUtf8("rightVL"))
        self.pincashHL = QtGui.QHBoxLayout()
        self.pincashHL.setObjectName(_fromUtf8("pincashHL"))
        self.payCashButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payCashButton.sizePolicy().hasHeightForWidth())
        self.payCashButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.payCashButton.setFont(font)
        self.payCashButton.setObjectName(_fromUtf8("payCashButton"))
        self.pincashHL.addWidget(self.payCashButton)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.pincashHL.addItem(spacerItem)
        self.payPinButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payPinButton.sizePolicy().hasHeightForWidth())
        self.payPinButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.payPinButton.setFont(font)
        self.payPinButton.setObjectName(_fromUtf8("payPinButton"))
        self.pincashHL.addWidget(self.payPinButton)
        self.pincashHL.setStretch(0, 1)
        self.pincashHL.setStretch(1, 1)
        self.pincashHL.setStretch(2, 1)
        self.rightVL.addLayout(self.pincashHL)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.rightVL.addWidget(self.line)
        self.catAndProductHL = QtGui.QHBoxLayout()
        self.catAndProductHL.setObjectName(_fromUtf8("catAndProductHL"))
        self.categoryLayout = QtGui.QVBoxLayout()
        self.categoryLayout.setObjectName(_fromUtf8("categoryLayout"))
        self.catBtn0 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBtn0.sizePolicy().hasHeightForWidth())
        self.catBtn0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.catBtn0.setFont(font)
        self.catBtn0.setText(_fromUtf8(""))
        self.catBtn0.setObjectName(_fromUtf8("catBtn0"))
        self.categoryLayout.addWidget(self.catBtn0)
        self.catBtn1 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBtn1.sizePolicy().hasHeightForWidth())
        self.catBtn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.catBtn1.setFont(font)
        self.catBtn1.setText(_fromUtf8(""))
        self.catBtn1.setObjectName(_fromUtf8("catBtn1"))
        self.categoryLayout.addWidget(self.catBtn1)
        self.catBtn2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBtn2.sizePolicy().hasHeightForWidth())
        self.catBtn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.catBtn2.setFont(font)
        self.catBtn2.setText(_fromUtf8(""))
        self.catBtn2.setObjectName(_fromUtf8("catBtn2"))
        self.categoryLayout.addWidget(self.catBtn2)
        self.catBtn3 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBtn3.sizePolicy().hasHeightForWidth())
        self.catBtn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.catBtn3.setFont(font)
        self.catBtn3.setText(_fromUtf8(""))
        self.catBtn3.setObjectName(_fromUtf8("catBtn3"))
        self.categoryLayout.addWidget(self.catBtn3)
        self.catBtn4 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBtn4.sizePolicy().hasHeightForWidth())
        self.catBtn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.catBtn4.setFont(font)
        self.catBtn4.setText(_fromUtf8(""))
        self.catBtn4.setObjectName(_fromUtf8("catBtn4"))
        self.categoryLayout.addWidget(self.catBtn4)
        self.catBtn5 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBtn5.sizePolicy().hasHeightForWidth())
        self.catBtn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.catBtn5.setFont(font)
        self.catBtn5.setText(_fromUtf8(""))
        self.catBtn5.setObjectName(_fromUtf8("catBtn5"))
        self.categoryLayout.addWidget(self.catBtn5)
        self.catBtn6 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBtn6.sizePolicy().hasHeightForWidth())
        self.catBtn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.catBtn6.setFont(font)
        self.catBtn6.setText(_fromUtf8(""))
        self.catBtn6.setObjectName(_fromUtf8("catBtn6"))
        self.categoryLayout.addWidget(self.catBtn6)
        self.catBtn7 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBtn7.sizePolicy().hasHeightForWidth())
        self.catBtn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.catBtn7.setFont(font)
        self.catBtn7.setText(_fromUtf8(""))
        self.catBtn7.setObjectName(_fromUtf8("catBtn7"))
        self.categoryLayout.addWidget(self.catBtn7)
        self.prevNextHL = QtGui.QHBoxLayout()
        self.prevNextHL.setObjectName(_fromUtf8("prevNextHL"))
        self.prevBtn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevBtn.sizePolicy().hasHeightForWidth())
        self.prevBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prevBtn.setFont(font)
        self.prevBtn.setObjectName(_fromUtf8("prevBtn"))
        self.prevNextHL.addWidget(self.prevBtn)
        self.nextBtn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.prevNextHL.addWidget(self.nextBtn)
        self.categoryLayout.addLayout(self.prevNextHL)
        self.catAndProductHL.addLayout(self.categoryLayout)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.catAndProductHL.addWidget(self.line_2)
        self.leftProductButtons = QtGui.QVBoxLayout()
        self.leftProductButtons.setObjectName(_fromUtf8("leftProductButtons"))
        self.pBtn0 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn0.sizePolicy().hasHeightForWidth())
        self.pBtn0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn0.setFont(font)
        self.pBtn0.setText(_fromUtf8(""))
        self.pBtn0.setObjectName(_fromUtf8("pBtn0"))
        self.leftProductButtons.addWidget(self.pBtn0)
        self.pBtn2 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn2.sizePolicy().hasHeightForWidth())
        self.pBtn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn2.setFont(font)
        self.pBtn2.setText(_fromUtf8(""))
        self.pBtn2.setObjectName(_fromUtf8("pBtn2"))
        self.leftProductButtons.addWidget(self.pBtn2)
        self.pBtn4 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn4.sizePolicy().hasHeightForWidth())
        self.pBtn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn4.setFont(font)
        self.pBtn4.setText(_fromUtf8(""))
        self.pBtn4.setObjectName(_fromUtf8("pBtn4"))
        self.leftProductButtons.addWidget(self.pBtn4)
        self.pBtn6 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn6.sizePolicy().hasHeightForWidth())
        self.pBtn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn6.setFont(font)
        self.pBtn6.setText(_fromUtf8(""))
        self.pBtn6.setObjectName(_fromUtf8("pBtn6"))
        self.leftProductButtons.addWidget(self.pBtn6)
        self.pBtn8 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn8.sizePolicy().hasHeightForWidth())
        self.pBtn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn8.setFont(font)
        self.pBtn8.setText(_fromUtf8(""))
        self.pBtn8.setObjectName(_fromUtf8("pBtn8"))
        self.leftProductButtons.addWidget(self.pBtn8)
        self.pBtn10 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn10.sizePolicy().hasHeightForWidth())
        self.pBtn10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn10.setFont(font)
        self.pBtn10.setText(_fromUtf8(""))
        self.pBtn10.setObjectName(_fromUtf8("pBtn10"))
        self.leftProductButtons.addWidget(self.pBtn10)
        self.pBtn12 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn12.sizePolicy().hasHeightForWidth())
        self.pBtn12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn12.setFont(font)
        self.pBtn12.setText(_fromUtf8(""))
        self.pBtn12.setObjectName(_fromUtf8("pBtn12"))
        self.leftProductButtons.addWidget(self.pBtn12)
        self.pBtn14 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn14.sizePolicy().hasHeightForWidth())
        self.pBtn14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn14.setFont(font)
        self.pBtn14.setText(_fromUtf8(""))
        self.pBtn14.setObjectName(_fromUtf8("pBtn14"))
        self.leftProductButtons.addWidget(self.pBtn14)
        self.pBtn16 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn16.sizePolicy().hasHeightForWidth())
        self.pBtn16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn16.setFont(font)
        self.pBtn16.setText(_fromUtf8(""))
        self.pBtn16.setObjectName(_fromUtf8("pBtn16"))
        self.leftProductButtons.addWidget(self.pBtn16)
        self.catAndProductHL.addLayout(self.leftProductButtons)
        self.rightProductButtons = QtGui.QVBoxLayout()
        self.rightProductButtons.setObjectName(_fromUtf8("rightProductButtons"))
        self.pBtn1 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn1.sizePolicy().hasHeightForWidth())
        self.pBtn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn1.setFont(font)
        self.pBtn1.setText(_fromUtf8(""))
        self.pBtn1.setObjectName(_fromUtf8("pBtn1"))
        self.rightProductButtons.addWidget(self.pBtn1)
        self.pBtn3 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn3.sizePolicy().hasHeightForWidth())
        self.pBtn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn3.setFont(font)
        self.pBtn3.setText(_fromUtf8(""))
        self.pBtn3.setObjectName(_fromUtf8("pBtn3"))
        self.rightProductButtons.addWidget(self.pBtn3)
        self.pBtn5 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn5.sizePolicy().hasHeightForWidth())
        self.pBtn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn5.setFont(font)
        self.pBtn5.setText(_fromUtf8(""))
        self.pBtn5.setObjectName(_fromUtf8("pBtn5"))
        self.rightProductButtons.addWidget(self.pBtn5)
        self.pBtn7 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn7.sizePolicy().hasHeightForWidth())
        self.pBtn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn7.setFont(font)
        self.pBtn7.setText(_fromUtf8(""))
        self.pBtn7.setObjectName(_fromUtf8("pBtn7"))
        self.rightProductButtons.addWidget(self.pBtn7)
        self.pBtn9 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn9.sizePolicy().hasHeightForWidth())
        self.pBtn9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn9.setFont(font)
        self.pBtn9.setText(_fromUtf8(""))
        self.pBtn9.setObjectName(_fromUtf8("pBtn9"))
        self.rightProductButtons.addWidget(self.pBtn9)
        self.pBtn11 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn11.sizePolicy().hasHeightForWidth())
        self.pBtn11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn11.setFont(font)
        self.pBtn11.setText(_fromUtf8(""))
        self.pBtn11.setObjectName(_fromUtf8("pBtn11"))
        self.rightProductButtons.addWidget(self.pBtn11)
        self.pBtn13 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn13.sizePolicy().hasHeightForWidth())
        self.pBtn13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn13.setFont(font)
        self.pBtn13.setText(_fromUtf8(""))
        self.pBtn13.setObjectName(_fromUtf8("pBtn13"))
        self.rightProductButtons.addWidget(self.pBtn13)
        self.pBtn15 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn15.sizePolicy().hasHeightForWidth())
        self.pBtn15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn15.setFont(font)
        self.pBtn15.setText(_fromUtf8(""))
        self.pBtn15.setObjectName(_fromUtf8("pBtn15"))
        self.rightProductButtons.addWidget(self.pBtn15)
        self.pBtn17 = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBtn17.sizePolicy().hasHeightForWidth())
        self.pBtn17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pBtn17.setFont(font)
        self.pBtn17.setText(_fromUtf8(""))
        self.pBtn17.setObjectName(_fromUtf8("pBtn17"))
        self.rightProductButtons.addWidget(self.pBtn17)
        self.catAndProductHL.addLayout(self.rightProductButtons)
        self.rightVL.addLayout(self.catAndProductHL)
        self.rightVL.setStretch(0, 1)
        self.rightVL.setStretch(2, 3)
        self.gridLayout.addLayout(self.rightVL, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(2, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 862, 21))
        self.menuBar.setMouseTracking(True)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionFullscreen = QtGui.QAction(MainWindow)
        self.actionFullscreen.setObjectName(_fromUtf8("actionFullscreen"))
        self.actionWindowed = QtGui.QAction(MainWindow)
        self.actionWindowed.setObjectName(_fromUtf8("actionWindowed"))
        self.actionGame = QtGui.QAction(MainWindow)
        self.actionGame.setObjectName(_fromUtf8("actionGame"))
        self.menuBar.addAction(self.actionQuit)
        self.menuBar.addAction(self.actionFullscreen)
        self.menuBar.addAction(self.actionWindowed)
        self.menuBar.addAction(self.actionGame)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "\'t Gat in de Markt", None))
        self.totalLabel.setText(_translate("MainWindow", "Totaal", None))
        self.npBtn4.setText(_translate("MainWindow", "4", None))
        self.npBtn3.setText(_translate("MainWindow", "3", None))
        self.numpadClearButton.setText(_translate("MainWindow", "Clear", None))
        self.numpadBackspaceButton.setText(_translate("MainWindow", "Bksp", None))
        self.npBtn6.setText(_translate("MainWindow", "6", None))
        self.npBtn9.setText(_translate("MainWindow", "9", None))
        self.npBtn1.setText(_translate("MainWindow", "1", None))
        self.npBtn0.setText(_translate("MainWindow", "0", None))
        self.npBtn5.setText(_translate("MainWindow", "5", None))
        self.npBtn2.setText(_translate("MainWindow", "2", None))
        self.npBtn7.setText(_translate("MainWindow", "7", None))
        self.npBtn8.setText(_translate("MainWindow", "8", None))
        self.payCashButton.setText(_translate("MainWindow", "Contant", None))
        self.payPinButton.setText(_translate("MainWindow", "PIN", None))
        self.prevBtn.setText(_translate("MainWindow", "<<", None))
        self.nextBtn.setText(_translate("MainWindow", ">>", None))
        self.actionQuit.setText(_translate("MainWindow", "Afsluiten", None))
        self.actionFullscreen.setText(_translate("MainWindow", "Volledig scherm", None))
        self.actionWindowed.setText(_translate("MainWindow", "Venster", None))
        self.actionGame.setText(_translate("MainWindow", "Ik verveel me...", None))

from . import resource_rc
