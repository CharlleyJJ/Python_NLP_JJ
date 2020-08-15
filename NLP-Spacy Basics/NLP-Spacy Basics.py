#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


nlp = spacy.load('en_core_web_sm')


# In[16]:


doc = nlp(u'Tesla is looking at buying U.S. startup for $6 Million ') ## Doc object


# In[17]:


for token in doc:
    print(token.text)


# In[18]:


for token in doc:
    print(token.text,token.pos)


# In[19]:


for token in doc:
    print(token.text,token.pos_,token.dep_)


# In[20]:


nlp.pipeline


# In[21]:


##Tagger ,  Parser , Name entity recognizer


# In[22]:


nlp.pipe_names


# In[ ]:





# In[29]:


doc2 = nlp(u"Tesla isn't   looking into startups anymore.")


# In[30]:


for token in doc2:
    print(token.text,token.pos_,token.dep_)


# In[31]:


doc2[0].pos_


# In[32]:


doc2[0].dep_


# In[41]:


doc2[2].lemma_


# In[42]:


doc3 = nlp(u"This chapter will introduce you to the basics of text processing with spaCy. You'll learn about the data structures, how to work with statistical models, and how to use them to predict linguistic features in your text. Learn how to make the most of spaCy's data structures, and how to effectively combine statistical and rule-based approaches for text analysis.")


# In[43]:


chapter_quote = doc3[0:13]


# In[44]:


print(chapter_quote)


# In[45]:


type(chapter_quote)


# In[46]:


type(doc3)


# In[50]:


doc4 = nlp(u"This is the first sentence. This is another sentence. This is the last sentence.")


# In[51]:


for sentence in doc4.sents:
    print(sentence)


# In[53]:


doc4[6].is_sent_start


# In[55]:


doc4[8].is_sent_start ## Won`t return anything bcuz this isn't the sentence start


# In[ ]:




