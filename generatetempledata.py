"""
Purpose : Google Connect is a utility to connect to the Google Search Engine.
Generate the csv data based on the search query given in the argument.
The demostrated program generate the datasheet in  a format in CSV.

Design and developed by :
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Lab : Nature Labs @ GCP
How to use
------------
python generatetempledata.py 

Contact 
--------
Kyndryl GCP Guild Moderator : Ramamurthy V 
Email           :  ramamurthy.valavandan@kyndryl.com
GCP Contact     : gcpguild@gmail.com
Date            : June 8 2022.
Contributors    : 42 key members from GCP Guild.
"""

import pandas as pd


basepath = "C:"
codepath="python"
function = "temples"
googlecsv = "googledata.csv"
N="\\"

googledata = ("{}{}{}{}{}{}{}".format(basepath,N, codepath, N, function, N, googlecsv))

data = pd.read_csv(googledata, header=None)

df = pd.read_csv(googledata, delimiter=',')
templeslist = [list(row) for row in df.values]

cities = ['Mumbai', 
'New Delhi', 
'Chennai', 
'Kolkata',
'Bengaluru',
'Hyderabad']

colheader = ['Temple Name', 
'State', 
'Description', 
'Location',
'Coordinates',
'Distance From Mumbai(Km)',
'Distance From NewDelhi(Km)', 
'Distance From Chennai(Km)', 
'Distance From Kolkata(Km)',
'Distance From Bengaluru(Km)',
'Distance From Hyderabad(Km)']


import pandas as pd

import re
import csv
import requests
from bs4 import BeautifulSoup

import bs4 as bs
import urllib.request

import numpy as np

# temple Name

flags = re.IGNORECASE

csvfile = "indiatemples.csv"
N="\\"

genfile = ("{}{}{}{}{}{}{}".format(basepath,N, codepath, N, function, N, csvfile))

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")


def googling(search):
    url = f"https://www.google.com/search?&q={search}"
    pi="\'Google Search for :  \' :"
    p = ("{} {}".format(pi,search))
    prt(p)
    #rint (url)
    req = requests.get(url)
    sor = BeautifulSoup(req.text, "html.parser")
    
    temp = sor.find("div", class_='BNeawe').text
    return temp

def addingtemples(templename,templelocation):
    
    pi="\'Temple name is searching in Google  \' :"
   
    p = ("{} {}".format(pi,templename))
    prt(p)
    temples_data.append(templename)

    search = "{}{}".format(
     templelocation, 
     " which state of india ?")
    templestate = googling(search)
    temples_data.append(templestate)


    search = "'{}, {}{}".format(templename,
    templelocation,
     " temple is famous for ")
    templedescription = googling(search)

    #templedescription = templedescription[:-10]
    templedescription = re.sub('[^A-Za-z0-9.,)()]+', ' ' , str(templedescription)).strip()
    temples_data.append(templedescription)


    temples_data.append(templelocation)

    search = "'Coordinates of {}".format(templelocation)
    templecoordinates = googling(search)
    templecoordinates = re.sub('[^0-9.,]+', '', templecoordinates)
    templecoordinates = ("{}{}{}".format("(", templecoordinates, ")"))

    temples_data.append(templecoordinates)

    for city in (cities):
    #Distance from New Delhi to Kedarnath
        search = "{}{}{}{}".format( 
            "\"Road kms \" ", 
        city, " to ", 
        templelocation )
        templereach = googling(search)
        
        searchcomma = re.search('\,', str(templereach))
        if (searchcomma):
            templereach = re.sub(",", '', templereach)
            #print("km",templereach )
        mano = re.findall('km', str(templereach))
        if (mano):
        
            telmano = re.findall('\(([^$]*)\)', str(templereach))
            if (telmano):
                templedist = [float(s) for s in re.findall(r'-?\d+\.?\d*', str(telmano))]
            
            else:
                templedist = [float(s) for s in re.findall(r'-?\d+\.?\d*', str(templereach))]
            float_lst = list(np.array(templedist, dtype = 'float'))
            chk_lst = re.findall('\[([^$]*)\]', str(float_lst))
            if (chk_lst):
                float_lst = float(re.sub('[^0-9.]+', '', str(float_lst)))
            #print ("i am printing Kms ",float_lst )
            temples_data.append(float_lst)



lt = len(templeslist)

pattern = '\|'

dfd = []
for n in range(0,lt):
    temples_data = []
    
    templename = templeslist[n]
    mano =" ".join(str(elem) for elem in templename).strip()
    templesplit =  re.split(pattern, str(mano))
    
    templename =  templesplit[0].rstrip()
    templelocation = templesplit[1].strip()
    
    templesdata = addingtemples(templename,templelocation)
    #print (temples_data)
    dfd.append(temples_data)


gencsv = pd.DataFrame(dfd,  columns= colheader )

gencsv.to_csv(genfile, index=False, na_rep='Unknown')

pi="\'Temple Data sheet is generated .. !  \' :"
p = ("{} {}".format(pi,genfile))
prt(p)

pi="\'Now you can validate the data .. !  \' :"
p = ("{} {}".format(pi,genfile))
prt(p)