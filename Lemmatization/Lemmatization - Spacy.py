#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


nlp = spacy.load('en_core_web_sm')


# In[4]:


doc1 = nlp(u"I am a runner running in a race because I love to run since I ran today.")


# In[5]:


for token in doc1:
    print(token.text, '\t', token.pos_,'\t',token.lemma,'\t',token.lemma_)


# In[7]:


def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_:}')


# In[10]:


doc2 = nlp(u'I saw 10 mice today.')


# In[11]:


show_lemmas(doc2)


# In[ ]:




