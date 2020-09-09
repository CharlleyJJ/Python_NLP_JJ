#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.stem.porter import PorterStemmer


# In[3]:


p_stemmer = PorterStemmer()


# In[4]:


words = ['run', 'runner','ran','runs','easily','fairly']


# In[5]:


for word in words:
    print(word + '---->' + p_stemmer.stem(word))


# In[6]:


from nltk.stem.snowball import SnowballStemmer


# In[13]:


s_stemmer = SnowballStemmer(language = 'english')


# In[21]:


for word in words:
    print(word + '---->' + s_stemmer.stem(word))


# In[20]:


palavra = ['vivendo','vivo','viveu','vila','vilas','vivos','virou','vaz']


# In[19]:


portuguese_stemmer = SnowballStemmer(language = 'portuguese')


# In[22]:


for word in palavra:
    print(word + '---->' + portuguese_stemmer.stem(word))


# In[ ]:




