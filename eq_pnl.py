
import pandas as pd
import numpy as np 
import os 
from datetime import date 
from pyxirr import xirr 

import warnings
warnings.filterwarnings('ignore', category=FutureWarning )
# from pandas.core.common import SettingWithCopyWarning
from pandas.errors import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)



filePath = "."
fileNameEq = "eq_data.csv"
fileNameEqFull = filePath + "/" + fileNameEq

####################
# 
####################
def processEqCsv():
    # print("Inside processEqCsv")


    colsTypeEq = {
        "Scrip" : "str" ,
        "Qty" : "int" ,
        "Price" :"float" ,
        "days" : "int" ,
        "gain" : "float" ,
        "Total" : "float",
        "Type" : "str"
    }
    dfEq = pd.DataFrame()
    
    dtToday = date.today()

    dfEq = pd.read_csv(fileNameEqFull , header=0)
    dfEq["days"] = dfEq["days"].fillna(0)
    dfEq["gain"] = dfEq["gain"].fillna(0)
    dfEq["Type"] = dfEq["Type"].str.upper()
    dfEq["Date"] = np.where(dfEq["Type"] == "CURRENT" , dtToday , dfEq["Date"] )
    dfEq["Qty"] = np.where(dfEq["Type"] == "CURRENT" , 0 , dfEq["Qty"] )
    dfEq["Total"] = dfEq["Qty"] * dfEq["Price"]
    dfEq["Qty"] = np.where(dfEq["Type"] == "SELL" , (dfEq["Qty"] * -1) , dfEq["Qty"] )
    dfEq["Total"] = np.where(dfEq["Type"] == "BUY" , (dfEq["Total"] * -1) , dfEq["Total"] )
    dfEq = dfEq.astype(colsTypeEq)
    dfEq['Date'] = pd.to_datetime(dfEq['Date'] ) 

    # dfTmp = dfEq["Date"]
    # ste1 = set(dfTmp)
    # print(ste1)


    # dfEq['Date'] = pd.to_datetime(dfEq['Date'], format='%y%m%d') 
    
    # print(dfEq)

    # print(dfEq.describe)
    # print("=================================================")
    # print(dfEq.dtypes)
    # print("=================================================")

    nameEq = dfEq["Scrip"]
    nameEqSet = set(nameEq)
    
    
    # for str in nameEqSet:
    #     print("{} - {}".format(str , type(str)))
    #     if pd.isna(str):
    #         print("X")
    # exit()

    print("-------------------------------------------------------")
    for currEqName in nameEqSet:
        print("\n\n          Now processing for {}".format(currEqName))
        if pd.isna(currEqName):
            continue
        else:

            dfXirrData = dfEq[dfEq['Scrip'] == currEqName]
            # print(dfXirrData)
            currQty = dfXirrData["Qty"].sum()

            if currQty < 0:
                print("Current Quantity can not be negative ... check the data, skipping to process {}".format(currEqName))
                continue 

            dfTmp = dfXirrData[dfXirrData['Type'] == 'CURRENT'].reset_index()
            currDate = dfTmp.loc[0 ,'Date']
            currValue = dfTmp.loc[0 , 'Price'] 
            # currValue = currValue.replace(",","")
            currValue = float(currValue) * currQty
            dfXirrData["Total"] = np.where(dfXirrData["Type"] == "CURRENT" , currValue , dfXirrData["Total"] )
            dfXirrData["Qty"] = np.where(dfXirrData["Type"] == "CURRENT" , currQty , dfXirrData["Qty"] )

            buyCost = dfXirrData[ dfXirrData["Type"] == "BUY" ].sum()["Total"]
            sellCost = dfXirrData[ dfXirrData["Type"] != "BUY" ].sum()["Total"]

            # print("for {} - buy cost as {} and sell cost as {}".format(currEqName , buyCost , sellCost))            
            # print(dfXirrData)


            
            dfXirrData = dfXirrData[["Date","Total"]]
            # dfXirrData = dfXirrData.apply(lambda z : z.str.replace(",","") )
            # dictXirr = { 'Amount' : float }
            # dfXirrData = dfXirrData.astype(dictXirr)
            # dfXirrData["Date"] = pd.to_datetime(dfXirrData["Date"]  , dayfirst=True)

            

            # XIRR
            x = xirr(dfXirrData)

            # CAGR
            minDate = min(dfXirrData["Date"])
            maxDate = max(dfXirrData["Date"])
            diff = maxDate - minDate
            diff = diff.days
            diffYrs = diff / 365 

            # costValue = dfXirrData['Amount'].sum()
            # costValue = costValue - currValue
            # costValue = abs(costValue)

            buyCost = abs(buyCost)
            c = (sellCost - buyCost) / buyCost / diffYrs

            

            # print("   min {} max {} and diff {} ".format(minDate, maxDate, diffYrs ))

            print("{}~{}~{:.3f}~{:.3f}~{:.3f} ".format(currEqName , currDate.strftime('%Y-%m-%d') , currValue , x*100 , c*100)   )

    print("-------------------------------------------------------")

 
 
####################
# XYZ
####################

def main():
    # print("Inside main -11.7")

    processEqCsv()


if __name__ == "__main__":
    main()
