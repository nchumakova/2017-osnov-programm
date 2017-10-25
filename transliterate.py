
import sys
#read all input lines
vocab = sys.stdin.readlines()
#create map, define dict to hold translit table
table = {}

fd = open('symbols.tsv')
#go through translit table and replace any key with value
for line in fd.readlines():#this part reads the table I madea in symbols.tsv
	line = line.strip('\n')#strips line
	line = line.split('\t') #splits into tabs, makes list
#input- first line, output- second line. 
	inn = line[0]
	out = line[1]
	table[inn] = out
for a in vocab:
	a = a.strip()
	if a.count('\t') != 9:
		print(a) #print it out
		continue #move on to next line
	line = a.split('\t') #take every line and make it into list splitting on the tab
	form = line[1]
	for stuff in table:
		form = form.replace(stuff, table[stuff])
	line[9] = form 
	#puts it into a string from a list
	print('\t'.join(line))
