import json
import pdb
afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.


stream_data = open("problem_1_submission - Copy.txt")
tweets = [] # initialize an empty list
for tweet in stream_data:
    line = tweet.splitlines()
    tweets.extend(line)

# each tweets is a dictionary

def clean_word(word):
	return word.lower().strip('.,"[]\'\n?!-_()$%~*+&/@')

# words_list is a list of lists of the words in each tweet 
words_list = []
for i in range(len(tweets)):
	j = json.loads(tweets[i])
	if 'text' in j.keys():
		words_list.append(j['text'].split())

i = 0
t_score = 0
for i in range(len(words_list)):
	for w in words_list[i]:
		if clean_word(w) in scores.keys():
			t_score = t_score + scores[w]
i +=1
# for w in words:
# 	if clean_word(w) in scores.keys():
# 		print w + scores[clean_word(w)]
# else:
# 	print 'nope'

print t_score

#unicode warning: unicode equal comparison failed to convert both argments to unicode