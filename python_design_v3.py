# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bilal Bhatti\Desktop\version 3\python_design_v3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from threading import Thread
from traceback import format_exc
from pyexcelerate import Workbook

import threading
import traceback
import datetime

from numpy import *
from numpy.core import *
import numpy.core._dtype_ctypes

import pandas as pd
from pandas import DataFrame
from pandas import Series
from pandas import read_excel

# ----------------------LOGGING---------------------------------
# Importing the logging module
import logging
# Defining the format of the string of the log message
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
# Setting the bacic configuration of the logger.

from pathlib import Path
home = str(Path.home())

f_name = home + '\\data.log'
print("Logging is saving in: {}".format(f_name))
logging.basicConfig(filename= f_name,
                    format=LOG_FORMAT,
                    level=logging.DEBUG,
                    filemode='w'
                    )
# Getting the logger object of the default name 'Root'
logger = logging.getLogger()
# ---------------------LOGGING----------------------------------


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.first_file_path = ''
        self.second_file_path = ''
        self.destination_file_path = ''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.first_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.first_file_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.first_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.first_file_btn.setObjectName("first_file_btn")
        self.gridLayout.addWidget(self.first_file_btn, 1, 2, 1, 1)
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
        self.second_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.second_file_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.second_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.second_file_btn.setObjectName("second_file_btn")
        self.gridLayout.addWidget(self.second_file_btn, 4, 2, 1, 1)
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

        self.first_file_btn.clicked.connect(self.onSelectFirstFileBtnClick)
        self.second_file_btn.clicked.connect(self.onSelectSecondFileBtnClick)
        self.select_destination_btn.clicked.connect(self.onSelectDestinationDirBtnClick)
        self.execute_btn.clicked.connect(self.onExecuteBtnClick)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.first_file_btn.setToolTip(_translate("MainWindow", "Click to Select Database File"))
        self.first_file_btn.setText(_translate("MainWindow", "Select First File"))
        self.db_file_label.setText(_translate("MainWindow", "Database File Path"))
        self.user_input_file_label.setText(_translate("MainWindow", "User Input File Path"))
        self.user_file_spiner.setToolTip(_translate("MainWindow", "Select Sheet Number By Default the selected sheet is zero means sheet 1"))
        self.sheet_number_label_2.setText(_translate("MainWindow", "Select Sheet Number :"))
        self.second_file_btn.setToolTip(_translate("MainWindow", "Click To Select User Input File"))
        self.second_file_btn.setText(_translate("MainWindow", "Select Second File"))
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


    def onSelectFirstFileBtnClick(self):
        print('Select First File btn Clicked')
        logger.info("Select First File Button Clicked")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select First File File", "", "DB Files (*.xlsx *.xls )") # Ask for file
        if fileName: # If the user gives a file
            print(fileName)
            self.db_file_label.setText(fileName)
            self.first_file_path = fileName

    def onSelectSecondFileBtnClick(self):
        print('Select Second File Btn Clicked')
        logger.info("Select Second File Btn Clicked")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Second File", "", "DB Files (*.xlsx *.xls )") # Ask for file
        if fileName: # If the user gives a file
            print(fileName)
            self.user_input_file_label.setText(fileName)
            self.second_file_path = fileName

    def onSelectDestinationDirBtnClick(self):
        logger.info("Select Destination Button Clicked.")

        print('Select Destinationg Btn Clicked')
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None) # Ask for file
        if fileName:
            print(fileName)
            self.destination_file_path = fileName


    def onExecuteBtnClick(self):
        logger.info("Execute Button Clicked")

        first_file_sheet_no = self.db_sheet_spiner.value()
        second_file_sheet_no = self.user_file_spiner.value()

        message = ''
        if len(self.first_file_path) == 0:
            message = message + 'First File Path Missing!\n'
        if len(self.second_file_path) == 0:
            message = message + 'Second File Path Missing!\n'
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

            thread = threading.Thread(target=self.script,
                args=(self.first_file_path,
                      first_file_sheet_no,
                      self.second_file_path,
                      second_file_sheet_no,
                      self.destination_file_path))
            thread.start()

    def script(self, first_file_path,first_file_sheet_no,second_file_path,second_file_sheet_no,destination_file_path):
        print('Script Executing')

        try:
            logger.debug("Reading First File")
            X = self.readExcelSheet(first_file_path, first_file_sheet_no)

            logger.debug("Reading Second File")
            Y = self.readExcelSheet(second_file_path, second_file_sheet_no)

            logger.debug("Equal the Columns.")
            X, Y = self.equalTheColumns(X, Y)

            logger.debug("Converting Columns To String.")
            str_x, str_y = self.convertToStringColumn(X, Y)

            logger.debug("Counting Columns Similarites.")
            count_series = self.preformCalculations(str_x, str_y)

            logger.debug("Making Export DataFrame.")
            export_df = self.makeDataFrameForExport(str_x, count_series)

            logger.debug("Writing To Destination.")
            self.writeToExcel(destination_file_path, export_df)

            logger.info("Finished Conversion.")
            self.load_label.setText('--FINISHED--')
        except Exception as e:
            print(e)
            self.load_label.setText('--FAILED--')

        self.user_input_file_label.setText(self.first_file_path)
        self.db_file_label.setText(self.second_file_path)
        self.execute_btn.setEnabled(True)

    # -----------------------------------------------------------------------------------------------
    def readExcelSheet(self, file_path, sheet_no):
        df = pd.read_excel(file_path, sheet_name=sheet_no, header=None)
        return df

    def writeToExcel(self, dest_path, dataframe):
        now = datetime.datetime.now()
        date = now.date()
        time = now.time()
        dt = str(date.year) + str(date.month) + str(date.day) + str(time.hour) + str(time.minute) + str(time.second) + str(time.microsecond)

        f_name = 'output' + dt + '.xlsx'
        path = dest_path + '/' + f_name
        writer = pd.ExcelWriter(path)
        dataframe.to_excel(writer, 'Sheet1', header=False, index=False)
        writer.save()

    def writeToCsv(self, dest_path, dataframe):
        now = datetime.datetime.now()
        date = now.date()
        time = now.time()
        dt = str(date.year) + str(date.month) + str(date.day) + str(time.hour) + str(time.minute) + str(time.second) + str(time.microsecond)

        f_name = 'output' + dt + '.csv'
        path = dest_path + '/' + f_name
        logger.debug("CSV Export Started.")
        df.to_csv(path, chunksize=1000, header=False, index=False)


    def equalTheColumns(self, X, Y):
        x_col_size = X.columns.size
        y_col_size = Y.columns.size

        if x_col_size < y_col_size:
            Y = Y.iloc[:, :x_col_size]
        elif x_col_size > y_col_size:
            X = X.iloc[:, :y_col_size]
        else:
            pass

        return (X, Y)


    def convertToStringColumn(self, X, Y):
        x_str = pd.Series(X.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))
        y_str = pd.Series(Y.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))

        return (x_str, y_str)

    def makeDataFrameForExport(self, str_series, count_series):
        d_frame = pd.DataFrame(str_series, columns=['Dashed Column'])
        d_frame['Count Column'] = count_series
        return d_frame



    def preformCalculations(self, X, Y):
        '''
        Preforms the count X over Y.
        :param X: pandas.Series
        :param Y: pandas.Series
        :return: Count as pandas.Series
        '''
        dictionary = {}
        rep_list = []
        for row in X:
           count = -1
           if row not in dictionary:
              dictionary[row] = count =Y.where(Y == row).count()
           else:
              count  = dictionary[row]
           if count == 0:
              count = count + 1
           s = str(count) + ' times'
           rep_list.append(s)
        count_series = pd.Series(rep_list)
        return count_series

    # -----------------------------------------------------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

