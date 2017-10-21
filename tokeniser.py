import sys # file ready stuff
# read in all the lines into a list
text = sys.stdin.readlines()
# variable for storing the sentence id
sentence_id = 1
# for each of the lines in the input
for line in text:
	line = line.strip()
	if line == '':
		continue

	# print out a comment with the sentence id
	print('# sent_id =:%d' % sentence_id)
	# this is a variable for storing the token id   
	print('# text = %s' % (line.strip()))
	blah = 0
	# make a list of all the kinds of punctuation
	punctuation = ['.', ',', '?', '!', ':', ';']
	# for each of the punctuation symbols, place a space before it 
	for turtles in punctuation:
		line = line.replace(turtles, ' ' + turtles)
	# make a list of tokens from the line
	tokens = line.split(' ')
	# fo each of the tokens in the line
	for token in tokens:
		if token.strip() == '':
			continue
		# print out the token and token id 
		# increment the token id by one
		blah = blah + 1
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (blah, token))
#		print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (blah, token, '_', '_', '_', '_', '_', '_', '_', '_'))
	
	# increment the sentence id by one
	sentence_id = sentence_id + 1
	print()
