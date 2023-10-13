#!/usr/bin/env python
# coding: utf-8

# In[9]:


#copy, difference, intersection, symetric_difference, union, issuperset, issubset, isdisjoint


# In[11]:


a1 = frozenset([1,2,3,4,4,5,5,5])


# In[12]:


a1


# In[15]:


type(a1)


# In[13]:


a2=a1.copy()    #Coping data from 1 frozenset to another frozenset


# In[14]:


a2


# In[16]:


type(a2)


# In[17]:


a3 = frozenset(["naveen","gopathi",2,3,4,5,6,(2+1j)])


# In[18]:


a3


# In[19]:


a3.difference(a2)  #Difference it shows the difference of values presenyt in a3


# In[20]:


a3.intersection(a2) #Shows the matching values from both the frozenset


# In[21]:


a3.symetric_difference(a2)  #symetric_difference not present


# In[22]:


a3.union(a2)  #it shows all the elements pressent in both the sets without duplicates


# In[23]:


a4 = frozenset([2,3,4,5])


# In[24]:


a4


# In[25]:


a4.issubset(a3)  #Issubset    becuse 2,3,4,5 is present in a3 also


# In[27]:


a3.issuperset(a4)  #Issuperset   it means a3 contains all the values of 24


# In[28]:


a3.isdisjoint(a4)


# In[29]:


a4.isdisjoint(a3)


# In[ ]:




