# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bilal Bhatti\Desktop\version 2\python_design_v2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading
#----------------------LOGGING---------------------------------
# Importing the logging module
import logging
#Defining the format of the string of the log message
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
#Setting the bacic configuration of the logger.

from pathlib import Path
home = str(Path.home())

f_name = home + '\\data.log'
print("Logging is saving in: {}".format(f_name))
logging.basicConfig(filename= f_name,
                    format=LOG_FORMAT,
                    level=logging.DEBUG,
                    filemode='w'
                    )
#Getting the logger object of the default name 'Root'
logger = logging.getLogger()
#---------------------LOGGING----------------------------------



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.db_file_path = ''
        self.user_file_path = ''
        self.destination_file_path = ''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.select_db_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_db_file_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.select_db_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_db_file_btn.setObjectName("select_db_file_btn")
        self.gridLayout.addWidget(self.select_db_file_btn, 1, 2, 1, 1)
        self.db_file_label = QtWidgets.QLabel(self.centralwidget)
        self.db_file_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.db_file_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.db_file_label.setMouseTracking(False)
        self.db_file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.db_file_label.setObjectName("db_file_label")
        self.gridLayout.addWidget(self.db_file_label, 0, 0, 1, 3)
        self.user_input_file_label = QtWidgets.QLabel(self.centralwidget)
        self.user_input_file_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.user_input_file_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.user_input_file_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_input_file_label.setObjectName("user_input_file_label")
        self.gridLayout.addWidget(self.user_input_file_label, 3, 0, 1, 3)
        self.user_file_spiner = QtWidgets.QSpinBox(self.centralwidget)
        self.user_file_spiner.setMaximumSize(QtCore.QSize(16777215, 40))
        self.user_file_spiner.setObjectName("user_file_spiner")
        self.gridLayout.addWidget(self.user_file_spiner, 4, 1, 1, 1)
        self.sheet_number_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.sheet_number_label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.sheet_number_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sheet_number_label_2.setObjectName("sheet_number_label_2")
        self.gridLayout.addWidget(self.sheet_number_label_2, 4, 0, 1, 1)
        self.select_user_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_user_file_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.select_user_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_user_file_btn.setObjectName("select_user_file_btn")
        self.gridLayout.addWidget(self.select_user_file_btn, 4, 2, 1, 1)
        self.select_destination_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_destination_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.select_destination_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_destination_btn.setObjectName("select_destination_btn")
        self.gridLayout.addWidget(self.select_destination_btn, 6, 0, 1, 3)
        self.db_sheet_spiner = QtWidgets.QSpinBox(self.centralwidget)
        self.db_sheet_spiner.setMaximumSize(QtCore.QSize(16777215, 40))
        self.db_sheet_spiner.setObjectName("db_sheet_spiner")
        self.gridLayout.addWidget(self.db_sheet_spiner, 1, 1, 1, 1)
        self.execute_btn = QtWidgets.QPushButton(self.centralwidget)
        self.execute_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.execute_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.execute_btn.setObjectName("execute_btn")
        self.gridLayout.addWidget(self.execute_btn, 7, 0, 1, 3)
        self.load_label = QtWidgets.QLabel(self.centralwidget)
        self.load_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.load_label.setText("")
        self.load_label.setAlignment(QtCore.Qt.AlignCenter)
        self.load_label.setObjectName("load_label")
        self.gridLayout.addWidget(self.load_label, 5, 1, 1, 1)
        self.sheet_number_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.sheet_number_label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sheet_number_label_1.setObjectName("sheet_number_label_1")
        self.gridLayout.addWidget(self.sheet_number_label_1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        self.menuHello = QtWidgets.QMenu(self.menubar)
        self.menuHello.setObjectName("menuHello")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.about_application = QtWidgets.QAction(MainWindow)
        self.about_application.setObjectName("about_application")
        self.about_developer = QtWidgets.QAction(MainWindow)
        self.about_developer.setObjectName("about_developer")
        self.menuHello.addAction(self.exit)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.about_application)
        self.menuAbout.addAction(self.about_developer)
        self.menubar.addAction(self.menuHello.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.select_db_file_btn.clicked.connect(self.onSelectDatabaseBtnClick)
        self.select_user_file_btn.clicked.connect(self.onSelectUserFileBtnClick)
        self.select_destination_btn.clicked.connect(self.onSelectDestinationDirBtnClick)
        self.execute_btn.clicked.connect(self.onExecuteBtnClick)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_db_file_btn.setToolTip(_translate("MainWindow", "Click to Select Database File"))
        self.select_db_file_btn.setText(_translate("MainWindow", "Select Database File"))
        self.db_file_label.setText(_translate("MainWindow", "Database File Path"))
        self.user_input_file_label.setText(_translate("MainWindow", "User Input File Path"))
        self.user_file_spiner.setToolTip(_translate("MainWindow", "Select Sheet Number By Default the selected sheet is zero means sheet 1"))
        self.sheet_number_label_2.setText(_translate("MainWindow", "Select Sheet Number :"))
        self.select_user_file_btn.setToolTip(_translate("MainWindow", "Click To Select User Input File"))
        self.select_user_file_btn.setText(_translate("MainWindow", "Select User Input File"))
        self.select_destination_btn.setToolTip(_translate("MainWindow", "Click To Select Output File Destination Directory"))
        self.select_destination_btn.setText(_translate("MainWindow", "Select Destination Path"))
        self.db_sheet_spiner.setToolTip(_translate("MainWindow", "Select Sheet Number By Default the selected sheet is zero means sheet 1"))
        self.execute_btn.setToolTip(_translate("MainWindow", "Execute Control"))
        self.execute_btn.setText(_translate("MainWindow", "GO"))
        self.sheet_number_label_1.setText(_translate("MainWindow", "Select Sheet Number: "))
        self.menuHello.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.about_application.setText(_translate("MainWindow", "About Application"))
        self.about_developer.setText(_translate("MainWindow", "About Developer"))


    def onSelectDatabaseBtnClick(self):
        print('Select DB btn Clicked')
        logger.info("Select DB Button Clicked")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Database File", "", "DB Files (*.xlsx *.xls )") # Ask for file
        if fileName: # If the user gives a file
            print(fileName)
            self.db_file_label.setText(fileName)
            self.db_file_path = fileName


    def onSelectUserFileBtnClick(self):
        print('Select user File Btn Clicked')
        logger.info("Selece User Button Clicked")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select User Input File", "", "DB Files (*.xlsx *.xls )") # Ask for file
        if fileName: # If the user gives a file
            print(fileName)
            self.user_input_file_label.setText(fileName)
            self.user_file_path = fileName

    def onSelectDestinationDirBtnClick(self):
        logger.info("Select Destination Button Clicked.")

        print('Select Destinationg Btn Clicked')
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None) # Ask for file
        if fileName:
            print(fileName)
            self.destination_file_path = fileName


        # #-----------------Animation--------------------
        # self.movie.stop()
        # self.execute_btn.setEnabled(True)
        # #-----------------Animation--------------------


    def onExecuteBtnClick(self):
        logger.info("Execute Button Clicked")


        db_sheet_no = self.db_sheet_spiner.value()
        user_sheet_no = self.user_file_spiner.value()

        message = ''
        if len(self.db_file_path) == 0:
            message = message + 'DB File Path Missing!\n'
        if len(self.user_file_path) == 0:
            message = message + 'User File Path Missing!\n'
        if len(self.destination_file_path) == 0:
            message = message + 'Destination Path Missing!\n'

        if len(message) > 0:
            mb = QtWidgets.QMessageBox()
            mb.setIcon(mb.Information)
            mb.setWindowTitle("MESSAGE WINDOW")
            mb.setInformativeText(message)
            mb.setStandardButtons(mb.Ok)
            mb.exec_()
        else:
            #-----------------Animation--------------------
            self.movie = QtGui.QMovie("ajax-loader2.gif")
            self.load_label.setMovie(self.movie)
            self.movie.start()
            self.execute_btn.setDisabled(True)
            #-----------------Animation--------------------

            thread = threading.Thread(target=self.script)
            thread.start()





    def script(self):
        print("Script Runs")
        logger.info("Script Running.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

