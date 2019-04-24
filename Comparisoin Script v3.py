import pandas as pd
import numpy as np
import datetime


def readExcelSheet(file_path, sheet_no):
    df = pd.read_excel(file_path, sheet_name=sheet_no, header=None)
    return df

def writeToExcel(dest_path, dataframe):
    now = datetime.datetime.now()
    date = now.date()
    time = now.time()
    dt = str(date.year) + str(date.month) + str(date.day) + str(time.hour) + str(time.minute) + str(time.second) + str(time.microsecond)

    f_name = 'output' + dt + '.xlsx'
    path = dest_path + '/' + f_name
    writer = pd.ExcelWriter(path)
    dataframe.to_excel(writer, 'Sheet1', header=False, index=False)
    writer.save()

def writeToCsv(dest_path, dataframe):
    now = datetime.datetime.now()
    date = now.date()
    time = now.time()
    dt = str(date.year) + str(date.month) + str(date.day) + str(time.hour) + str(time.minute) + str(time.second) + str(time.microsecond)

    f_name = 'output' + dt + '.csv'
    path = dest_path + '/' + f_name
    logger.debug("CSV Export Started.")
    df.to_csv(path, chunksize=1000, header=False, index=False)


def equalTheColumns(X, Y):
    x_col_size = X.columns.size
    y_col_size = Y.columns.size

    if x_col_size < y_col_size:
        Y = Y.iloc[:, :x_col_size]
    elif x_col_size > y_col_size:
        X = X.iloc[:, :y_col_size]
    else:
        pass

    return (X, Y)


def convertToStringColumn(X, Y):
    x_str = pd.Series(X.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))
    y_str = pd.Series(Y.apply(lambda row: '-'.join([str(int(val)) for val in row]), axis=1))

    return (x_str, y_str)

def makeDataFrameForExport(str_series, count_series):
    d_frame = pd.DataFrame(str_series, columns=['Dashed Column'])
    d_frame['Count Column'] = count_series
    return d_frame



def preformCalculations(X, Y):
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

def main():
    X = readExcelSheet('C:/Users/Bilal Bhatti/Desktop/Excel Files/6 Number Database.xlsx', sheet_no=0)
    Y = readExcelSheet('C:/Users/Bilal Bhatti/Desktop/Excel Files/4 Number Database.xlsx', sheet_no=0)
    X, Y = equalTheColumns(X, Y)
    str_x, str_y = convertToStringColumn(X, Y)
    count_series = preformCalculations(str_x, str_y)
    export_df = makeDataFrameForExport(str_x, count_series)
    writeToExcel('C:/Users/Bilal Bhatti/Desktop/Excel Files', export_df)

    def onSelectDestinationDirBtnClick(self):
        logger.info("Select Destination Button Clicked.")

        print('Select Destinationg Btn Clicked')
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None) # Ask for file
        if fileName:
            print(fileName)
            self.destination_file_path = fileName

if __name__ == '__main__':
    main()


