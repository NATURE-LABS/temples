import os

basepath = "C:"
codepath="python"
function = "temples"
N="\\"


datapath = ("{}{}{}{}{}{}{}".format(basepath,N,codepath,N,function,N,"data"))

if not os.path.exists(datapath):
    os.makedirs(datapath)




