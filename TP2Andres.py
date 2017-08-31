
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
import pylab


# In[2]:

data = "CDO8702897422043.txt"


# In[58]:

frame = pd.read_csv(data,sep=',',decimal='.',engine='python')


# In[59]:

frame.columns = map(str.strip, frame.columns)
frame.columns = map(str.lower, frame.columns)


# In[60]:

frame.drop(frame.columns[[4]], axis=1, inplace=True)


# In[12]:

frame.keys()


# In[61]:

frame.drop(frame.columns[[0,1,-1]],axis=1,inplace=True)


# In[32]:

frame['yearmoda'] = frame['yearmoda'].apply(str)


# In[22]:

get_ipython().magic(u'matplotlib inline')


# In[66]:

for index, row in frame.iterrows():
    frame.ix[index, 'celsius'] = (row['temp']-32)/1.8


# In[86]:

x = frame["date"]
y = frame["celsius"]
plt.plot(x, y)
pylab.show()


# In[80]:

from datetime import date


# In[84]:

for index, row in frame.iterrows():
    frame.ix[index,'date'] = date(int(row['yearmoda'][0:4]),int(row['yearmoda'][4:6]),int(row['yearmoda'][6:]))


# In[85]:

frame['date']


# In[ ]:



