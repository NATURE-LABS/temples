import re, csv, os, unicodedata, requests, string, lxml,  string

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
"""
templeslistsck = ['bangla', 'balrampur', 'bansuli', 
'barakar', 'bargabhima', 'bhagwati', 
'birla', 'chandrod', 'dakshineshwar', 
'gourangpur', 'hangseswari', 
'hangseswari', 'hanseswari', 'iskcon', 'jor', 
'kali', 'kalibari', 'kalighat', 'mayapur', 
'nandikeshwari', 'nannur', 'pareshnath', 
'radhamadhab', 'rasmancha', 'shyam', 'siddeshwara', 
'tamluk', 'tarapith', 'thanthania', 
'thanthaniakalibari']


templeslistsck = [ "Brahadeeswarar", 
"Meenatchi Amman"
]

"""
#----------------------------------------------------------------------------------------------------
templeslistsck = [ "dakshineshwar" ]
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
def googling(search):
    params1 = {'q': search}
    html1 = requests.get('https://www.google.com/search', 
    headers=headers, params=params1).text
    soup1 = BeautifulSoup(html1, 'lxml')
    diving1 = soup1.find_all("div", {"class": "BNeawe tAd8D AP7Wnd"})
    if (len(diving1) > 1):
        diving1_1 = soup1.find_all("div", {"class": "BNeawe tAd8D AP7Wnd"})[0]
        print(diving1_1)
        ul = ''
        for x in diving1_1:
            ul += ''+ str(x)
            #lookingaddress = lookingaddress.split(' ')[-4]
            #print('lookingaddress', lookingaddress)
            #print(ul)
            m = [ x.strip() for x in ''.join(ul).strip('[]').split(' ') ]
            print(m)
            lookingaddress = ''
            lookingaddress = m[2]
            lookingaddress = re.sub(r"[^a-zA-Z]+",'',lookingaddress)
        print(lookingaddress)
        print('-----------------------------------------------')
    else:
        soupspanfindingall1 = soup1.find_all("span", class_="BNeawe")
        ul = ''
        for x in soupspanfindingall1:
            ul += ''+ str(x)
            #lookingaddress = lookingaddress.split(' ')[-4]
            #print('lookingaddress', lookingaddress)
            #print(ul)
            m = [ x.strip() for x in ''.join(ul).strip('[]').split(' ') ]
            print(m)
            lookingaddress = ''
            lookingaddress = m[2]
            lookingaddress = re.sub(r"[^a-zA-Z]+",'',lookingaddress)
        print(lookingaddress)
        print('-----------------------------------------------')
    #print('-----------------------------------------------')
    #print(soupspanfindingall1)
    #print('-----------------------------------------------')
    #print('-----------------------------------------------')
    pi="\'Google Search for :  \' :"
    p = ("{} {}".format(pi,search))
    prt(p)
    return lookingaddress
#---------------------------------------------------------------- 
tp =  [] 
def addtemple(lookingaddress, mys):
    templelocation = ''
    templelocation = re.sub(r'[^a-zA-Z]', ' ', str(lookingaddress).strip())
    #print(templelocation, 'look', lookingaddress)
    #print('--------------------------------------------------')
    pt = ''
    pt = ("{}{}{}".format(mys.capitalize() , " Temple | ", templelocation ))
    tp.append(pt)
    return tp
#----------------------------------------------------------------------------
#-------------------------------------------------------------------- 
templeslists = []

for t in range(0, len(templeslistsck)):
    if t is not (templeslists):
        k = ''
        k = templeslistsck[t]
        templemano = re.sub(r'[^a-zA-Z]', ' ', str(k).strip())
        search = ("{}{}{}{}".format(k, " temple in ",  statename, " location"))
        #print ('search --:', search)
        lookingaddress = ''
        lookingaddress = googling(search)
        print('------------------')
        print(lookingaddress)
        print('------------------')
        if (lookingaddress):
            #print('temple kadaul:-------------: ', templesgetaroanam)
            #print('------------------')
            addtemple(lookingaddress, k)
            #templeslists.append(k)
#----------------------------------------------------------------
patten = ("{}{}{}".format('<span class="BNeawe tAd8D AP7Wnd">', 
    "([^$]*)", 
    '</span>'))
#----------------------------------------------------------------
def common_elemets(a, b):
    ce = [i for i in a if i in b]
    return ce
#-----------------------------------------------------------------

def completetagging(g):
    ca = ''
    ca = common_elemets(['a'], g)
    if (ca):
        a = ca[0]
    else:
        a = 'a'
    dict={
              'rl': ("{}{}{}".format(a, ',', 'eZt8xd'))
          }
    return dict.get(g, 'b')
#-----------------------------------------------------------
def bs4_get_first_googlesearch(mys):
    myser = ("{}{}{}{}".format(mys, " temple in" , statename ,  " location"))
    print(myser)
    patterns = ["X97X+PW7"]
    params = {'q': myser}
    html = requests.get('https://www.google.com/search', 
    headers=headers, params=params).text
    soup = BeautifulSoup(html, 'lxml')
    diving = soup.find_all("div", {"class": "BNeawe tAd8D AP7Wnd"})
    print ('--------------------------------------')
    print(diving)
    if(diving):
        ul = ''
        for x in diving:
            ul += ''+ str(x)
            #lookingaddress = lookingaddress.split(' ')[-4]
            #print('lookingaddress', lookingaddress)
            #print(ul)
            m = [ x.strip() for x in ''.join(ul).strip('[]').split(' ') ]
            #print(m)
            if (len(m) > 1):
                lookingaddress = ''
                lookingaddress = m[2]
                if (lookingaddress != 'rQMQod'):
                    lookingaddress = m[2]
                else:
                    lookingaddress = ''

                if (lookingaddress):
                    #print ('--------------------------------------')
                    #print(lookingaddress)
                    addtemple(lookingaddress, mys)
                    #print ('--------------------------------------')
    if not lookingaddress:
        soupspanfindingall = soup.find_all("span", class_="BNeawe")
        tb = soup.find_all("span",  {"class": "BNeawe tAd8D AP7Wnd"})
        #print ('--------------------------------------')
        #print(tb)
        if(tb):
            ul = ''
            for x in tb:
                ul += ''+ str(x)
            #lookingaddress = lookingaddress.split(' ')[-4]
            #print('lookingaddress', lookingaddress)
            #print(ul)
            m = [ x.strip() for x in ''.join(ul).strip('[]').split(',') ]
            lookingaddress = ''
            #print(m)
        #print(soupspanfindingall)
        #print ('--------------------------------------')
        patten0 = ("{}{}{}".format( 
                '<span class="BNeawe tAd8D AP7Wnd">',
                        "([^$]*)", 
                        '</span>,'))
        #print ('Key', pattern)
        searchp0 = re.findall(patten0, str(soupspanfindingall))
            
        #print(searchp0)
        string0 = ''
        stringpatten = string0.join(searchp0)
        stringtemplelist = stringpatten.split(",") if stringpatten else []
        #print(soupspanfindingall)
        #print('---------------------------------')
        #print(stringtemplelist)
        lookingaddress = ''
        if (stringtemplelist):
            
            if (stringtemplelist[0] == patterns [0]):
                lookingaddress = stringtemplelist[2].strip()
                
                if (lookingaddress):
                    addtemple(lookingaddress, mys)

            if ( stringtemplelist[0].isdigit() ):
                lookingaddress = stringtemplelist[3].strip()

                if (lookingaddress):
                    addtemple(lookingaddress, mys)               

            if ( stringtemplelist[0] == mys):
                lookingaddress = stringtemplelist[1].strip()

                if (lookingaddress):
                    addtemple(lookingaddress, mys)

            if  not  lookingaddress:

                for n in [1,3]:
                    lookingaddress = ''
                    searchp1 = str(stringtemplelist[n]).strip()
                    w = re.sub(r'[^0-9]','',str(searchp1))
                    #print(w,n)
                    if(searchp1):
                        if ( w.isdigit() ):
                            i = n -1
                            lookingaddress = stringtemplelist[i].strip()
            
                        if (lookingaddress):
                            addtemple(lookingaddress, mys)
                            break

    if not lookingaddress:
        lookingaddress = ''
        lookingaddress = googling(myser)
        #print('lookingaddress ::::::::', lookingaddress)
        if (lookingaddress):
            ul = ''
            for x in lookingaddress:
                ul += ''+ x
            #lookingaddress = lookingaddress.split(' ')[-4]
            #print('lookingaddress', lookingaddress)
            #print(ul)
            m = [ x.strip() for x in ''.join(ul).strip('[]').split(' ') ]
            print(m)
            addtemple(lookingaddress, mys)

for mys in (templeslists):
    #print('temple : ', mys)
    temples = ''
    
    temples = bs4_get_first_googlesearch(mys)

if(tp):
    for t in (tp):
        print(t)
