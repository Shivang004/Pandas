#!/usr/bin/env python
# coding: utf-8

# # PANDAS

# In[3]:


import pandas as pd
import openpyxl


# # Reading
# 

# In[4]:


pd.read_excel("shiva.xlsx").head()


# In[5]:


pd.read_excel("shiva.xlsx").tail()


# In[15]:


data=pd.read_excel("shiva.xlsx")
data


# In[16]:


pd.set_option('display.max_rows', 5)


# In[17]:


data


# In[18]:


data.P1


# In[19]:


data["P1"][0]


# In[20]:


data.iloc[0]


# In[22]:


data.iloc[:,0]


# In[23]:


data.iloc[:3,0]


# In[24]:


data.iloc[1:3,0]


# In[25]:


data.iloc[-5:]


# In[28]:


data.set_index("P1")


# In[29]:


data.P1==4


# In[31]:


data["P1"]=5
data


# In[32]:


data.set_index("P1")


# In[33]:


data


# In[34]:


data["P1"]=range(len(data),0,-1)
data.set_index("P1")


# In[35]:


data.describe()


# In[43]:


pd.set_option("display.max_rows",10)


# In[44]:


data


# In[45]:


data.describe()


# # data.P1.describe()

# In[46]:


data.P1.describe()


# In[47]:


data.mean()


# In[49]:


data.P1.unique()


# In[54]:


data.P1.value_counts()


# # Map
# 

# In[58]:


data_mean=data.P2.mean()
data_mean


# In[60]:


data.P2.map(lambda p: p- data_mean)


# In[65]:


data.P3 + data.P2


# # Grouping and Sorting

# In[71]:


data.groupby("P1").P1.count()


# In[75]:


data.groupby("P1").P2.min()


# In[77]:


data.groupby("P3").apply(lambda d: d.P2.iloc[0])


# In[78]:


data


# In[83]:


data.groupby(["P3","P4"]).apply(lambda d: d.loc[d.P5.idxmax()])


# In[87]:


data.groupby("P10").P2.agg([len,min ,max])


# In[90]:


data.sort_values(by="P1")


# In[91]:


data.sort_values(by="P1",ascending=False)


# In[92]:


data.sort_index()


# In[93]:


data.sort_values(["P1","P2"])


# # Datatypes And Missing values
# 

# In[99]:


data.P2.dtype


# In[100]:


data.dtypes


# In[101]:


data.P1.astype('float64')


# In[103]:


data


# In[104]:


data.index.dtype


# In[106]:


data.isnull()


# In[108]:


data[pd.isnull(data.P1)]


# In[109]:


data.fillna("NULL")


# In[119]:


data=data.replace(66,None)


# In[120]:


data


# In[121]:


data.isnull()


# In[124]:


data=data.fillna("Hello")
data


# In[126]:


data.groupby("P2").P1.count()


# # Renaming and Combing

# In[127]:


data.rename(columns={"P10":"P15"})


# In[130]:


data=data.rename(index={0:"zero"})


# In[131]:


data.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

