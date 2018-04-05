import re
import csv
from datetime import datetime, date, time

filetime = datetime.now()
filetime = filetime.strftime('%Y-%m-%d_%I-%M_%p')
#one initial only
#two initials, no space
count=0

#two initials, space
abbreviated_name_regex = re.compile('\w*,\s[a-zA-Z]\.\s[a-zA-Z]\.|\w*,\s[a-zA-Z]\.[a-zA-Z]\.|\w*,\s[a-zA-Z]\.')
# abbreviated_name_regex2 = re.compile('\w*,\s[a-zA-Z]\.[a-zA-Z]\.'),
# abbreviated_name_regex3 = re.compile('\w*,\s[a-zA-Z]\.\s[a-zA-Z]\.')
# ]

with open ('alltopic_relOccurTitle_count2_enm_6-28-17_11-50 AM.csv') as topicscsv:
	topicdata = csv.reader(topicscsv)
	print('here we go...')
	next(topicdata, None)
	for row in topicdata:
		topicid = row[0]
		topicname = row[2]
		abbreviated_name = abbreviated_name_regex.match(topicname)
		if abbreviated_name:
			print('Match found: ', abbreviated_name.group(), "|", topicname)
			count=count+1
		else:
			pass
print(count)