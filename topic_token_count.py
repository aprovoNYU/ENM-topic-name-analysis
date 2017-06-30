import csv
import nltk
import string
from slugify import slugify
import re
from datetime import datetime, date, time


filetime = datetime.now()
filetime = filetime.strftime('%Y-%m-%d_%I-%M_%p')
newdatalist = []

with open ('alltopic_relOccurTitle_count2_enm_6-28-17_11-50 AM.csv') as topicscsv:
	topicdata = csv.reader(topicscsv)
	next(topicdata, None)
	for row in topicdata:
		newdata=[]

		topicid = row[0]
		newdata.append(topicid)
		topicname = row[2]
		topicname_clean = topicname.replace('--',"")
		topicslug = slugify(topicname_clean, lower=False, spaces=True)
		topicslug_clean = re.sub(' +', ' ', topicslug)
		#print(topicslug_clean)
		topictokens = nltk.word_tokenize(topicslug_clean)
		lentopictokens = len(topictokens)
		#print(topicid,len(topictokens))
		newdata.append(lentopictokens)
		newdatalist.append(newdata)
print(newdatalist)
with open ("topictokencount_%s.csv" %filetime, "w") as file:
	writer = csv.writer(file)
	writer.writerow(['topic_id','number_of_words_in_topic'])
	for x in newdatalist:
		row = x
		writer.writerow(row)