#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Add the Pandas dependency.
import pandas as pd
import os


# In[37]:


# Files to load
#school_data_to_load = r'Users/carad/Desktop/GWBootcamp/Resources\schools_complete.csv'
#student_data_to_load =r'Users/carad/Desktop/GWBootcamp/Resources\students_complete.csv'


school_data_to_load = r'C:\Users\carad\Desktop\GWBootcamp\Resources\schools_complete.csv'
student_data_to_load = r'C:\Users\carad\Desktop\GWBootcamp\Resources\students_complete.csv'


# In[18]:


# Files to load
#school_data_to_load = os.path.join("Desktop", "GWBootcamp", "Resources", "schools_complete.csv")
#student_data_to_load = os.path.join("Desktop", "GWBootcamp", "Resources", "students_complete.csv")


# In[38]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df = pd.read_csv(student_data_to_load)


# In[39]:


school_data_df.head()

