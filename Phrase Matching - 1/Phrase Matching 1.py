#!/usr/bin/env python
# coding: utf-8

# In[4]:


import spacy


# In[5]:


nlp = spacy.load('en_core_web_sm')


# In[6]:


from spacy.matcher import Matcher


# In[7]:


matcher = Matcher(nlp.vocab)


# In[8]:


#Pchave= input('Digite sua palavra chave: ') ideia para a IA pesquisa X palavra


# In[9]:


#é necessário inserir este conjunto de regras ao comparador ( Matcher)


# ArtificialIntelligence
pattern1 = [{'LOWER':'artificialintelligence'}]
# Artificial-Intelligence
pattern2 = [{'LOWER':'artificial'},{'IS_PUNCT':True},{'LOWER':'intelligence'}]
# Artificial Intelligence
pattern3 = [{'LOWER': 'artificial'},{'LOWER':'intelligence'}]
#Tentando fazer o usuario colocar por input o comando:
#pattern4 = [{'LOWER': f'Pchave }]


# In[10]:


matcher.add("ArtificialIntelligence",None,pattern1,pattern2,pattern3)


# In[16]:


doc = nlp(u"Artificial intelligence (AI), is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of 'intelligent agents': any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[3] Colloquially, the term 'Artificialintelligence' is often used to describe machines (or computers) that mimic 'cognitive' functions that humans associate with the human mind, such as learning and problem solving.[4] just to say we found an artificial-intelligence with a following dash")


# In[17]:


found_matches=matcher(doc)


# In[18]:


print(found_matches)


# In[19]:


for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id] #adquirir a representação da string
    span = doc[start:end] #adquirir em qual linha iniciou e finalizou a palavra identificada
    print(match_id,string_id, start, end, span.text)


# In[ ]:





# In[20]:


matcher.remove('ArtificialIntelligence')


# In[ ]:





# In[29]:


#artificialintelligence ArtificialIntelligence
pattern1 = [{'LOWER': 'artificialintelligence'}]
#Articial.Intelligence
pattern2 = [{'Lower':'Artificial'},{'IS_PUNCT':True, 'OP':'*'},{'LOWER':'intelligence'}]


# In[30]:


matcher.add('ArtificialIntelligence',None,pattern1,pattern2)


# In[31]:


doc2=nlp(u"Artificial--Intelligence is the way we should seek our bright new future alltogether with artificialintelligence yay!")


# In[32]:


found_matches = matcher(doc2)


# In[33]:


print(found_matches)


# In[34]:


for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id] #adquirir a representação da string
    span = doc[start:end] #adquirir em qual linha iniciou e finalizou a palavra identificada
    print(match_id,string_id, start, end, span.text)


# In[35]:


#Phrase Matching2


# In[36]:


#Outro método


# In[37]:


from spacy.matcher import PhraseMatcher


# In[38]:


matcher = PhraseMatcher(nlp.vocab)


# In[39]:


with open('../Text files/machinelearning.txt') as f:
    doc3 = nlp(f.read())


# In[40]:


phrase_list = ['artificial intelligence','making predictions','supervised learning']


# In[41]:


phrase_patterns = [nlp(text) for text in phrase_list]


# In[42]:


phrase_patterns # Observa a lista de frases


# In[43]:


type(phrase_patterns[0]) #Objeto do doc de spacy


# In[44]:


matcher.add('MachineMatcher',None,*phrase_patterns)


# In[46]:


found_matches = matcher(doc3)


# In[47]:


found_matches


# In[48]:


for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id] #adquirir a representação da string
    span = doc3[start:end] #adquirir em qual linha iniciou e finalizou a palavra identificada
    print(match_id,string_id, start, end, span.text)


# In[52]:


for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id] #adquirir a representação da string
    span = doc3[start-5:end+5] #adquirir em qual linha iniciou e finalizou a palavra identificada aderindo CONTEXTO
    print(match_id,string_id, start, end, span.text)


# In[ ]:




