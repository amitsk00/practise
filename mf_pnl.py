
import pandas as pd
import os 
from datetime import date 
from pyxirr import xirr 

filePath = "./py_tools"
fileName = "mf_data.csv"
fileNameFull = filePath + "/" + fileName

####################
# 
####################
def processCsv():
    # print("Inside processCsv")

    dfMf = pd.DataFrame()

    dfMf = pd.read_csv(fileNameFull , header=0)
    # print(dfMf)

    nameMf = dfMf["Scrip"]
    nameMfSet = set(nameMf)
    # for str in nameMfSet:
    #     print("{} - {}".format(str , type(str)))
    #     if pd.isna(str):
    #         print("X")
    # exit()

    print("-------------------------------------------------------")
    for currMfName in nameMfSet:
        # print("\n\n          Now processing for {}".format(currMfName))
        if pd.isna(currMfName):
            continue
        else:

            dfXirrData = dfMf[dfMf['Scrip'] == currMfName]
            # print(dfXirrData)

            dfTmp = dfXirrData[dfXirrData['Type'] == 'Current'].reset_index()
            currDate = dfTmp.loc[0 ,'Date']
            currValue = dfTmp.loc[0 , 'Amount']
            currValue = currValue.replace(",","")
            currValue = float(currValue)

            dfXirrData = dfXirrData[["Date","Amount"]]
            dfXirrData = dfXirrData.apply(lambda z : z.str.replace(",","") )
            dictXirr = { 'Amount' : float }
            dfXirrData = dfXirrData.astype(dictXirr)
            dfXirrData["Date"] = pd.to_datetime(dfXirrData["Date"]  , dayfirst=True)

            
            # XIRR
            x = xirr(dfXirrData)

            # CAGR
            minDate = min(dfXirrData["Date"])
            maxDate = max(dfXirrData["Date"])
            diff = maxDate - minDate
            diff = diff.days
            diffYrs = diff / 365 

            costValue = dfXirrData['Amount'].sum()
            costValue = costValue - currValue
            costValue = abs(costValue)

            c = (currValue - costValue) / costValue / diffYrs

            

            # print("   min {} max {} and diff {} ".format(minDate, maxDate, diffYrs ))

            print("{}~{}~{:.3f}~{:.3f}~{:.3f} ".format(currMfName , currDate , currValue , x*100 , c*100)   )

    print("-------------------------------------------------------")

 
 
####################
# XYZ
####################

def main():
    # print("Inside main -11.7")

    processCsv()


if __name__ == "__main__":
    main()
