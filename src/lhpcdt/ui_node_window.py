# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'node_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_panel = QtWidgets.QWidget(self.centralwidget)
        self.search_panel.setObjectName("search_panel")
        self.search_layout = QtWidgets.QHBoxLayout(self.search_panel)
        self.search_layout.setSpacing(6)
        self.search_layout.setObjectName("search_layout")
        self.label = QtWidgets.QLabel(self.search_panel)
        self.label.setObjectName("label")
        self.search_layout.addWidget(self.label)
        self.search_combo = QtWidgets.QComboBox(self.search_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_combo.sizePolicy().hasHeightForWidth())
        self.search_combo.setSizePolicy(sizePolicy)
        self.search_combo.setEditable(True)
        self.search_combo.setObjectName("search_combo")
        self.search_layout.addWidget(self.search_combo)
        self.verticalLayout.addWidget(self.search_panel)
        self.node_view_table = QtWidgets.QTableView(self.centralwidget)
        self.node_view_table.setObjectName("node_view_table")
        self.node_view_table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.node_view_table)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.running_jobs_label = QtWidgets.QLabel(self.centralwidget)
        self.running_jobs_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.running_jobs_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.running_jobs_label.setObjectName("running_jobs_label")
        self.horizontalLayout.addWidget(self.running_jobs_label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.waiting_jobs_label = QtWidgets.QLabel(self.centralwidget)
        self.waiting_jobs_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.waiting_jobs_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.waiting_jobs_label.setObjectName("waiting_jobs_label")
        self.horizontalLayout.addWidget(self.waiting_jobs_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.processing_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.processing_progress.setProperty("value", 0)
        self.processing_progress.setInvertedAppearance(False)
        self.processing_progress.setObjectName("processing_progress")
        self.verticalLayout.addWidget(self.processing_progress)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_refresh = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/round_refresh_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_refresh.setIcon(icon)
        self.action_refresh.setObjectName("action_refresh")
        self.action_auto_refresh = QtWidgets.QAction(MainWindow)
        self.action_auto_refresh.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/round_autorenew_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_auto_refresh.setIcon(icon1)
        self.action_auto_refresh.setObjectName("action_auto_refresh")
        self.action_search = QtWidgets.QAction(MainWindow)
        self.action_search.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/round_search_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_search.setIcon(icon2)
        self.action_search.setObjectName("action_search")
        self.toolBar.addAction(self.action_refresh)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_search)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_auto_refresh)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SLURM Node Monitor"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.label_2.setText(_translate("MainWindow", "Jobs running:"))
        self.running_jobs_label.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "jobs waiting:"))
        self.waiting_jobs_label.setText(_translate("MainWindow", "0"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_refresh.setText(_translate("MainWindow", "Refresh"))
        self.action_auto_refresh.setText(_translate("MainWindow", "Auto refresh"))
        self.action_search.setText(_translate("MainWindow", "Search"))
        self.action_search.setShortcut(_translate("MainWindow", "Ctrl+F"))
from . import toolbar_icons_rc
