
# coding: utf-8

# # Spike train explorer
# 
# The `SpikeTrainExplorer` contains several functions to explore and plot spike trains and templates.

# In[ ]:


import yass
print('Running on YASS version {}'.format(yass.__version__))


# In[ ]:


import os.path as path
import matplotlib.pyplot as plt
from yass.explore import SpikeTrainExplorer, RecordingExplorer

get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (10, 10)


# In[ ]:


# path to whitened recordings, geometry file and spike train
ROOT = path.join(path.expanduser('~'), 'data/yass')
path_to_data = path.join(ROOT, 'tmp/whitened.bin')
path_to_geom = path.join(ROOT, 'ej49_geometry1.txt')
path_to_spike_train = path.join(ROOT, 'middle_spike_train.npy')


# In[ ]:


# initialize recordings explorer, this is another helper class
# to explore recordings and is needed to initialize the spike
# train explorer
rce = RecordingExplorer(path_to_data,
                        path_to_geom,
                        spike_size=15,
                        neighbor_radius=70,
                        dtype='float64',
                        n_channels=49,
                        data_format='long')


# In[ ]:


# we now initialize the spike train explorer
spe = SpikeTrainExplorer(path_to_spike_train, rce)


# In[ ]:


# we can take a look at the spike train, first column is the spike
# index, second column is the spike ID
spe.spike_train


# In[ ]:


# plot some templates
spe.plot_templates(group_ids=[0, 1, 2, 3, 4, 5])

