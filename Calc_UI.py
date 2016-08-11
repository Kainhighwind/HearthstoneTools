# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc_UI.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(690, 805)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.MainBox = QtGui.QTabWidget(self.centralwidget)
        self.MainBox.setEnabled(True)
        self.MainBox.setObjectName(_fromUtf8("MainBox"))
        self.SingleOutsTab = QtGui.QWidget()
        self.SingleOutsTab.setObjectName(_fromUtf8("SingleOutsTab"))
        self.SingleOutWidget = QtGui.QWidget(self.SingleOutsTab)
        self.SingleOutWidget.setGeometry(QtCore.QRect(20, 30, 621, 651))
        self.SingleOutWidget.setObjectName(_fromUtf8("SingleOutWidget"))
        self.groupBox = QtGui.QGroupBox(self.SingleOutWidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 0, 400, 201))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 200))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 362, 131))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(50)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.remainingDeckSizeLabel = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.remainingDeckSizeLabel.setFont(font)
        self.remainingDeckSizeLabel.setAutoFillBackground(False)
        self.remainingDeckSizeLabel.setObjectName(_fromUtf8("remainingDeckSizeLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.remainingDeckSizeLabel)
        self.remainingDeckSizeSpinBox = QtGui.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.remainingDeckSizeSpinBox.setFont(font)
        self.remainingDeckSizeSpinBox.setProperty("value", 30)
        self.remainingDeckSizeSpinBox.setObjectName(_fromUtf8("remainingDeckSizeSpinBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.remainingDeckSizeSpinBox)
        self.numberOfDrawsLabel = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.numberOfDrawsLabel.setFont(font)
        self.numberOfDrawsLabel.setObjectName(_fromUtf8("numberOfDrawsLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.numberOfDrawsLabel)
        self.numberOfDrawsSpinBox = QtGui.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.numberOfDrawsSpinBox.setFont(font)
        self.numberOfDrawsSpinBox.setProperty("value", 7)
        self.numberOfDrawsSpinBox.setObjectName(_fromUtf8("numberOfDrawsSpinBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.numberOfDrawsSpinBox)
        self.numberOfOutsInDeckLabel = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.numberOfOutsInDeckLabel.setFont(font)
        self.numberOfOutsInDeckLabel.setObjectName(_fromUtf8("numberOfOutsInDeckLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.numberOfOutsInDeckLabel)
        self.numberOfOutsInDeckSpinBox = QtGui.QSpinBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.numberOfOutsInDeckSpinBox.setFont(font)
        self.numberOfOutsInDeckSpinBox.setProperty("value", 4)
        self.numberOfOutsInDeckSpinBox.setObjectName(_fromUtf8("numberOfOutsInDeckSpinBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.numberOfOutsInDeckSpinBox)
        self.splitter = QtGui.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(10, 150, 361, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.CalculateButton = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CalculateButton.setFont(font)
        self.CalculateButton.setObjectName(_fromUtf8("CalculateButton"))
        self.ResetButton = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResetButton.setFont(font)
        self.ResetButton.setObjectName(_fromUtf8("ResetButton"))
        self.probabilityTable = QtGui.QTableWidget(self.SingleOutWidget)
        self.probabilityTable.setGeometry(QtCore.QRect(30, 210, 411, 221))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probabilityTable.sizePolicy().hasHeightForWidth())
        self.probabilityTable.setSizePolicy(sizePolicy)
        self.probabilityTable.setMaximumSize(QtCore.QSize(415, 450))
        self.probabilityTable.setRowCount(1)
        self.probabilityTable.setColumnCount(4)
        self.probabilityTable.setObjectName(_fromUtf8("probabilityTable"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.probabilityTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.probabilityTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.probabilityTable.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.probabilityTable.setItem(0, 3, item)
        self.probabilityTable.horizontalHeader().setVisible(False)
        self.probabilityTable.verticalHeader().setVisible(False)
        self.GraphArea = QtGui.QFrame(self.SingleOutWidget)
        self.GraphArea.setGeometry(QtCore.QRect(30, 450, 501, 181))
        self.GraphArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.GraphArea.setFrameShadow(QtGui.QFrame.Raised)
        self.GraphArea.setObjectName(_fromUtf8("GraphArea"))
        self.MainBox.addTab(self.SingleOutsTab, _fromUtf8(""))
        self.MultiVariateTab = QtGui.QWidget()
        self.MultiVariateTab.setObjectName(_fromUtf8("MultiVariateTab"))
        self.MultiVariateTab_2 = QtGui.QWidget(self.MultiVariateTab)
        self.MultiVariateTab_2.setGeometry(QtCore.QRect(20, 10, 621, 651))
        self.MultiVariateTab_2.setObjectName(_fromUtf8("MultiVariateTab_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.MultiVariateTab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 20, 400, 291))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(400, 200))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 331, 131))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setHorizontalSpacing(50)
        self.formLayout_2.setVerticalSpacing(3)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.remainingDeckSizeLabel_2 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.remainingDeckSizeLabel_2.setFont(font)
        self.remainingDeckSizeLabel_2.setAutoFillBackground(False)
        self.remainingDeckSizeLabel_2.setObjectName(_fromUtf8("remainingDeckSizeLabel_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.remainingDeckSizeLabel_2)
        self.remainingDeckSizeSpinBox_2 = QtGui.QSpinBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.remainingDeckSizeSpinBox_2.setFont(font)
        self.remainingDeckSizeSpinBox_2.setProperty("value", 30)
        self.remainingDeckSizeSpinBox_2.setObjectName(_fromUtf8("remainingDeckSizeSpinBox_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.remainingDeckSizeSpinBox_2)
        self.numberOfDrawsLabel_2 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.numberOfDrawsLabel_2.setFont(font)
        self.numberOfDrawsLabel_2.setObjectName(_fromUtf8("numberOfDrawsLabel_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.numberOfDrawsLabel_2)
        self.numberOfDrawsSpinBox_2 = QtGui.QSpinBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.numberOfDrawsSpinBox_2.setFont(font)
        self.numberOfDrawsSpinBox_2.setProperty("value", 7)
        self.numberOfDrawsSpinBox_2.setObjectName(_fromUtf8("numberOfDrawsSpinBox_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.numberOfDrawsSpinBox_2)
        self.numberOfOutsInDeckLabel_2 = QtGui.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.numberOfOutsInDeckLabel_2.setFont(font)
        self.numberOfOutsInDeckLabel_2.setObjectName(_fromUtf8("numberOfOutsInDeckLabel_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.numberOfOutsInDeckLabel_2)
        self.numberOfOutsInDeckSpinBox_2 = QtGui.QSpinBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.numberOfOutsInDeckSpinBox_2.setFont(font)
        self.numberOfOutsInDeckSpinBox_2.setProperty("value", 4)
        self.numberOfOutsInDeckSpinBox_2.setObjectName(_fromUtf8("numberOfOutsInDeckSpinBox_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.numberOfOutsInDeckSpinBox_2)
        self.splitter_2 = QtGui.QSplitter(self.groupBox_2)
        self.splitter_2.setGeometry(QtCore.QRect(10, 250, 361, 31))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.CalculateButton_2 = QtGui.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CalculateButton_2.setFont(font)
        self.CalculateButton_2.setObjectName(_fromUtf8("CalculateButton_2"))
        self.ResetButton_2 = QtGui.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResetButton_2.setFont(font)
        self.ResetButton_2.setObjectName(_fromUtf8("ResetButton_2"))
        self.probabilityTable_2 = QtGui.QTableWidget(self.MultiVariateTab_2)
        self.probabilityTable_2.setGeometry(QtCore.QRect(30, 339, 411, 321))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.probabilityTable_2.sizePolicy().hasHeightForWidth())
        self.probabilityTable_2.setSizePolicy(sizePolicy)
        self.probabilityTable_2.setMaximumSize(QtCore.QSize(415, 450))
        self.probabilityTable_2.setRowCount(1)
        self.probabilityTable_2.setColumnCount(4)
        self.probabilityTable_2.setObjectName(_fromUtf8("probabilityTable_2"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.probabilityTable_2.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.probabilityTable_2.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.probabilityTable_2.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.probabilityTable_2.setItem(0, 3, item)
        self.probabilityTable_2.horizontalHeader().setVisible(False)
        self.probabilityTable_2.verticalHeader().setVisible(False)
        self.MainBox.addTab(self.MultiVariateTab, _fromUtf8(""))
        self.BombTab = QtGui.QWidget()
        self.BombTab.setObjectName(_fromUtf8("BombTab"))
        self.AddMinionPushButton = QtGui.QPushButton(self.BombTab)
        self.AddMinionPushButton.setGeometry(QtCore.QRect(60, 400, 111, 21))
        self.AddMinionPushButton.setObjectName(_fromUtf8("AddMinionPushButton"))
        self.MyHeathSpinBox = QtGui.QSpinBox(self.BombTab)
        self.MyHeathSpinBox.setGeometry(QtCore.QRect(340, 350, 42, 22))
        self.MyHeathSpinBox.setObjectName(_fromUtf8("MyHeathSpinBox"))
        self.EnemyHealthSpinBox = QtGui.QSpinBox(self.BombTab)
        self.EnemyHealthSpinBox.setGeometry(QtCore.QRect(320, 110, 42, 22))
        self.EnemyHealthSpinBox.setObjectName(_fromUtf8("EnemyHealthSpinBox"))
        self.EnemHealth = QtGui.QLabel(self.BombTab)
        self.EnemHealth.setGeometry(QtCore.QRect(220, 100, 81, 41))
        self.EnemHealth.setObjectName(_fromUtf8("EnemHealth"))
        self.RemoveMinionPushButton = QtGui.QPushButton(self.BombTab)
        self.RemoveMinionPushButton.setGeometry(QtCore.QRect(190, 400, 121, 21))
        self.RemoveMinionPushButton.setObjectName(_fromUtf8("RemoveMinionPushButton"))
        self.MinionHealthSpinBox = QtGui.QSpinBox(self.BombTab)
        self.MinionHealthSpinBox.setGeometry(QtCore.QRect(180, 460, 61, 31))
        self.MinionHealthSpinBox.setObjectName(_fromUtf8("MinionHealthSpinBox"))
        self.MinionHealthLabel = QtGui.QLabel(self.BombTab)
        self.MinionHealthLabel.setGeometry(QtCore.QRect(70, 470, 91, 21))
        self.MinionHealthLabel.setObjectName(_fromUtf8("MinionHealthLabel"))
        self.DivineShield = QtGui.QCheckBox(self.BombTab)
        self.DivineShield.setGeometry(QtCore.QRect(60, 500, 101, 21))
        self.DivineShield.setObjectName(_fromUtf8("DivineShield"))
        self.MinionName = QtGui.QLineEdit(self.BombTab)
        self.MinionName.setGeometry(QtCore.QRect(60, 440, 113, 20))
        self.MinionName.setObjectName(_fromUtf8("MinionName"))
        self.Silenced = QtGui.QCheckBox(self.BombTab)
        self.Silenced.setGeometry(QtCore.QRect(60, 530, 70, 17))
        self.Silenced.setObjectName(_fromUtf8("Silenced"))
        self.BoardState = QtGui.QTableWidget(self.BombTab)
        self.BoardState.setGeometry(QtCore.QRect(80, 140, 491, 191))
        self.BoardState.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.BoardState.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.BoardState.setRowCount(2)
        self.BoardState.setColumnCount(7)
        self.BoardState.setObjectName(_fromUtf8("BoardState"))
        item = QtGui.QTableWidgetItem()
        self.BoardState.setItem(0, 0, item)
        self.BoardState.horizontalHeader().setVisible(False)
        self.BoardState.horizontalHeader().setDefaultSectionSize(69)
        self.BoardState.horizontalHeader().setMinimumSectionSize(21)
        self.BoardState.verticalHeader().setVisible(False)
        self.BoardState.verticalHeader().setDefaultSectionSize(90)
        self.PlayerSelectBox = QtGui.QComboBox(self.BombTab)
        self.PlayerSelectBox.setGeometry(QtCore.QRect(200, 430, 69, 22))
        self.PlayerSelectBox.setObjectName(_fromUtf8("PlayerSelectBox"))
        self.PlayerSelectBox.addItem(_fromUtf8(""))
        self.PlayerSelectBox.addItem(_fromUtf8(""))
        self.MyHeath = QtGui.QLabel(self.BombTab)
        self.MyHeath.setGeometry(QtCore.QRect(210, 350, 81, 16))
        self.MyHeath.setObjectName(_fromUtf8("MyHeath"))
        self.MainBox.addTab(self.BombTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.MainBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionTest = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/HS/2016-04-10 13-33-34.926.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTest.setIcon(icon)
        self.actionTest.setObjectName(_fromUtf8("actionTest"))

        self.retranslateUi(MainWindow)
        self.MainBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.ResetButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.numberOfOutsInDeckSpinBox.clear)
        QtCore.QObject.connect(self.ResetButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.numberOfDrawsSpinBox.clear)
        QtCore.QObject.connect(self.ResetButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.remainingDeckSizeSpinBox.clear)
        QtCore.QObject.connect(self.ResetButton, QtCore.SIGNAL(_fromUtf8("pressed()")), self.probabilityTable.reset)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.remainingDeckSizeLabel.setText(_translate("MainWindow", "Deck Size", None))
        self.numberOfDrawsLabel.setText(_translate("MainWindow", "Number of Draws", None))
        self.numberOfOutsInDeckLabel.setText(_translate("MainWindow", "Number of Outs in Deck", None))
        self.CalculateButton.setText(_translate("MainWindow", "Calculate!", None))
        self.ResetButton.setText(_translate("MainWindow", "Reset", None))
        __sortingEnabled = self.probabilityTable.isSortingEnabled()
        self.probabilityTable.setSortingEnabled(False)
        item = self.probabilityTable.item(0, 0)
        item.setText(_translate("MainWindow", "Exactly", None))
        item = self.probabilityTable.item(0, 1)
        item.setText(_translate("MainWindow", "Probability", None))
        item = self.probabilityTable.item(0, 2)
        item.setText(_translate("MainWindow", "At Least", None))
        item = self.probabilityTable.item(0, 3)
        item.setText(_translate("MainWindow", "Probablity", None))
        self.probabilityTable.setSortingEnabled(__sortingEnabled)
        self.MainBox.setTabText(self.MainBox.indexOf(self.SingleOutsTab), _translate("MainWindow", "Single Out Group", None))
        self.remainingDeckSizeLabel_2.setText(_translate("MainWindow", "Deck Size", None))
        self.numberOfDrawsLabel_2.setText(_translate("MainWindow", "Number of Draws", None))
        self.numberOfOutsInDeckLabel_2.setText(_translate("MainWindow", "Number of Outs in Deck", None))
        self.CalculateButton_2.setText(_translate("MainWindow", "Calculate!", None))
        self.ResetButton_2.setText(_translate("MainWindow", "Reset", None))
        __sortingEnabled = self.probabilityTable_2.isSortingEnabled()
        self.probabilityTable_2.setSortingEnabled(False)
        item = self.probabilityTable_2.item(0, 0)
        item.setText(_translate("MainWindow", "Exactly", None))
        item = self.probabilityTable_2.item(0, 1)
        item.setText(_translate("MainWindow", "Probability", None))
        item = self.probabilityTable_2.item(0, 2)
        item.setText(_translate("MainWindow", "At Least", None))
        item = self.probabilityTable_2.item(0, 3)
        item.setText(_translate("MainWindow", "Probablity", None))
        self.probabilityTable_2.setSortingEnabled(__sortingEnabled)
        self.MainBox.setTabText(self.MainBox.indexOf(self.MultiVariateTab), _translate("MainWindow", "Page", None))
        self.AddMinionPushButton.setText(_translate("MainWindow", "AddMinion", None))
        self.EnemHealth.setText(_translate("MainWindow", "Enemy Hero Health", None))
        self.RemoveMinionPushButton.setText(_translate("MainWindow", "RemoveLastMinion", None))
        self.MinionHealthLabel.setText(_translate("MainWindow", "Minion Health", None))
        self.DivineShield.setText(_translate("MainWindow", "Divine Shield", None))
        self.MinionName.setText(_translate("MainWindow", "Minions Name", None))
        self.Silenced.setText(_translate("MainWindow", "Silenced", None))
        __sortingEnabled = self.BoardState.isSortingEnabled()
        self.BoardState.setSortingEnabled(False)
        self.BoardState.setSortingEnabled(__sortingEnabled)
        self.PlayerSelectBox.setItemText(0, _translate("MainWindow", "Our\'s", None))
        self.PlayerSelectBox.setItemText(1, _translate("MainWindow", "Enemy\'s", None))
        self.MyHeath.setText(_translate("MainWindow", "Your Hero Health", None))
        self.MainBox.setTabText(self.MainBox.indexOf(self.BombTab), _translate("MainWindow", "Bomber odds", None))
        self.actionTest.setText(_translate("MainWindow", "Test", None))
        self.actionTest.setToolTip(_translate("MainWindow", "Test", None))

import HSstuff_rc