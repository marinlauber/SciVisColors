#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cm_xml_to_matplotlib as cm
import matplotlib.pyplot as plt
import numpy as np

w = np.round(np.genfromtxt("data/vort_000050.dat", delimiter=" ")[1:,:], 6)

mycmap = cm.make_cmap('xml/colormap_2.xml').reversed() #make the Matplotlib compatible colormap
# cm.plot_cmap(mycmap) #plot an 8 by 1 copy of the colormap
plt.imshow(w,cmap=mycmap,extent=[0,1,0,1])
plt.colorbar()
plt.savefig("figure.png", dpi=600)