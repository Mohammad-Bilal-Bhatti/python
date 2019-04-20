# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Bilal Bhatti\Desktop\python exel reader\python_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import traceback
import pandas as pd


# Importing the logging module
import logging
#Defining the format of the string of the log message
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
#Setting the bacic configuration of the logger.

from pathlib import Path
home = str(Path.home())

f_name = home + '\\data.log'

logging.basicConfig(filename= f_name,
                    format=LOG_FORMAT,
                    level=logging.DEBUG,
                    filemode='w'
                    )
#Getting the logger object of the default name 'Root'
logger = logging.getLogger()

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
        self.execute_btn = QtWidgets.QPushButton(self.centralwidget)
        self.execute_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.execute_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.execute_btn.setObjectName("execute_btn")
        self.gridLayout.addWidget(self.execute_btn, 6, 0, 1, 3)

        self.sheet_number_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.sheet_number_label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.sheet_number_label_2.setObjectName("sheet_number_label_2")
        self.gridLayout.addWidget(self.sheet_number_label_2, 4, 0, 1, 1)

        self.select_destination_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_destination_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.select_destination_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_destination_btn.setObjectName("select_destination_btn")
        self.gridLayout.addWidget(self.select_destination_btn, 5, 0, 1, 3)
        self.select_user_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_user_file_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.select_user_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_user_file_btn.setObjectName("select_user_file_btn")
        self.gridLayout.addWidget(self.select_user_file_btn, 4, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sheet_number_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.sheet_number_label_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.sheet_number_label_1.setObjectName("sheet_number_label_1")
        self.horizontalLayout_2.addWidget(self.sheet_number_label_1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.db_sheet_spiner = QtWidgets.QSpinBox(self.centralwidget)
        self.db_sheet_spiner.setMaximumSize(QtCore.QSize(16777215, 40))
        self.db_sheet_spiner.setObjectName("db_sheet_spiner")
        self.gridLayout.addWidget(self.db_sheet_spiner, 1, 1, 1, 1)

        self.select_db_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_db_file_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.select_db_file_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.select_db_file_btn.setObjectName("select_db_file_btn")
        self.gridLayout.addWidget(self.select_db_file_btn, 1, 2, 1, 1)

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

        self.select_db_file_btn.clicked.connect(self.onDBFileBtnClick)
        self.select_user_file_btn.clicked.connect(self.onUserFileBtnClick)
        self.execute_btn.clicked.connect(self.onExecuteBtnClick)
        self.select_destination_btn.clicked.connect(self.onDestinationFileBtnClick)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.db_file_label.setText(_translate("MainWindow", "Database File Path"))
        self.user_input_file_label.setText(_translate("MainWindow", "User Input File Path"))
        self.user_file_spiner.setToolTip(_translate("MainWindow", "Select Sheet Number By Default the selected sheet is zero means sheet 1"))
        self.execute_btn.setToolTip(_translate("MainWindow", "Execute Control"))
        self.execute_btn.setText(_translate("MainWindow", "GO"))
        self.sheet_number_label_2.setText(_translate("MainWindow", "Select Sheet Number"))
        self.select_destination_btn.setToolTip(_translate("MainWindow", "Click To Select Output File Destination Directory"))
        self.select_destination_btn.setText(_translate("MainWindow", "Select Destination Path"))
        self.select_user_file_btn.setToolTip(_translate("MainWindow", "Click To Select User Input File"))
        self.select_user_file_btn.setText(_translate("MainWindow", "Select User Input File"))
        self.sheet_number_label_1.setText(_translate("MainWindow", "Select Sheet Number"))


        self.db_sheet_spiner.setToolTip(_translate("MainWindow", "Select Sheet Number By Default the selected sheet is zero means sheet 1"))
        self.select_db_file_btn.setToolTip(_translate("MainWindow", "Click to Select Database File"))
        self.select_db_file_btn.setText(_translate("MainWindow", "Select Database File"))
        self.menuHello.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.about_application.setText(_translate("MainWindow", "About Application"))
        self.about_developer.setText(_translate("MainWindow", "About Developer"))



    def onDBFileBtnClick(self):
        print('DB File Btn Click')
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Database File", "", "DB Files (*.xlsx *.xls )") # Ask for file
        if fileName: # If the user gives a file
            print(fileName)
            self.db_file_label.setText(fileName)
            self.db_file_path = fileName
    def onUserFileBtnClick(self):
        print('User File Btn Click')
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select User Input File", "", "DB Files (*.xlsx *.xls )") # Ask for file
        if fileName: # If the user gives a file
            print(fileName)
            self.user_input_file_label.setText(fileName)
            self.user_file_path = fileName


    def onDestinationFileBtnClick(self):
        print('Destination File Btn Click')
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None) # Ask for file
        if fileName:
            print(fileName)
            self.destination_file_path = fileName



        

    def onExecuteBtnClick(self):
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
            self.movie = QtGui.QMovie("ajax-loader2.gif")
            self.user_input_file_label.setMovie(self.movie)
            self.db_file_label.setMovie(self.movie)
            self.movie.start()
            self.execute_btn.setDisabled(True)

            logger.info("Executing Process: db_file={dbfp}, sheet_no = {usn}, user_file={ufp}, sheet_no={dbsn}, dest_path={destfp}".format(ufp=self.user_file_path,usn=user_sheet_no,dbfp=self.db_file_path,dbsn=db_sheet_no,destfp=self.destination_file_path))
            import threading
            thread =threading.Thread(target=self.script,args=(self.user_file_path,user_sheet_no,self.db_file_path,db_sheet_no,self.destination_file_path))
            # self.script(ufp=self.user_file_path,usn=user_sheet_no,dbfp=self.db_file_path,dbsn=db_sheet_no,destfp=self.destination_file_path)
            thread.start()




    def script(self,ufp,usn,dbfp,dbsn,destfp):
        def df_to_excel(df, path, sheet_name='Sheet 1'):
            path = path +'/output.xlsx'
            from pyexcelerate import Workbook
            logger.debug("Excel Export Started.")
            data = [df.columns.tolist(), ] + df.values.tolist()
            wb = Workbook()
            wb.new_sheet(sheet_name, data=data)
            wb.save(path)
            logger.info("Save Completes!")
        def df_to_scv(df, path):
            path = path +'/output.csv'
            logger.debug("CSV Export Started.")
            df.to_csv(path, chunksize=1000,header=False,index=False)
            logger.info("Save Completes!")

        try:

            u_inpt_file_path = ufp
            u_file_sheet_no = usn - 1

            database_file_path = dbfp
            db_file_sheet_no = dbsn - 1

            if u_file_sheet_no < 0:
                u_file_sheet_no = 0
            if db_file_sheet_no < 0:
                db_file_sheet_no = 0



            logger.debug("Reading Database File.")
            databaseFrame = pd.read_excel(database_file_path, sheet_name=u_file_sheet_no,header=None)

            logger.debug("Reading User Input File.")
            userInputFrame = pd.read_excel(u_inpt_file_path, sheet_name=db_file_sheet_no,header=None)

            #getting columns size...
            logger.debug("Getting Columns sizes.")
            db_col_size = databaseFrame.columns.size
            us_col_size = userInputFrame.columns.size


            columns_names = ['A','B','C','D','E','F','G','H']
            #---------Assigning the columns Names--------------
            logger.debug("Assigning Columns Names.")
            databaseFrame.columns = columns_names[:db_col_size]
            userInputFrame.columns = columns_names[:us_col_size]


            if us_col_size == 2:#------------------------------------------------------------------------------
                logger.info("Executing Case 2: user file with 2 columns")
                #droping the column from databaseFrame
                print('Input data has 2 columns')

                logger.debug("Copying the Columns")
                droped_column_copy_C = pd.Series(databaseFrame['C'])
                droped_column_copy_D = pd.Series(databaseFrame['D'])
                droped_column_copy_E = pd.Series(databaseFrame['E'])

                logger.debug("Dropping the Unused Columns")
                databaseFrame = databaseFrame.drop(['C','D','E'], axis=1)

                logger.debug("Combining the user input columns in format - - - -.")
                str_list_userinpt = pd.Series(userInputFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))
                logger.debug("Combining the database columns.")
                str_list_database = pd.Series(databaseFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))

                #Now rejoining the dropped column and combined column list.
                logger.debug("Rejoining the Dropped Columns.")
                databaseFrame['C'] = droped_column_copy_C
                databaseFrame['D'] = droped_column_copy_D
                databaseFrame['E'] = droped_column_copy_E

                #joining the str_list to the dataframes.
                logger.debug("Joining the str_columns to User DataFrame")
                userInputFrame['str_list'] = str_list_userinpt
                logger.debug("Joining the str_columns to DB DataFrame")
                databaseFrame['str_list'] = str_list_database

                print('User Input: ')
                print(str_list_userinpt)
                print('Database: ')
                print(str_list_database)

                logger.debug("Counting the Similar Columns.")
                dictionary = {}
                rep_list = []
                for item in str_list_database:
                   num = -1
                   if item not in dictionary:
                      dictionary[item] = num =userInputFrame['str_list'].where(userInputFrame['str_list'] == item).count()
                   else:
                      num  = dictionary[item]
                   if num == 0:
                      num = num + 1
                   s = str(num) + ' times'
                   rep_list.append(s)

                logger.debug("Counting Completes Now getting the series of repeted list.")
                rep_list = pd.Series(rep_list)

                logger.debug("Dropping the str_list columnn form user Frame")
                userInputFrame = userInputFrame.drop('str_list', axis=1)

                logger.debug("Adding the count colunn to the Database Frame")
                databaseFrame['count'] = rep_list

                #Dropping the all database Columns list...
                logger.debug("Dropping all the columns to of the Database Frame except str_list and count")
                databaseFrame = databaseFrame.drop(columns_names[:db_col_size],axis = 1)


                #Saving back to excel file
                destfp = destfp +'/output.xlsx'

                logger.debug("Preparing the Writer")
                # writer = pd.ExcelWriter(destfp)
                # databaseFrame.to_excel(writer, 'Sheet1', header=False, index=False)
                # writer.save()

                logger.debug("Preparing the Writer For Saving File")

                output_file_full_path = self.destination_file_path
                # df_to_excel(databaseFrame,output_file_full_path)
                df_to_scv(databaseFrame,output_file_full_path)


                self.user_input_file_label.setText(self.user_file_path)
                self.db_file_label.setText(self.db_file_path)

                self.execute_btn.setEnabled(True)


                # # show Message Dialog to user.
                # mb = QtWidgets.QMessageBox()
                # mb.setIcon(mb.Information)
                # mb.setWindowTitle("MESSAGE WINDOW")
                # message = "File Saved To: " + destfp
                # mb.setInformativeText(message)
                # mb.setStandardButtons(mb.Ok)
                # mb.exec_()


    #--------------------------------------------------------------------------------------------------
            elif us_col_size == 3:#------------------------------------------------------------------------------
                logger.info("Executing Case 3: user file with 3 columns")

                print('Input data has 3 columns')
                    #droping the column from databaseFrame
                logger.debug("Copying the Columns")
                droped_column_copy_D = pd.Series(databaseFrame['D'])
                droped_column_copy_E = pd.Series(databaseFrame['E'])

                logger.debug("Dropping the Unused Columns")
                databaseFrame = databaseFrame.drop(['D','E'], axis=1)

                logger.debug("Combining the user input columns in format - - - -.")
                str_list_userinpt = pd.Series(userInputFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))
                str_list_database = pd.Series(databaseFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))

                #Now rejoining the dropped column and combined column list.
                databaseFrame['D'] = droped_column_copy_D
                databaseFrame['E'] = droped_column_copy_E

                #joining the str_list to the dataframes.
                userInputFrame['str_list'] = str_list_userinpt
                databaseFrame['str_list'] = str_list_database

                print('User Input: ')
                print(str_list_userinpt)
                print('Database: ')
                print(str_list_database)

                logger.debug("Counting the Similar Columns.")
                dictionary = {}
                rep_list = []
                for item in str_list_database:
                   num = -1
                   if item not in dictionary:
                      dictionary[item] = num =userInputFrame['str_list'].where(userInputFrame['str_list'] == item).count()
                   else:
                      num  = dictionary[item]
                   if num == 0:
                      num = num + 1
                   s = str(num) + ' times'
                   rep_list.append(s)

                rep_list = pd.Series(rep_list)

                userInputFrame = userInputFrame.drop('str_list', axis=1)

                logger.debug("Adding the count colunn to the Database Frame")
                databaseFrame['count'] = rep_list

                #Dropping the all database Columns list...
                logger.debug("Dropping all the columns to of the Database Frame except str_list and count")
                databaseFrame = databaseFrame.drop(columns_names[:db_col_size],axis = 1)


                # #Saving back to excel file
                # destfp = destfp +'/output.xlsx'
                # writer = pd.ExcelWriter(destfp)
                # databaseFrame.to_excel(writer, 'Sheet1', header=False, index=False)
                # writer.save()

                logger.debug("Preparing the Writer For Saving File")
                output_file_full_path = self.destination_file_path
                # df_to_excel(databaseFrame,output_file_full_path)
                df_to_scv(databaseFrame,output_file_full_path)

                # mb = QtWidgets.QMessageBox()
                # mb.setIcon(mb.Information)
                # mb.setWindowTitle("MESSAGE WINDOW")
                # message = "File Saved To: " + destfp
                # mb.setInformativeText(message)
                # mb.setStandardButtons(mb.Ok)
                # mb.exec()

    #--------------------------------------------------------------------------------------------------
            elif us_col_size == 4:#------------------------------------------------------------------------------
                logger.info("Executing Case 4: user file with 4 columns")
                print('Input data has 4 columns')
                    #droping the column from databaseFrame
                logger.debug("Copying the Columns")
                logger.debug("Dropping the Unused Columns")
                droped_column_copy_E = pd.Series(databaseFrame['E'])

                databaseFrame = databaseFrame.drop('E', axis=1)

                logger.debug("Combining the user input columns in format - - - -.")
                str_list_userinpt = pd.Series(userInputFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))
                str_list_database = pd.Series(databaseFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))

                #Now rejoining the dropped column and combined column list.
                databaseFrame['E'] = droped_column_copy_E

                #joining the str_list to the dataframes.
                userInputFrame['str_list'] = str_list_userinpt
                databaseFrame['str_list'] = str_list_database

                print('User Input: ')
                print(str_list_userinpt)
                print('Database: ')
                print(str_list_database)

                logger.debug("Counting the Similar Columns.")
                dictionary = {}
                rep_list = []
                for item in str_list_database:
                   num = -1
                   if item not in dictionary:
                      dictionary[item] = num =userInputFrame['str_list'].where(userInputFrame['str_list'] == item).count()
                   else:
                      num  = dictionary[item]
                   if num == 0:
                      num = num + 1
                   s = str(num) + ' times'
                   rep_list.append(s)

                rep_list = pd.Series(rep_list)

                userInputFrame = userInputFrame.drop('str_list', axis=1)

                logger.debug("Adding the count colunn to the Database Frame")
                databaseFrame['count'] = rep_list

                #Dropping the all database Columns list...
                logger.debug("Dropping all the columns to of the Database Frame except str_list and count")
                databaseFrame = databaseFrame.drop(columns_names[:db_col_size],axis = 1)


                # #Saving back to excel file
                # destfp = destfp +'/output.xlsx'
                # writer = pd.ExcelWriter(destfp)
                # databaseFrame.to_excel(writer, 'Sheet1', header=False, index=False)
                # writer.save()

                logger.debug("Preparing the Writer For Saving File")
                output_file_full_path = self.destination_file_path
                # df_to_excel(databaseFrame,output_file_full_path)
                df_to_scv(databaseFrame,output_file_full_path)


                # mb = QtWidgets.QMessageBox()
                # mb.setIcon(mb.Information)
                # mb.setWindowTitle("MESSAGE WINDOW")
                # message = "File Saved To: " + destfp
                # mb.setInformativeText(message)
                # mb.setStandardButtons(mb.Ok)
                # mb.exec()


    #--------------------------------------------------------------------------------------------------
            elif us_col_size == 5:#------------------------------------------------------------------------------
                logger.info("Executing Case 5: user file with 5 columns")
                print('Input data has 5 columns')

                logger.debug("Combining the user input columns in format - - - -.")
                str_list_userinpt = pd.Series(userInputFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))
                str_list_database = pd.Series(databaseFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))

                #joining the str_list to the dataframes.
                userInputFrame['str_list'] = str_list_userinpt
                databaseFrame['str_list'] = str_list_database

                print('User Input: ')
                print(str_list_userinpt)
                print('Database: ')
                print(str_list_database)


                logger.debug("Counting the Similar Columns.")
                dictionary = {}
                rep_list = []
                for item in str_list_database:
                   num = -1
                   if item not in dictionary:
                      dictionary[item] = num =userInputFrame['str_list'].where(userInputFrame['str_list'] == item).count()
                   else:
                      num  = dictionary[item]
                   if num == 0:
                      num = num + 1
                   s = str(num) + ' times'
                   rep_list.append(s)

                rep_list = pd.Series(rep_list)

                userInputFrame = userInputFrame.drop('str_list', axis=1)

                logger.debug("Adding the count colunn to the Database Frame")
                databaseFrame['count'] = rep_list

                #Dropping the all database Columns list...
                logger.debug("Dropping all the columns to of the Database Frame except str_list and count")
                databaseFrame = databaseFrame.drop(columns_names[:db_col_size],axis = 1)

                # #Saving back to excel file
                # destfp = destfp +'/output.xlsx'
                # writer = pd.ExcelWriter(destfp)
                # databaseFrame.to_excel(writer, 'Sheet1', header=False, index=False)
                # writer.save()

                logger.debug("Preparing the Writer For Saving File")
                output_file_full_path = self.destination_file_path
                # df_to_excel(databaseFrame,output_file_full_path)
                df_to_scv(databaseFrame,output_file_full_path)


                # mb = QtWidgets.QMessageBox()
                # mb.setIcon(mb.Information)
                # mb.setWindowTitle("MESSAGE WINDOW")
                # message = "File Saved To: " + destfp
                # mb.setInformativeText(message)
                # mb.setStandardButtons(mb.Ok)
                # mb.exec()

    #--------------------------------------------------------------------------------------------------
            elif us_col_size == 6:#-----------------------------------------------------------------------------------
                print('Input data has 6 columns')
                logger.info("Executing Case 6: user file with 6 columns")
                #drop the last column of the dataframe.
                logger.debug("Copying the Columns")
                logger.debug("Dropping the Unused Columns")
                droped_column_copy = pd.Series(userInputFrame[userInputFrame.columns[-1]])
                userInputFrame = userInputFrame.drop(userInputFrame.columns[-1], axis=1)


                logger.debug("Combining the user input columns in format - - - -.")
                str_list_userinpt = pd.Series(userInputFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))
                str_list_database = pd.Series(databaseFrame.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))

                #Now rejoining the dropped column and combined column list.
                userInputFrame['F'] = droped_column_copy
                userInputFrame['str_list'] = str_list_userinpt
                databaseFrame['str_list'] = str_list_database

                print('User Input: ')
                print(str_list_userinpt)
                print('Database: ')
                print(str_list_database)

                logger.debug("Counting the Similar Columns.")
                dictionary = {}
                rep_list = []
                for item in str_list_database:
                   num = -1
                   if item not in dictionary:
                      dictionary[item] = num =userInputFrame['str_list'].where(userInputFrame['str_list'] == item).count()
                   else:
                      num  = dictionary[item]
                   if num == 0:
                      num = num + 1
                   s = str(num) + ' times'
                   rep_list.append(s)

                rep_list = pd.Series(rep_list)

                userInputFrame = userInputFrame.drop('str_list', axis=1)

                logger.debug("Adding the count colunn to the Database Frame")
                databaseFrame['count'] = rep_list

                #Dropping the all database Columns list...
                logger.debug("Dropping all the columns to of the Database Frame except str_list and count")
                databaseFrame = databaseFrame.drop(columns_names[:db_col_size],axis = 1)


                #Saving back to excel file
                # destfp = destfp +'/output.xlsx'
                # writer = pd.ExcelWriter(destfp)
                # databaseFrame.to_excel(writer, 'Sheet1', header=False, index=False)
                # writer.save()

                logger.debug("Preparing the Writer For Saving File")
                output_file_full_path = self.destination_file_path
                # df_to_excel(databaseFrame,output_file_full_path)
                df_to_scv(databaseFrame,output_file_full_path)


                # mb = QtWidgets.QMessageBox()
                # mb.setIcon(mb.Information)
                # mb.setWindowTitle("MESSAGE WINDOW")
                # message = "File Saved To: " + destfp
                # mb.setInformativeText(message)
                # mb.setStandardButtons(mb.Ok)
                # mb.exec()

        except Exception as e:
            logger.error(traceback.format_exc())
            logger.error(e.__traceback__)
            pass
#-------------------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

