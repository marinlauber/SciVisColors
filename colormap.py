#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cm_xml_to_matplotlib as cm
import matplotlib.pyplot as plt
import numpy as np
import os

w = np.round(np.genfromtxt("data/vort_000050.dat", delimiter=" ")[1:,:], 6)

def make_figure(w, cmp="RdBu", fname="figure"):
    plt.imshow(w,cmap=cmp,extent=[0,1,0,1])
    plt.colorbar()
    plt.savefig("images/"+fname+".png", dpi=600)
    plt.close()

# list all colormaps
# xmls = os.listdir("xml")
xmls = [_ for _ in os.listdir("xml") if _.endswith("xml")]

# generate README.md
f = open("README.md", "w")
f.write("# SciVisColormaps\n\n")
f.write("Repo holding some custom colormaps and a python script to convert them from `.xml` to matplotlib colormaps.\n")
f.write("\nHere is a list of all colormaps:\n")

for i,cmap in enumerate(xmls):
    mycmap = cm.make_cmap("xml/"+cmap)
    make_figure(w, mycmap, cmap[:-4])
    f.write("\n"+cmap[:-4]+"\n![image_"+str(i)+"](images/"+cmap[:-4]+".png)\n")
f.close()
