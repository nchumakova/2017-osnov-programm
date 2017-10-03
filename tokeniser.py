import sys # file ready stuff
# read in all the lines into a list
text = sys.stdin.readlines()
# variable for storing the sentence id
sentence_id = 1
# for each of the lines in the input
for line in text:
        # print out a comment with the sentence id
        print('# sent_id =', sentence_id)
        # this is a variable for storing the token id   
        blah = 1
        # make a list of all the kinds of punctuation
        punctuation = ['.', ',', '?', '!']
        # for each of the punctuation symbols, place a space before it 
        for hats in punctuation:
                line = line.replace(hats, ' ' + hats)
        # make a list of tokens from the line
        tokens = line.split(' ')
        # fo each of the tokens in the line
        for token in tokens:
                # print out the token and token id 
                print('%d\t%s' % (blah, token))
                # increment the token id by one
                blah = blah + 1
        # increment the sentence id by one
        sentence_id = sentence_id + 1


