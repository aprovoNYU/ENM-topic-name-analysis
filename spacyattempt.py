import requests, json
import spacy

nlp = spacy.load('en')


with open ("Topics_Z.txt") as json_data:
	topics = json.load(json_data)
	for rows in topics:
		
		for topic in topics[rows]:
			name = str(topic["basket - display_name"])
			if 'None' in name:
				pass
			else:
				#print(name)
				#tokenized_name = MWETokenizer(name)
				doc = nlp(name)
				print(doc[0].text, doc[0].ent_iob, doc[0].ent_type_)
				# for ent in doc.ents:
				# 	print(ent.label_, ent.text)