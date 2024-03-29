'''

Download Cricket Data

'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib3
import csv
import sys
import time
import os
import unicodedata
# from urlparse3 import urlparse
import  urllib.request, urllib.parse, urllib.error 
# from beautifulsoup4 import BeautifulSoup, SoupStrainer
# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests
# import beautifulsoup4 

BASE_URL = 'http://www.espncricinfo.com'

odi = 'http://search.espncricinfo.com/ci/content/match/search.html?search=odi;all=1;page='  
first_class = 'http://search.espncricinfo.com/ci/content/match/search.html?search=first%20class;all=1;page='  
test = 'http://search.espncricinfo.com/ci/content/match/search.html?search=test;all=1;page=' 
t20i = 'http://search.espncricinfo.com/ci/content/match/search.html?search=t20i;all=1;page='  
t20 = 'http://search.espncricinfo.com/ci/content/match/search.html?search=t20;all=1;page=' 
list_a = 'http://search.espncricinfo.com/ci/content/match/search.html?search=list%20a;all=1;page='  
    

if not os.path.exists('./espncricinfo-fc'):
    os.mkdir('./espncricinfo-fc')


def cric_scrape():

    for i in range(1, 1):

        MY_URL = odi + str(i) 
        print("\n my URL - {}".format(MY_URL))
        http = urllib3.PoolManager()
        response = http.request('GET', MY_URL)
        soupy = BeautifulSoup(response.data , "html.parser")

        # print(soupy)
        # exit()

        time.sleep(1)
        for new_host in soupy.findAll('a', {'class' : 'srchPlyrNmTxt'}):
            try:
                new_host = new_host['href']
                # print("{} - {} ".format(new_host , type(new_host)))
            except:
                continue

            FINAL_URL = urllib.parse.urlparse(BASE_URL , new_host)
            odiurl = FINAL_URL.geturl()
            new_host1 = unicodedata.normalize('NFKD', new_host).encode('ascii','ignore')
            new_host1 = str(new_host1)
            
            print("New host is {}".format(new_host  ))
            print( str.split(new_host, "/")[4])
            print("+++++++++")

            http2 = urllib3.PoolManager()
            response2 = http.request('GET', odiurl)
            # html = urllib3.urlopen(odiurl).read()
            if response2.data:
                with open('espncricinfo-fc/{0!s}'.format(str.split(new_host, "/")[4]), "wb") as f:
                    f.write(response2.data)




        


#######################
#

import os

INPUT_FOLDER = ["espncricinfo-t20","espncricinfo-lista","espncricinfo-fc","espncricinfo-odi","espncricinfo-t20i","espncricinfo-test"]
FINAL_OUTPUT_FILE = "final_output.csv"

HEADER = "url, team1, team2, win_toss, bat_or_bowl, outcome, win_game, date, day_n_night, ground, rain, duckworth_lewis, match_id, type_of_match"

def removeEndLineCharacter(mystr):
    if mystr.find("\n"):
        return mystr[:-1]
    
def removeDoubleQuote(myStr):
    return myStr.replace("\"", "").strip();

def removeDivInText(myStr, divs):
    for div in divs:
        myStr = myStr.replace(div,"")
    return myStr

def refineHTMLToText(myStr):
    for div in USELESS_TAGS:
        myStr = myStr.replace(div,"")
    myStr = myStr.replace("  "," ").strip()
    return myStr


def findWithPattern(mystr, startPattern, endPattern):

    x = mystr.find(startPattern)
    if x==-1:
        return "",mystr
    mystr = mystr[x + len(startPattern):]
    y = mystr.find(endPattern)
    if y==-1:
        return "",mystr
    return mystr[:y], mystr[y+len(endPattern):]


def extractDataFrom(data):
    # Extract 2 teams name
    team1, tmp = findWithPattern(data,'class="teamLink">','</a>')
    team2, tmp = findWithPattern(tmp,'class="teamLink">','</a>')

    # Extract win_toss
    toss_div, tmp = findWithPattern(data,"Toss  - <span class='normal'>","</span>")
    if toss_div.find(team1)>-1:
        win_toss = team1
    elif toss_div.find(team2)>-1:
        win_toss = team2
    else:
        win_toss = "" #!!!

    # Extract bat_or_bowl
    if toss_div.find("bat")>-1:
        bat_or_bowl = "bat"
    elif toss_div.find("field")>-1:
        bat_or_bowl = "bowl"
    else:
        bat_or_bowl = "" #!!!

    # Extract outcome and the winning team if any
    outcome, tmp = findWithPattern(data, '<div class="innings-requirement">','</div>')
    #print outcome
    k = outcome.find("won")
    win_game = ""
    if k>-1 and outcome.find("drawn")==-1:
        if outcome[:k].find(team1)>-1:
            win_game = team1
        elif outcome[:k].find(team2)>-1:
            win_game = team2
        else:
            wingame = "" #!!!

    # Extract the date
    titleDiv, tmp = findWithPattern(data, '<title>','</title>')
    date = "".join(titleDiv.split("|")[0].split(",")[-2:])

    # Extract day_n_night
    day_n_night = int(data.find("day/night")>-1)

    # Extract ground
    ground,tmp = findWithPattern(data,'title="view the ground profile for','"')
            
    # Extract rain
    matchNotesDiv,tmp = findWithPattern(data, ">Match Notes<","</div>")
    rain = int(matchNotesDiv.find(" rain")>-1 or matchNotesDiv.find("Rain")>-1)

    # Extract duckworth_lewis
    duckworth_lewis = int(data.find("D/L method")>-1)
    
    """
    id1, tmp = findWithPattern(data,'Test no. ','<')
    id2, tmp = findWithPattern(data,'ODI no. ','<')
    id3, tmp = findWithPattern(data,'>List A ','<')
    id4, tmp = findWithPattern(data,'unofficial ODI ','<')
    match_id = "NA"
    for mid in [id1,id2,id3,id4]:
        if mid:
            match_id = mid
            break
    """
    # Extract match_id
    match_id, tmp = findWithPattern(data,'data-matchId="','"')

    # Return result
    return  team1, team2, win_toss, bat_or_bowl, outcome, win_game, date, day_n_night, ground, rain, duckworth_lewis, match_id
            


def cric_proc():
    ##################################START PROCESSING DATA#########################################
    outputFile = open (FINAL_OUTPUT_FILE, "w")
    outputFile.write(HEADER + "\n")
    for folder in INPUT_FOLDER:
        print("---PROCESSING FOLDER {0!s}---".format(folder) )
        counter = 0

        folder = "./" + folder
        try:
            listFiles = os.listdir(folder)
            print(listFiles)


            for url in listFiles:
                data = open(folder + "/" + url).read()
                print(data)
                print("+++++++++++++++++++++++")
                team1, team2, win_toss, bat_or_bowl, outcome, win_game, date, day_n_night, ground, rain, duckworth_lewis, match_id = extractDataFrom(data)
                url_new = folder + "/" + url
                type_of_match = folder.split("-")[-1].upper()
                rowStr = '"{0!s}","{1!s}","{2!s}","{3!s}","{4!s}","{5!s}","{6!s}","{7!s}","{8!s}","{9!s}","{10!s}","{11!s}","{12!s}","{13!s}"\n'.format(url_new, team1, team2, win_toss, bat_or_bowl, outcome, win_game, date, day_n_night, ground, rain, duckworth_lewis, match_id, type_of_match)
                outputFile.write(rowStr)
                counter = counter + 1
                if counter%1000==0:
                    print("   + Processing file {0:d}0th".format(counter/10) )
            
        except:
            print("no dir found")
            continue

    outputFile.close()

    ##################################FINISHED#########################################
    print("DONE. Wrote output to {0!s}".format(FINAL_OUTPUT_FILE) )
        