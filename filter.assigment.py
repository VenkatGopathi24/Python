#!/usr/bin/env python
# coding: utf-8

# In[6]:


L = [1,2,3,4]
def fun(a):
    return a%2==0

list2 = filter(fun,L)
result = list(list2)
print(result)


# In[9]:


result


# In[ ]:




