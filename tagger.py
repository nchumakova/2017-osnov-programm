import sys

#open the file, ready for reading. 
fd = open('model.tsv')

for line in fd.readlines():
	line = line.strip() #take away newline characters @ beginning/end of line
	line = line.split('\t') # split the line on tab, creates a list. 
	print(line)
