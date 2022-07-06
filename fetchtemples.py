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
Date            : June 8 2022
revised         : July 7 2022
Contributors    : 102 key members from GCP Guild.
"""
import requests, re, csv, sys

import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import numpy as np
import os
import re
import sys
from subprocess import check_output
from pathlib import Path

#--------------------------------------------------------------------------
rootpath = "C:"
client_name = "google"
Project_ID = "serpapi"
Project_Performed_Country = "indias"
projectname = "temples"
N = "\\"
applicationstatename = 'stateutname.py'
#--------------------------------------------------------------------------
Application_Folder = ("{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,projectname))
Google_application = ("{}{}{}".format(Application_Folder,N,applicationstatename))
#------------------------------------------------------------------------------------
path = Path(Google_application)

if not path.is_file():
   pi="\'Data of States and UTs is missing!\' :"
   p = ("{} {}".format(pi,Google_application))
   print(p)
   exit(1)

output = check_output([sys.executable, Google_application], universal_newlines=True)

#print(output)

inputstate =  re.sub('-',' ', str(output.split(',')[0])) 
inputstametemple = ("{}{}{}".format('Google Engine -', inputstate, ' Temples'))

links = []

titles = []
def getweburls(inputlink,sut):

    parser = 'lxml'  # or 'lxml' (preferred) or 'html5lib', if installed
    resp = urllib.request.urlopen(inputlink)
    soup = BeautifulSoup(resp, parser)
    if (sut == 'India'):
        titles.append(str(soup.title.string))
    #soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
    return soup

baselink = "https://www.googlengine.com"
soup = getweburls(inputlink = baselink, sut = 'Googlengine')

for link in soup.find_all('a', href=True):
    fulllink = ''
    lh = ''
    lh = link['href']
    lh = re.sub('/','',lh)

    conditions = [len(lh) == 3, lh[-1] == 't']

    if all(conditions):
        fulllink = ("{}{}{}".format(baselink,'/',lh))
   
        if not fulllink in links:
            links.append(fulllink)
          

fullcalls = []

for l in range(0, len(links)):
    soup = getweburls(inputlink = links[l], sut = 'India')
    #print(links[l], titles[l],'===>', inputstametemple)
    if (titles[l] == inputstametemple):
        print(links[l])