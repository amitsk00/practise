import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# import tkinter as tk
import configparser
import os 
from datetime import datetime
import sys
import fnmatch

# matplotlib.use('TkAgg')


myConfig = configparser.ConfigParser()
myConfig.read("config.ini")

flagDebug = myConfig["SETTINGS"]["debug"]
filePath =  myConfig["SETTINGS"]["filePath"]
fileName =  myConfig["SETTINGS"]["fileName"]

dt_format = "%Y-%m-%d %H:%M:%S"

def summaryDf(dfCsv):
    print("----------------------------------------")
    print("High level summary")


    t = dfCsv.pivot_table(index = 'YearMonth' , values = 'Amount' 
                          , aggfunc = np.sum , margins = True  , fill_value = 0 ) 
    for c in t.columns:
        t[c] = t[c].apply('{:,.2f}'.format)
    print(t)

    print("----------------------------------------")


    t = dfCsv.pivot_table(index = 'Weekday' , values = 'Amount' 
                          , aggfunc = np.sum , margins = True , fill_value = 0 ) 
    for c in t.columns:
        t[c] = t[c].apply('{:,.2f}'.format)
    print(t)
    print("----------------------------------------")


    t = dfCsv.pivot_table(index = 'WeekNum' , values = 'Amount' 
                          , aggfunc = np.sum , margins = True  , fill_value = 0 ) 
    for c in t.columns:
        t[c] = t[c].apply('{:,.2f}'.format)
    print(t)

    print("----------------------------------------")
    print("----------------------------------------")
    print("########################################")
    print("----------------------------------------")
    print("----------------------------------------")

    t = dfCsv.pivot_table(index = 'Account' , columns = 'YearMonth' , values = 'Amount' 
                          , aggfunc = np.sum , margins = True  , fill_value = 0 )
    for c in t.columns:
        t[c].astype('float64')
        # if "All" in c:
        #     for f in c:
        #         break
        #     c_new = ((f , "Percentage"))
        #     t[c_new] = t[c].cumsum()
        t[c] = t[c].apply('{:,.2f}'.format)   

    print(t)
    print("----------------------------------------")
    

    t = dfCsv.pivot_table(index = 'Category Group Name' , columns = "YearMonth" , values = 'Amount'  
                          , aggfunc = [np.sum  ] , margins = True  , fill_value = 0 )
    for c in t.columns:
        t[c].astype('float64')
        # if "All" in c:
        #     for f in c:
        #         break
        #     c_new = ((f , "Percentage"))
        #     t[c_new] = t[c].cumsum()
        t[c] = t[c].apply('{:,.2f}'.format)   

    print(t)
    print("----------------------------------------")


    t = dfCsv.pivot_table(index = 'Category' , columns = "YearMonth" , values = 'Amount'  
                          , aggfunc = [np.sum  ] , margins = True , fill_value = 0 )
    
    for c in t.columns:
        t[c].astype('float64')
        # if "All" in c:
        #     for f in c:
        #         break
        #     c_new = ((f , "Percentage"))
        #     t[c_new] = t[c].cumsum()
        t[c] = t[c].apply('{:,.2f}'.format)   

    print(t)
    print("----------------------------------------")




def  plotDf(dfCsv):
    print("plotting part")

    # %matplotlib inline
    plt.figure(figsize=(10,8))
    ax = dfCsv.plot(xticks = dfCsv.index , ylabel = 'Amounts', kind = 'bar')
    dfCsv.plot(x = 'Category' , ax = ax , kind = 'bar')
    plt.show()    



def processDf(dfCsv):
    if flagDebug:
        print("processing CSV DF")

    dfCsv["Weekday"] = dfCsv.apply(lambda x : datetime.strptime(x.Date , dt_format).strftime("%A")  , axis = 1)
    dfCsv["YearMonth"] = dfCsv.apply(lambda x : datetime.strptime(x.Date , dt_format).strftime("%Y-%m")  , axis = 1)
    dfCsv["Weekend"] = dfCsv.apply(lambda x :  'WeekEnd' if x["Weekday"] in ('Saturday','Sunday') else 'WeekDay' , axis = 1)
    # dfCsv["WeekNum"] = dfCsv.apply(lambda x : datetime.strptime(x.Date , dt_format).date().dt.week  , axis = 1)
    dfCsv["WeekNum"] = dfCsv.apply(lambda x : datetime.strptime(x.Date , dt_format).strftime("%U")  , axis = 1)
    # print(dfCsv.columns )

    dfCsv["Amount"].fillna(0 , inplace = True)
    # print(dfCsv)

    # dfCsv.to_csv("test1.csv")
    summaryDf(dfCsv)
    # plotDf(dfCsv)
    



def getFiles():
    for root, dirnames, filenames in os.walk(filePath):        
        for filename in fnmatch.filter(filenames, 'transactions_list_*csv'):
            yield os.path.join(root, filename)    

def main():
    if flagDebug:
        print("starting main")

    dfExp = pd.DataFrame()

    for myFile in getFiles():
        # print(myFile)

        dfTmp = pd.read_csv(myFile)    
        dfTmp = dfTmp[ dfTmp['Type'] == 'Expense' ]    
        dfTmp = dfTmp[ dfTmp['Category'] != 'EMI' ]    
        dfTmp = dfTmp.round(2)
        dfExp = pd.concat([dfExp , dfTmp])
        # print(" {} - {} ---- {} ".format(myFile , dfTmp.shape , dfExp.shape ))
        
    # dfExp.to_csv("mydata.csv")
        
    processDf(dfExp)


    # myFile = filePath + fileName
    # print(myFile)

    # if os.path.isdir(filePath):
    #     pass
    # else:
    #     print("path doesnt exist")
    #     sys.exit(9)

    # if os.path.isfile(myFile):
    #     pass
    # else:
    #     print("file is missing")
    #     sys.exit(9)



    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    


if __name__ == "__main__":
    main()