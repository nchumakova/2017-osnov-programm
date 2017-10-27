
import sys
#read all input lines
vocab = sys.stdin.readlines()
#create map, define dict to hold translit table
table = {}
def classify(word):
	# word = input word to the function, e.g. theos
	# output = list of features
	word = word.replace("́́´","")
	output = ['Gender=?', 'Number=?', 'Case=?']
	if word[-2:] == 'ός' and word[-4:] != 'ατος':
		output = ['Gender=m/f/n', 'Number=sg', 'Case=_']
	if word[-2:] == 'ης':
		output = ['Gender=_', 'Number=sg', 'Case=_']
	if word[-2:] == 'ας' and word[-3:] != 'εας':
		output = ['Gender=m/f', 'Number=sg', 'Case=nom if m/gen if f']
	if word[-3:] == 'εας':
		output = ['Gender=m', 'Number=sg', 'Case=nom']
	if word[-2:] == 'ου' and word[-3:] != 'ιου':
		output = ['Gender=m/f/n', 'Number=?sg', 'Case=gen']
	if word[-1] == 'η':
		output = ['Gender=_', 'Number=_', 'Case=_']
	if word[-1] == 'α' and word[-2:] != 'εα':
	        output = ['Gender=_', 'Number=_', 'Case=_']
	if word[-2:] == 'εα':
	        output = ['Gender=m', 'Number=sg', 'Case=gen/acc/voc']
	if word[-1] == 'ο':
	        output = ['Gender=m/f/n', 'Number=sg', 'Case=acc/(nom if neu)']
	if word[-1] == 'ε':
	        output = ['Gender=m/f', 'Number=sg', 'Case=voc']
	if word[-2:] == 'οι':
	        output = ['Gender=m/f', 'Number=pl', 'Case=nom']
	if word[-2:] == 'ες' and word[-4:] != 'αδες':
	        output = ['Gender=m/f', 'Number=pl', 'Case=nom/acc']
	if word[-3:] == 'εις':
	        output = ['Gender=m/f', 'Number=pl', 'Case=nom/acc']
	if word[-4:] == 'αδες':
	        output = ['Gender=m', 'Number=pl', 'Case=nom/acc']
	if word[-2:] == 'ων' and word[-3:] != 'ιων' and word[-4:] != 'ατων':
	        output = ['Gender=m/f/n', 'Number=pl', 'Case=gen']
	if word[-3:] == 'ους':
	        output = ['Gender=m/f/n', 'Number=pl/(sg if neut)', 'Case=acc/(gen if neut)']
	if word[-2:] == 'ης':
	        output = ['Gender=f', 'Number=sg', 'Case=gen']
	if word[-1] == 'ι':
	        output = ['Gender=n', 'Number=sg', 'Case=nom/acc']
	if word[-3:] == 'ατα':
	        output = ['Gender=n', 'Number=pl', 'Case=nom/acc']
	if word[-3:] == 'ιου':
	        output = ['Gender=n', 'Number=s', 'Case=gen']
	if word[-4:] == 'ατος':
	        output = ['Gender=n', 'Number=sg', 'Case=gen']
	if word[-2:] == 'ια':
	        output = ['Gender=n', 'Number=pl', 'Case=nom/acc']
	if word[-3:] == 'ιων':
	        output = ['Gender=n', 'Number=pl', 'Case=gen']
	if word[-4:] == 'ατων':
		output = ['Gender=n', 'Number=pl', 'Case=gen']
	return '|'.join(output)
for a in vocab:
	a = a.strip()
	if a.count('\t') != 9:
		print(a) #print it out
		continue #move on to next line
	line = a.split('\t') #take every line and make it into list splitting on the tab
	form = line[1]
	if line[3] == 'NOUN':
		line[6] =classify(form)
		#if the line has noun in it, then print out 
	#puts it into a string from a list
	print('\t'.join(line))
