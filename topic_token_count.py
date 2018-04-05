import csv
import nltk
import string
from slugify import slugify
import re
from datetime import datetime, date, time


filetime = datetime.now()
filetime = filetime.strftime('%Y-%m-%d_%I-%M_%p')
newdatalist = []
table = str.maketrans({key: None for key in string.punctuation})

with open ('enm_devdb3_alltopics_2017-12-20-2-28 PM.csv') as topicscsv:
	topicdata = csv.reader(topicscsv)
	next(topicdata, None)
	for row in topicdata:
		newdata=[]

		topicid = row[0]
		print(topicid)
		newdata.append(topicid)
		topicname = row[2]
		print(topicname)
		topicname_clean = re.sub('/'," ",topicname)
		topicname_clean = re.sub("-"," ",topicname_clean)
		topicname_clean = topicname_clean.translate(table)
		print(topicname_clean)
		# topicname_clean = topicname.replace('--',"")
		# topicname_clean = topicname_clean.replace("("," ")
		# topicname_clean = topicname_clean.replace(".","")
		# topicslug = slugify(topicname_clean)
		# print(topicslug)
		# topicslug_clean = re.sub('-', " ", topicslug)
		# print(topicslug_clean)
		topictokens = nltk.word_tokenize(topicname_clean)
		print(topictokens)
		lentopictokens = len(topictokens)
		print(topicid,len(topictokens))
		newdata.append(lentopictokens)
		newdatalist.append(newdata)
print(newdatalist)
with open ("topictokencount_%s.csv" %filetime, "w") as file:
	writer = csv.writer(file)
	writer.writerow(['topic_id','number_of_words_in_topic'])
	for x in newdatalist:
		row = x
		writer.writerow(row)