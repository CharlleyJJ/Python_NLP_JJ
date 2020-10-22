#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NLP Basics Assessment

# For this assessment we'll be using the short story [_An Occurrence at Owl Creek Bridge_](https://en.wikipedia.org/wiki/An_Occurrence_at_Owl_Creek_Bridge) by Ambrose Bierce (1890). <br>The story is in the public domain; the text file was obtained from [Project Gutenberg](https://www.gutenberg.org/ebooks/375.txt.utf-8).

# In[12]:


# RUN THIS CELL to perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')


# **1. Create a Doc object from the file `owlcreek.txt`**<br>
# > HINT: Use `with open('../TextFiles/owlcreek.txt') as f:`

# In[13]:


# Enter your code here:
with open('../Text files/owlcreek.txt') as f:
    doc = nlp(f.read())


# In[14]:


# Run this cell to verify it worked:

doc[:36]


# **2. How many tokens are contained in the file?**

# In[17]:


len(doc)


# **3. How many sentences are contained in the file?**<br>HINT: You'll want to build a list first!

# In[122]:


#*for sentence in doc.sents:
#   print(sentence)
#len(sentence)

doc_sentences = [sents for sents in doc.sents]
print(doc_sentences)
len(doc_sentences)


# **4. Print the second sentence in the document**<br> HINT: Indexing starts at zero, and the title counts as the first sentence.

# In[133]:


#doc[13:36]
print(doc_sentences[2].text)


# ** 5. For each token in the sentence above, print its `text`, `POS` tag, `dep` tag and `lemma`<br>
# CHALLENGE: Have values line up in columns in the print output.**

# In[153]:


doc2 = doc[13:36]
doc5 = print(doc_sentences[2].text)

def show_lemmas(doc2):
    for token in doc2:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_:}')
    print('\n\n\n')
show_lemmas(doc2)

for token in doc_sentences[2]:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.dep_:<{20}} {token.dep:<{20}} {token.lemma:<{22}} {token.lemma_:}')


# In[7]:


# NORMAL SOLUTION:


# In[8]:


# CHALLENGE SOLUTION:


# **6. Write a matcher called 'Swimming' that finds both occurrences of the phrase "swimming vigorously" in the text**<br>
# HINT: You should include an `'IS_SPACE': True` pattern between the two words!

# In[73]:


# Import the Matcher library:

from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)


# In[74]:


# Create a pattern and add it to matcher:
#SwimmingVigorously
pattern1 = [{'LOWER': 'swimmingvigorously'}]
#Swimming-Vigorously
pattern2 = [{'LOWER':'swimming'},{'IS_PUNCT':True, 'OP':'*'},{'LOWER':'vigorously'}]
#swimming vigorously
pattern3 = [{'LOWER':'swimming'},{'IS_SPACE':True, 'OP':'*'},{'LOWER':'vigorously'}]

#add

matcher.add("Swimming Vigorously", None, pattern1, pattern2, pattern3)



# In[77]:


# Create a list of matches called "found_matches" and print the list:

found_matches = matcher(doc)
print(found_matches)


# **7. Print the text surrounding each found match**

# In[113]:


##for match_id, start, end in found_matches:
string_id = nlp.vocab.strings[match_id] #adquirir a representação da string
span = doc[1265:1290] #adquirir em qual linha iniciou e finalizou a palavra identificada aderindo CONTEXTO
print(span.text)



# In[162]:


#Professor
def surrounding(doc,start,end):
    print(doc[start-9:end+13])


# In[163]:


surrounding(doc,1274,1277)


# In[118]:


string_id = nlp.vocab.strings[match_id] #adquirir a representação da string
span = doc[3602:3617] #adquirir em qual linha iniciou e finalizou a palavra identificada aderindo CONTEXTO
print(span.text)


# In[175]:


#Professor
def surrounding2(doc,start,end):
    print(doc[start-7:end])


# In[176]:



surrounding2(doc,3602,3617)


# **EXTRA CREDIT:<br>Print the *sentence* that contains each found match**

# In[196]:


for sentence in doc_sentences:
    if found_matches[0][1]<sentence.end:
        print(sentence)
        break


# In[197]:




for sentence in doc_sentences:
    if found_matches[1][1]<sentence.end:
        print(sentence)
        break


# ### Great Job!
