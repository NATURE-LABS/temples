import re, csv, os, unicodedata, requests, string, lxml,  string, sys

from pathlib import Path
from bs4 import BeautifulSoup

import pandas as pd

#--------------------------------------------------------------------------
def prt(p):
    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#--------------------------------------------------------------------------
basepath = "C:"
codepath="google"
function = "serpapi"
N="\\"
namefile = "indias"
max_gs = 10 # maximum number of google search in href or urls
#-----------------------------------------------------
indiatempledatadir = ("{}{}{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,namefile,N,"data"))

datadirgoo = ("{}{}{}".format(namefile.capitalize(),"_","googlengine_temple_States_and_UTs"))

googledataindiastutdir = ("{}{}{}".format(indiatempledatadir,N,datadirgoo))

cre_directory = Path(googledataindiastutdir)
cre_directory.mkdir(parents=True, exist_ok=True)

indiastautfile = ("{}{}{}".format(googledataindiastutdir,N,"Ind_googlengine_states_ut_master.csv"))
#----------------------------------------------------------------------------------------------------
path = Path(indiastautfile)
#----------------------------------------------------------------------------------------------------
if path.is_file():
    pi="\'India States and UTs data : \' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    
else:
    pi="\'Data of States and UTs is missing!\' :"
    p = ("{} {}".format(pi,indiastautfile))
    prt(p)
    pi="\'Execute myindiagenStatesandUTdata.py First !\' :"
    statesutpy = "Get from Git Hub"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Download :' :"
    statesutpy = "https://github.com/NATURE-LABS/India/blob/main/myindiagenStatesandUTdata.py"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Save myindiagenStatesandUTdata.py \' :"
    statesutpy = "in c:\python\indias"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    pi="\'Document :\' :"
    statesutpy = "https://github.com/NATURE-LABS/India/blob/main/Python%20Lab%20India_states_UT.docx"
    p = ("{} {}".format(pi,statesutpy))
    prt(p)
    exit(1)
#-----------------------------------------------------
def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())
#----------------------------------------------------------
#-----------------------------------------------------
def serapitemplesoutfile(st,csvf):
    templesgoogleoutcsv = ''
    templesgoogleoutcsv = ("{}_{}_{}".format(namefile.capitalize(),st,csvf))
    serpapisearchedtempledatastate = ''
    serpapisearchedtempledatastate = ("{}{}{}".format(googledatastunindiatemplesdir,N,templesgoogleoutcsv))
    return serpapisearchedtempledatastate
#-----------------------------------------------------
fields = ['States and Union Territories in India']
#----------------------------------------------------------------------------------------------------
df_stuts = pd.read_csv(indiastautfile, skipinitialspace=True, usecols=fields)
#-----------------------------------------------------
statesget = sorted([list(row) for row in df_stuts.values])
sul =  []
cap = []
templeslisings = []
#----------------------------------------------------------------------------------------------------
for t in statesget:
  print(t)
  m = [ x.strip() for x in ''.join(t).strip('[]').split(',') ]
  
  if m not in sul:
      sul.append(m[0])
      cap.append(m[1])
  else:
        print("Duplicate is removed", t)
#----------------------------------------------------------------------------------------------------
csco = len(sul)
for cc in range(0,csco):
    
    patternspace = re.compile(r'\s+')
    statename = re.sub(patternspace, '-', sul[cc])
    capital = re.sub(patternspace, '-', cap[cc])
    googledatastunindiatemplesdir = ''
    googledatastunindiatemplesdir = ("{}{}{}".format(googledataindiastutdir,N,statename))
    templesserpapifilterdata = serapitemplesoutfile(st = statename,csvf ="Temples_Google_SerpApi.csv")
    #-----------------------------------------------------
    fields = ['List of temples']
    df_temples = pd.read_csv(templesserpapifilterdata, skipinitialspace=True, usecols=fields)
    #-----------------------------------------------------
    templesget = sorted([list(row) for row in df_temples.values])

    for t in (templesget):
        #print(t)
        templeslisings.append(t[0])
#----------------------------------------------------------------------------------------------------
print(templeslisings)
#--------------------------------------------------------------------------------------------------------
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}
#----------------------------------------------------------------
print("\nName of Temple given as a input:", sys.argv[1])
#----------------------------------------------------------------------------------------------------
templeslistsck = []

for t in (templeslisings):
    if t not in templeslistsck:
        print(t)
        templeslistsck.append(t)

templeslistsck = [ sys.argv[1] ]
#----------------------------------------------------------------------------------------------------
statename = "west bengal"
#--------------------------------------------------------
rootpath = "C:"
client_name = "google"
Project_ID = "serpapi"
N = "\\"
Project_Performed_Country = "indias"
max_gs = 10 # maximum number of google search in href or urls
#-------------------------------------------------------
Application_Data_Folder = ("{}{}{}{}{}{}{}{}{}".format(rootpath,N,client_name,N,Project_ID,N,Project_Performed_Country,N,"data"))
Google_States_UT_Data_Folder_Path = ("{}{}{}".format(Project_Performed_Country.capitalize(),'_',"googlengine_temple_States_and_UTs"))
#------------------------------------------------------------------------------------
googledataindiastutdir = ("{}{}{}".format(Application_Data_Folder,N,Google_States_UT_Data_Folder_Path))
#------------------------------------------------------------------------------------
cre_directory = Path(googledataindiastutdir)
cre_directory.mkdir(parents=True, exist_ok=True)
#-------------------------------------------------------
def prt(p):
    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#-----------------------------------------------------
def csvreaddata(inputfile,fields):
    df_csv = pd.read_csv(inputfile, 
    delimiter=',',
    on_bad_lines='skip', 
    engine="python",
    skipinitialspace=True, usecols=[fields])
    readdata = sorted([list(row) for row in df_csv.values])
    return readdata
#---------------------------------------------------------------
#-----------------------------------------------------
def normalize_caseless(text):
    return unicodedata.normalize("NFKD", text.casefold())
#-----------------------------------------------------
wordcsvpath = ("{}{}{}".format(googledataindiastutdir,N,"word_master.csv"))
#----------------------------------------------------------------------------------------------------
wordmfile = Path(wordcsvpath)

if wordmfile.is_file():
    pi="\'Words data : \' :"
    p = ("{} {}".format(pi,wordmfile))
    prt(p)
    
else:
    pi="\'World filter data is missing!\' :"
    p = ("{} {}".format(pi,wordmfile))
    prt(p)
    pi="\'Execute words.py First !\' :"
    exit(1)
#-------------------------------------------------------------

#------------------------------------------------------------------
tp =  [] 
def addtemple(lookingaddress, mys):
    print('lookingaddress', lookingaddress)
    templelocation = re.sub(r'[^a-zA-Z]', ' ', str(lookingaddress).strip())
    pt = ''
    pt = ("{}{}{}".format(mys.capitalize() , " Temple | ", templelocation ))
    tp.append(pt)
    return tp
#----------------------------------------------------------------------------

templeslists = []

for t in range(0, len(templeslistsck)):
    if t is not (templeslists):
        mys = ''
        mys = templeslistsck[t]
        templemano = re.sub(r'[^a-zA-Z]', ' ', str(mys).strip())
        search = ("{}{}{}{}".format(mys, " temple in ",  statename, " location"))
        lookingaddress =''
        params1 = {'q': search}
        html1 = requests.get('https://www.google.com/search', 
        headers=headers, params=params1).text
        soup1 = BeautifulSoup(html1, 'lxml')
        diving1 = soup1.find_all("div", {"class": "BNeawe tAd8D AP7Wnd"})
        #print(diving1)
        ul = ''
        for x in diving1:
            ul += ''+ str(x)
        m = [ x.strip() for x in ''.join(ul).strip('[]').split('</div>') ]
    
        #print(m)
        print(len(m), 'length')
        if (len(m) == 3):
            s1 = soup1.find_all("span", class_="BNeawe")
            print('len', len(s1) , s1)
            if (len(s1) > 0):
                ul = ''
                for x in s1[1]:
                    ul += ''+ str(x)
                    m = [ x.strip() for x in ''.join(ul).strip('[]').split('</span>') ]
                    tl = list(filter(None, m))
                    tl = [ x.strip() for x in ''.join(tl).strip('[]').split(',') ]
                    #lookingaddress = re.sub(r"[^a-zA-Z]+",'',tl)
                    pat1 = 'X97X+PW7'
                    if (tl[0] == pat1):
                        lookingaddress = tl[2]
                        res = len(re.findall(r'\w+', lookingaddress))

                        print ('Lenth', res, '---------')
                        print(tl)
                        if (res == 1):
                            addtemple(lookingaddress, mys)

                if not lookingaddress:
                    for x in s1:
                        ul += ''+ str(x)
                        m = [ x.strip() for x in ''.join(ul).strip('[]').split('</span>') ]
                        print (m)
  
        if (len(m) >= 8):
        
            la = ''
            la = [ x.strip() for x in ''.join(m[0]).strip('[]').split(',') ]
            #lookingaddress = la[-2].strip()
            print (la)
            print ('len --------------', len(la))
            res = len(re.findall(r'\w+', str(la)))
            print ('Lenth', res, '---------')
            #lookingaddress = la[1]
            if (res >= 1):
                lookingaddress = la[2]
                addtemple(lookingaddress, mys)
        
        if (len(m) == 8):
            la = ''
            la = [ x.strip() for x in ''.join(m[0]).strip('[]').split(',') ]
            #lookingaddress = la[-2].strip()
            print (la)
            print ('len --------------', len(la))
            res = len(re.findall(r'\w+', str(la)))

            print ('Lenth', res, '---------')
            
            if (res >= 1):
                lookingaddress = la[1]
            
                addtemple(lookingaddress, mys)
        
            print('-----------------------------------------------')
        #print('-----------------------------------------------')
        #print(soupspanfindingall1)
        #print('-----------------------------------------------')
        #print('-----------------------------------------------')
        pi="\'Google Search for :  \' :"
        p = ("{} {}".format(pi,search))
        prt(p)
 


if(tp):
    for t in (tp):
        print(t)
