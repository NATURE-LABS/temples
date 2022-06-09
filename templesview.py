import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


basepath = "C:"
codepath="python"
function = "temples"
csvfile = "indiatemples.csv"
N="\\"
inputcsvfile = ("{}{}{}{}{}{}{}".format(basepath,N, codepath, N, function, N, csvfile))

temple_data = pd.read_csv(inputcsvfile)

#temple_data['State']=temple_data['templeName'].str.split(',',expand=True)[1]

def pltfig(parameter):

    plt.figure(figsize=(15,6))
    sns.countplot(parameter,
                  x = parameter,  
                  data = temple_data, 
                  palette="Set1"
                
                  )
    plt.xticks(rotation = 90)
    
    plt.show()


     
pltfig('Temple Name')
#pltfig(temple_data.State.value_counts())

pltfig(temple_data.State.unique())

#pltfig('DistanceFromMumbai(Km)')

def temp(city):
    return temple_data.sort_values(by=[city],ignore_index=True).loc[:,['Temple Name',city]].head(10)

deldis = temp("Distance From Bengaluru(Km)")

print(deldis)
