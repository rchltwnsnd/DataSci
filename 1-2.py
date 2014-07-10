import json

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

i = 0
wtf = []
while i < 5:
    j = json.loads(tweets)
    if 'text' in j.keys():
      wtf.extend(j['text'])
    i +=1

print wtf
