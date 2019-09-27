#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mne
import numpy as np
import matplotlib as plt
import pandas as pd
import os
import scipy.io


# In[9]:


# define path
global project_path, eeg_path, data_path, label_path, post_fix, sampling
project_path = '/Volumes/CLPS_Watanabe_Lab/users/Zhiyan/SleepDecoding/'
eeg_path = 'Experiment/sbj/'
data_path = 'EEG/raw/'
label_path = 'label/'
post_fix = '_reref_01100.vhdr'
subjects = ['sldcd01']
naps = ['nap2'] #%, 'nap3']
sampling = 500 # hz


# In[10]:


# define the function for loading participants EEG raw data 
def load_parse_eeg(SUB, NAP):
    fn_path = project_path +  eeg_path + SUB + '/' + NAP + '/' +  data_path + SUB + NAP + post_fix
    raw = mne.io.read_raw_brainvision(fn_path, eog = ('HEOG', 'VEOG'), preload=True)
    eeg_pick = raw.copy().pick_types(eeg = True, eog = True, misc = True)
    # pick channels 
    eog_pick = raw.copy().pick_types(eeg = False, eog = True)
    emg_pick =raw.copy().pick_types(eeg = False, eog = False, misc = True)
    return eeg_pick, eog_pick, emg_pick


# In[18]:


# function for loading the stage label 


# In[20]:


# label = load_label_eeg('sldcd01', 'nap2')
# label.shape


# In[23]:


# function for loading bad eeg chanels 
def load_bad_ch(SUB, NAP):
    fn_path = project_path +  eeg_path + SUB + '/' + NAP + '/' +  label_path + SUB + '_' + NAP + '_bad' + '.txt'
    bad = pd.read_csv(fn_path, sep=" ", header = None)
    return bad 

#bad = load_bad_ch('sldcd01', 'nap2')


# In[ ]:




