import os
cwd = os.getcwd()
path1 = os.path.join(cwd,"keyword-data.txt")
path2=os.path.join(cwd,"keyword-extraction/keyword-data.txt")
data1 = open(path1).read().split("\n")
data2 = open(path2).read().split("\n")
data=[]
data.extend(data1)
data.extend(data2)
print("Data before duplicate removal: ",len(data))
data = list(set(data))
print("Data after duplicate removal: ",len(data))
fd = open("merged_data.txt","w")
for line in data:
	line=line.strip()
	if line:
		fd.write(line+"\n")
fd.close()