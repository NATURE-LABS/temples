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
python googledata.py http://www.walkthroughindia.com/hindu-temple/top-25-popular-hindu-temples-tamil-nadu/

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
csvfile = "googledata.csv"
N="\\"

genfile = ("{}{}{}{}{}{}{}".format(basepath,N, codepath, N, function, N, csvfile))

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")

arglen =  len(sys.argv)
exampleurl = "https://www.google.com/search?q='popular hindu temples tamil nadu'"


if (arglen != 2):
    pi="\'Input website is not given .. !  \' :"
    p = ("{} {}".format(pi,exampleurl))
    prt(p)
    pi="python "
    p = ("{} {}".format(pi,exampleurl))
    prt(p)
    exit(1)

searchpg = str(sys.argv[1])

website = requests.get(searchpg)
soup = BeautifulSoup(website.content, 'html.parser')



if (soup.title is not None):
    title = soup.title.string
    dfd = [title]
if (title):
    sl=27
    ls=len(title)
    if(ls <= sl ):
        titname=title
    else:
        titname=(title[0:sl])


for i in range(1,4):
    hn =  ("{}{}".format("h",i)) 

    htags = ("{}{}".format(hn,"tags"))
 
    htags = soup.find_all(hn)
   
    patent = ("{}{}{}{}{}{}{}".format("<", hn, ">", "([^$]*)", "</", hn, ">"))

    for soups in htags:
    
        telmano = re.findall(patent, str(soups))
        if (telmano):
            
            searchcomma = re.search('\,', str(telmano))
            if (searchcomma):
                mymano = ' '
                for x in telmano:
                    mymano += ' '+ x
                    tc = []
                    tcm = re.sub(",", '|', mymano)
                    
                 
                    tc.append(tcm)
                  
                    telapp = tc
           
            else:
                telapp = telmano
            dfd.append(telapp)
mano = []

for ma in (dfd):
    man =" ".join(str(elem) for elem in ma).strip()
    
    mano.append(man)

gencsv = pd.DataFrame(mano)

gencsv.to_csv(genfile, index=False, header = False, na_rep='Unknown')

pi="\'Temple Data sheet is generated .. !  \' :"
p = ("{} {}".format(pi,genfile))
prt(p)

pi="\'Now you can validate the data .. !  \' :"
p = ("{} {}".format(pi,genfile))
prt(p)