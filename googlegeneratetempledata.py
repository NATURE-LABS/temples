"""
Purpose : Google Connect is a utility to connect to the Google Search Engine.
Generate the csv data based on the search query given in the argument.
The demonstrated  program generate the datasheet in  a format in CSV.

Design and developed by :
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Lab : Nature Labs @ GCP
How to use
------------
python googlegeneratetempledata.py 

Contact 
--------
Kyndryl GCP Guild Moderator : Ramamurthy V 
Email           :  ramamurthy.valavandan@kyndryl.com
GCP Contact     : gcpguild@gmail.com
Date            : June 8 2022.
Contributors    : 42 key members from GCP Guild.
"""

import requests, re, csv, sys

import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import numpy as np


basepath = "C:"
codepath="python"
function = "temples"
N="\\"
namefile = "googledata"

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

arglen =  len(sys.argv)

exampleurl = "https://www.googlengine.com/tnt"

pythoncode = str(sys.argv[0])

if (arglen != 2):
    pi="\'Input website is not given .. !  \' :"
    p = ("{} {}".format(pi,exampleurl))
    prt(p)
    pi="python "
    p = ("{} {} {}".format(pi,pythoncode, exampleurl))
    prt(p)
    exit(1)

searchpg = str(sys.argv[1])

gourl = re.sub(r'^.+/([^/]+)$', r'\1', searchpg)

inputcsvfilename = ("{}{}{}{}".format(namefile,"_",gourl,".csv"))

googletempledata = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,"data",N,inputcsvfilename))

#df = pd.read_csv(googletempledata, header=None)

df = pd.read_csv(googletempledata, delimiter=',')
templeslist = sorted([list(row) for row in df.values])

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


generatemplecsvfile = "indiatemples.csv"

genfile = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,"data",N,generatemplecsvfile))

def coordinatesearch(search):
    try:
        templecoordinatesget = templecoordinates = ''
        #search =  re.sub('[^A-Za-z]+', '', search)
        search = [re.sub(r"[^a-zA-Z]+", ' ', k) for k in search.split("\n")]
        mymano = ' '
        for x in search:
            mymano += ' '+ x
        templecoordinatesget = googling(str(mymano))

        templecoordinates = re.sub('[^0-9.,]+', '', templecoordinatesget)
        
        if not (templecoordinates):
            
            search = "'{}{}{}".format("'", " the latitude longitude coordinates of India", "'")
            templecoordinatesget = googling(search)
            templecoordinates = re.sub('[^0-9.,]+', '', templecoordinatesget)
            
            
        return templecoordinates

    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    finally:
        if not (templecoordinates):
            search = "'{}{}{}".format("'", " the latitude longitude coordinates of India", "'")
            templecoordinates = googling(search)
            templecoordinates = re.sub('[^0-9.,]+', '', templecoordinatesget)
            return templecoordinates

def googling(search):
    url = f"https://www.google.com/search?&q={search}"
    pi="\'Google Search for :  \' :"
    p = ("{} {}".format(pi,search))
    prt(p)
    
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

    search = "'the latitude longitude coordinates of {} {} ".format(templelocation,"India'")
    
    templecoordinates = coordinatesearch(search)
    
  
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