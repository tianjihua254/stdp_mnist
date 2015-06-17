
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys



input_size =28
output_num = 8
#im = plt.imshow(np.zeros((input_size,input_size)))
start = 100
stop = 350

output_num = int(sys.argv[1])
start = int(sys.argv[2])
stop = int(sys.argv[3])


for run_i in range(start, stop):
    stdp_weight = np.load('saved/weight_%d.npy'%run_i)
    to_plot = np.reshape(stdp_weight[:,output_num], (input_size, input_size))
    if run_i == start:
        plt.figure(figsize=(3,3))
        im = plt.imshow(to_plot,interpolation='none')#,cmap = cm.Greys_r)#,interpolation='none')
        fig = plt.gcf()
        im.set_clim(0, 1.3)
        plt.colorbar(im, fraction=0.046, pad=0.04)
    else:
        im.set_data(to_plot)
        
    #im = plt.imshow(to_plot)
    plt.title(run_i)
    plt.draw()
    plt.pause(0.1)
#plt.close()


# In[ ]:


