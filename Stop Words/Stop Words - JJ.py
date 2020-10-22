#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


nlp = spacy.load("en_core_web_sm")


# In[5]:


print(nlp.Defaults.stop_words)


# In[7]:


len(nlp.Defaults.stop_words)


# In[10]:


nlp.vocab['is'].is_stop ## verifica na lista de vocabul[ario] X palavra


# In[11]:


nlp.vocab['mystery'].is_stop


# In[12]:


## Aderindo palavras


# In[23]:


nlp.Defaults.stop_words.add ('btw')


# In[24]:


len(nlp.Defaults.stop_words)


# In[25]:


nlp.Defaults.stop_words.remove ('btw')


# In[27]:


nlp.vocab['btw'].is_stop = False


# In[28]:


nlp.vocab['btw'].is_stop


# In[ ]:




