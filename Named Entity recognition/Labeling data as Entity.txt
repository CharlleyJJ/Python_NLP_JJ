from spacy.tokens import Span
 
# Get the hash value of the PRODUCT entity label
PRODUCT = doc.vocab.strings[u'PRODUCT']
PRODUCT
# Create a Span for the new entity
new_ent = Span(doc, 0, 1, label=PRODUCT)
 
# Add the entity to the existing Doc object
for entity in doc.ents:
    if entity.text == 'Walkman':
        span = Span(doc, entity.start, entity.end, label=PRODUCT)
        doc.ents = [span if e == entity else e for e in doc.ents]
 
displacy.render(doc, style='ent', jupyter=True)
