#!/usr/bin/env python
# coding: utf-8

# In[101]:


import spacy


# In[123]:


nlp = spacy.load('en_core_web_sm')
from spacy.lang.en import English
nlp2 = English()


# In[124]:


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' +ent.label_ + ' - ' +str(spacy.explain(ent.label_)))
            
    else:
        print('No entities found')


# In[125]:


doc = nlp(u'Hi how are you?')


# In[126]:


show_ents(doc)


# In[127]:


doc2 = nlp(u"May I go to Burger King or should I go to Paris?")


# In[128]:


show_ents(doc2)


# In[129]:


doc3 = nlp(u"Can I please have 300 Dollars to buy a brazilian candy?")


# In[130]:


show_ents(doc3)


# In[210]:


doc4 = nlp2(u"Tesla to build a U.K. factory for $6 million.")
doc5 = nlp(u"Tesla to build a U.K. factory for $6 million.")


# In[211]:


show_ents(doc4)
show_ents(doc5)


# In[212]:


from spacy.tokens import Span


# In[213]:


ORG = doc.vocab.strings[u"ORG"]


# In[214]:


ORG


# In[215]:


new_ent = Span(doc4,0,1,label=ORG)


# In[216]:


new_ent


# In[217]:


doc4.ents = list(doc4.ents) + [new_ent]


# In[218]:


show_ents(doc4)


# In[219]:


show_ents(doc5)


# In[ ]:




