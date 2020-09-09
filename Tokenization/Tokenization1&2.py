#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
nlp = spacy.load('en_core_web_sm')


# In[2]:


mystring = '"We\'re moving to L.A.!"'


# In[3]:


mystring


# In[4]:


print(mystring)


# In[5]:


doc = nlp(mystring)


# In[6]:


for token in doc:
    print(token.text)


# In[7]:


doc2 = nlp(u"We're here to help ! Send snail-mail, email support@jjsite.com or visit us at http://www.google.com!")


# In[8]:


for t in doc2:
    print(t)


# In[9]:


doc3 = nlp(u"A 5km NYC cab ride cost $10.30")


# In[10]:


for t in doc3:
    print(t)


# In[11]:


doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")


# In[12]:


for t in doc4:
    print(t)


# In[13]:


len(doc4)


# In[14]:


doc4.vocab


# In[15]:


len(doc4.vocab)


# In[16]:


doc5 = nlp(u"It is better to give than receive.")


# In[17]:


doc5[0]


# In[18]:


doc5[2:5]


# In[19]:


doc5[0]='test' ## pois o spacy realiza muita coisa dentro de cada token, n faz sentido uma linha python substituir tudo


# In[20]:


doc8 = nlp(u'Apple to build a South Korea factory gona pay ₩ 6 million for the locals governments ❤ .')


# In[21]:


for token in doc8:
    print(token.text, end =' | ')


# In[22]:


for entity in doc8.ents:
    print(entity) ## o proprio spacy identifica que estas palavras sao entidades em especial no contexto
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print('\n')


# In[23]:


doc9 = nlp(u'Autonomous cars shift insurance liability for manufacturers.')


# In[24]:


for chunk in doc9.noun_chunks:
    print(chunk)


# In[25]:


##Part 2 starts here ##


# In[26]:


from spacy import displacy


# In[27]:


##Visualization method for tokens


# In[28]:


doc = nlp(u"Apple is going to build a U.K. factory for $6 billion." )


# In[29]:


displacy.render(doc,style='dep',jupyter=True,options={'distance':110})


# In[30]:


doc10 = nlp(u"Over the last quarter Apple sold nearly 20 thousand in Ipods for a profit of $3 millions.")


# In[31]:


displacy.render(doc10, style='ent', jupyter=True)


# In[32]:


doc11 = nlp(u"This is a sentence.")


# In[77]:


displacy.serve(doc11,style='dep') ##http://127.0.0.1:5000/


# In[ ]:





# In[33]:


doc12 = nlp(u'Laressa is the most Beutiful girl in the world.')


# In[35]:


options = {"compact": True, "bg": "#C091FF","color": "white", "font": "Adam"}
displacy.render(doc12, style="dep", options=options, jupyter=True)


# In[36]:


displacy.render(doc12, style="ent", options=options, jupyter=True)


# In[ ]:




