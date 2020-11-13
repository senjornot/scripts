import os
path = "D:\\1\\2\\"
listOfFiles = os.listdir(path)
countOfFiles = len(listOfFiles)
for i in range(0, countOfFiles):
	os.rename(path+listOfFiles[i], '[python] '+listOfFiles[i]+'.pdf')