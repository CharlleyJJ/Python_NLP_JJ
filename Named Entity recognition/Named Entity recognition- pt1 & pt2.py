#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


nlp = spacy.load('en_core_web_sm')
from spacy.lang.en import English
nlp2 = English()


# In[3]:


def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' +ent.label_ + ' - ' +str(spacy.explain(ent.label_)))
            
    else:
        print('No entities found')


# In[4]:


doc = nlp(u'Hi how are you?')


# In[5]:


show_ents(doc)


# In[6]:


doc2 = nlp(u"May I go to Burger King or should I go to Paris?")


# In[7]:


show_ents(doc2)


# In[8]:


doc3 = nlp(u"Can I please have 300 Dollars to buy a brazilian candy?")


# In[9]:


show_ents(doc3)


# In[10]:


doc4 = nlp2(u"Tesla to build a U.K. factory for $6 million.")
doc5 = nlp(u"Tesla to build a U.K. factory for $6 million.")


# In[11]:


show_ents(doc4)
show_ents(doc5)


# In[12]:


from spacy.tokens import Span


# In[13]:


ORG = doc.vocab.strings[u"ORG"]


# In[14]:


ORG


# In[15]:


new_ent = Span(doc4,0,1,label=ORG)


# In[16]:


new_ent


# In[17]:


doc4.ents = list(doc4.ents) + [new_ent]


# In[18]:


show_ents(doc4)


# In[19]:


show_ents(doc5)


# In[ ]:





# In[20]:


###### PART 2


# In[21]:


docA = nlp(u"Our company created a brand new vacuum cleaner." u"This new vacuum-cleaner is the best in show.")


# In[22]:


show_ents(docA)


# In[23]:


from spacy.matcher import PhraseMatcher


# In[24]:


matcher = PhraseMatcher(nlp.vocab)


# In[25]:


phrase_list = ['vacuum cleaner','vacuum-cleaner']


# In[26]:


phrase_patterns = [nlp(text) for text in phrase_list]


# In[27]:


matcher.add('NovoProduto',None,*phrase_patterns)


# In[28]:


found_matches = matcher(docA)


# In[29]:


found_matches


# In[30]:


from spacy.tokens import Span


# In[31]:


#dizendo que os aspiradores de pó é um produto 


# In[42]:


PROD =docA.vocab.strings [u"PRODUCT"]


# In[43]:


found_matches


# In[44]:


new_ents = [Span(docA,match[1],match[2],label = PROD) for match in found_matches]


# In[45]:


docA.ents = list(docA.ents) + new_ents


# In[46]:


show_ents(docA)


# In[47]:


docB = nlp(u"Originally I paid $29.95 for this car toy, but now it is markdown by 10 dollars.")


# In[48]:


#filtrando quantas vezes foi mencionado dinheiro nesta frase


# In[52]:


[ent for ent in docB.ents if ent.label_ == "MONEY"] # Nota há uma lista de entidades na documentação, sempre tudo em letra maiúscula.


# In[ ]:




