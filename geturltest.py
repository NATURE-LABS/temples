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
applicationstatename = 'fetchtemples.py'
#--------------------------------------------------------------------------
Application_Folder = ("{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,projectname))
Google_application = ("{}{}{}".format(Application_Folder,N,applicationstatename))
#------------------------------------------------------------------------------------
path = Path(Google_application)

if not path.is_file():
    pi="\'Unable to find dirctory!\' :"
    p = ("{} {}".format(pi,Google_application))
    print(p)
    exit(1)

geturl = check_output([sys.executable, Google_application], universal_newlines=True)

print(geturl)

#webbrowser.open_new_tab(geturl)
                    
