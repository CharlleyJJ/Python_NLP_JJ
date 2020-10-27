#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spacy


# In[ ]:


nlp = spacy.load("en_core_web_sm")


# In[ ]:


doc = nlp(u"The quick brown fox jumped over the lazy dog")


# In[ ]:


from spacy import displacy


# In[ ]:


displacy.render(doc,style='dep',jupyter=True)


# In[27]:


options = {'distance':110, 'compact':True,'color':'yellow','bg':'#000','font':'Roboto'}


# In[28]:


displacy.render(doc,style='dep',jupyter=True, options=options)


# In[ ]:


doc2 = nlp("This is a sentence.This is another sentence.This is a longer sentence.")


# In[ ]:


spans=list(doc2.sents)


# In[ ]:


displacy.serve(spans,style='dep',options=options)


# In[ ]:




