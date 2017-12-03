try:
	f = open(r'c:\test.txt','r')
	print(f.read())
finally:
	if f:
		f.close()

with open(r'c:\test.txt','r') as fileReader:
	print(fileReader.read())

# with open(r'c:\test.txt','r') as fileReader:
# 	for line in fileReader.readline():
# 		print(line.strip())

# f = open(r'c:\test.txt','w')
# f.write('写入')
# f.close()

# with open(r'c:\test.txt','r') as fileReader:
# 	print(fileReader.read())

with open(r'c:\test.txt','w') as fileWriter:
	fileWriter.write('something')