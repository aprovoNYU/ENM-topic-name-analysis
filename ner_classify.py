import requests, json
from collections import Counter
from nltk.tag import StanfordNERTagger
from nltk.tokenize.mwe import MWETokenizer
from nltk.tokenize import word_tokenize

st = StanfordNERTagger('/Users/alex/Desktop/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz','/Users/alex/Desktop/stanford-ner-2016-10-31/stanford-ner-3.7.0.jar', encoding="utf-8")

with open ("Topics_Z.txt") as json_data:
	topics = json.load(json_data)
	for rows in topics:
		
		for topic in topics[rows]:
			name = str(topic["basket - display_name"])
			if 'None' in name:
				pass
			else:
				print(name)
				#tokenized_name = MWETokenizer(name)
				tokenized_name = word_tokenize(name)
				classified_name = st.tag(tokenized_name)
				print(classified_name)