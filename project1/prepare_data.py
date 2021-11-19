import os
fd = open("keywords-web2.csv","r").read().split("\n")
print("Total sentences in data: ",len(fd))
f = open('keyword-data.txt','w')
for i in fd:
	i=i.strip()
	if i:
		title = i.split('"')[1].strip()
		keywords = i.split('"')[3].strip().split(",")
		if title and len(keywords)>0:
			f.write(title + "\t" + ' '.join(k.replace(' ', '_').strip() for k in keywords) + "\n")
f.close()
