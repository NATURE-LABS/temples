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
python googlengine.py https://www.googlengine.com/tnt

Contact 
--------
Kyndryl GCP Guild Moderator : Ramamurthy V 
Email           :  ramamurthy.valavandan@kyndryl.com
GCP Contact     : gcpguild@gmail.com
Date            : June 8 2022.
Revised         : July 7 2022.
Contributors    : 42 key members from GCP Guild.
"""
import requests, re, csv, sys

import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import numpy as np
import os
import sys
from subprocess import check_output
from pathlib import Path
import webbrowser 

#--------------------------------------------------------------------------
rootpath = "C:"
client_name = "google"
Project_ID = "serpapi"
Project_Performed_Country = "indias"
projectname = "temples"
N = "\\"
applicationstatename = 'geturltest.py'
#--------------------------------------------------------------------------
Application_Folder = ("{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,projectname))
Google_application = ("{}{}{}".format(Application_Folder,N,applicationstatename))
Application_Data_Folder = ("{}{}{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,'data',N,projectname.capitalize()))
#------------------------------------------------------------------------------------
path = Path(Google_application)
if not path.is_file():
    pi="\'Unable to get Google URL!\' :"
    p = ("{} {}".format(pi,Google_application))
    print(p)
    exit(1)

searchpg = check_output([sys.executable, Google_application], universal_newlines=True)


gourl = re.sub(r'^.+/([^/]+)$', r'\1', searchpg)

clean_string = re.sub(r"[^a-zA-Z]+", '', gourl)
csvfile = ("{}{}{}{}{}{}".format(Application_Data_Folder,N,projectname,"_",clean_string,".csv"))

print(csvfile)

print(searchpg)

if not searchpg:
    print ('URL missing', searchpg)
    exit(1)

website = requests.get(searchpg)
soup = BeautifulSoup(website.content, 'html.parser')

bese= soup.prettify()

#print(bese)
lt = "&lt;"
gt = "&gt;"

bese = re.sub(lt, '<', bese)
bese = re.sub(gt, '>', bese)

mano = []

patent = ("{}{}{}".format('<h3>', "([^$]*)", '</h3>'))

bese = re.findall(patent, str(bese))

bese = re.sub('\,', '|', str(bese))

bese = re.sub('<h3>', '', str(bese))

bese = re.sub('</h3>', ',', str(bese))
bese = re.sub('[^A-Za-z|,]+', ' ' , str(bese))


mano = [ x.strip() for x in bese.strip('[]').split(',') ]

gencsv = pd.DataFrame(mano)

gencsv.to_csv(csvfile, index=False, header = False, na_rep='Unknown')


pi="\'Temple Data sheet is generated .. !  \' :"
p = ("{} {}".format(pi,csvfile))
print(p)

pi="\'Now you can validate the data .. !  \' :"
p = ("{} {}".format(pi,csvfile))
print(p)

#webbrowser.open_new_tab(searchpg)