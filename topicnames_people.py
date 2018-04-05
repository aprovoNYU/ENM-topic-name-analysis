import csv
import nltk
import string
from slugify import slugify
import re
import probablepeople
from datetime import datetime, date, time

filetime = datetime.now()
filetime = filetime.strftime('%Y-%m-%d_%I-%M_%p')

taggednames_list = []
problems_list =[]

with open ('alltopic_relOccurTitle_count2_enm_6-28-17_11-50 AM.csv') as topicscsv:
	topicdata = csv.reader(topicscsv)
	print('here we go...')
	next(topicdata, None)
	for row in topicdata:
		taggednames =[]
		topicid = row[0]
		taggednames.append(topicid)
		topicname = row[2]
		
		# topicname_clean = topicname.replace('--',"")
		# topicslug = slugify(topicname_clean, lower=False, spaces=True)
		# topicslug_clean = re.sub(' +', ' ', topicslug)
		# #print(topicslug_clean)
		# cleantopictokens = nltk.word_tokenize(topicslug_clean)
		# lencleantopictokens = len(cleantopictokens)
		#topictokens = nltk.word_tokenize(topicname)
		problems =[]

		if "--" not in topicname:
			taggednames.append(topicname)

			try:
				taggedname, nametype = probablepeople.tag(topicname)
			except probablepeople.RepeatedLabelError:
				# problems.append(topicname)
				# problems.append('not sure what this is')
				# print(problems)
				# problems_list.append(problems)
				print(topicname, '|', 'not sure what this is')
				pass
			taggednames.append(nametype)
			taggednames_list.append(taggednames)
		#if lencleantopictokens >1 and topictokens[1] == ',' and nametype == "Household":
		#if "--" not in topicname:

		#print(topicname, "|", nametype)
#print(problems_list)

with open ("taggedtopicnames_%s.csv" %filetime, "w") as file:
	writer = csv.writer(file)
	writer.writerow(['topic_id','topic_name', 'name_type'])
	for x in taggednames_list:
		row = x
		writer.writerow(row)
print("hooray we did it!")