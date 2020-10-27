#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


nlp = spacy.load('en_core_web_sm')


# In[3]:


doc = nlp(u'The quick brown fox jumped over the lazy dogs back')


# In[4]:


print(doc.text)


# In[5]:


print(doc[4].text) # Acessando os tokens


# In[6]:


print(doc[4].pos_)


# In[7]:


print(doc[4].tag_) # VBD means past tense verb


# In[8]:


for token in doc:
    print(f"{token.text:{15}}{token.pos_:{15}}{token.tag_:<{8}} {spacy.explain(token.tag_)}")


# In[9]:


doc2 = nlp(u"I read books on NLP")


# In[10]:


word = doc2[1]


# In[11]:


word.text


# In[12]:


token =word
print(f"{token.text:{15}}{token.pos_:{15}}{token.tag_:<{8}} {spacy.explain(token.tag_)}")


# In[24]:


doc3 = nlp(u"I read a book on NLP")


# In[27]:


word = doc3[1]

token = word
print(f"{token.text:{15}}{token.pos_:{15}}{token.tag_:<{8}} {spacy.explain(token.tag_)}")


# In[28]:


POS_counts = doc.count_by(spacy.attrs.POS)


# In[29]:


POS_counts


# In[30]:


doc.vocab[83].text


# In[32]:


doc[2]


# In[33]:


doc[2].pos


# In[34]:


doc[2].pos_


# In[35]:


for k,v in sorted(POS_counts.items()):
    print(f"{k}.{doc.vocab[k].text:{5}}{v}")


# In[36]:


TAG_counts = doc.count_by(spacy.attrs.TAG)

for k,v in sorted(TAG_counts.items()):
    print(f"{k}.{doc.vocab[k].text:{5}}{v}")


# In[37]:


DEP_counts = doc.count_by(spacy.attrs.DEP)

for k,v in sorted(DEP_counts.items()):
    print(f"{k}.{doc.vocab[k].text:{5}}{v}")


# In[ ]:




