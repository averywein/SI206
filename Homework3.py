# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
import nltk # requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random

print("START*******")

# import nltk
nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize
from nltk.book import text2


debug = False #True

# get file from user to make mad lib out of
if debug:
	print ("Getting information from file madlib_test.txt...\n")

tokens = text2[0:150]

# print("TOKENS")
# print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print("TAGGED TOKENS")
# print(tagged_tokens)
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:5]:
		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PRP$":"pronoun"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "PRP$":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))

print("\n\nEND*******")

#Part B
import requests
from bs4 import BeautifulSoup
import re


base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')


# word = soup.find_all('p')
# for elt in word:
# 	element = elt.text
# 	paragraph = re.findall('student', element)
# 	print (paragraph)
# 	element = re.sub('student', 'AMAZING student', element)
# 	print (element)

link = soup.find_all('img')

for a in link:
	href = a["src"]
	if (href) == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		# print (href)
		a["src"] = "https://scontent-ord1-1.xx.fbcdn.net/v/t1.0-9/12821478_10206119180719270_8945575614241860663_n.jpg?oh=5bec14975b22b378b095c5f0c9be0e31&oe=589765EA"
		# print(a["src"])

for a in link:
	href = a["src"]
	if not href.startswith("https:"):
		print("before changing",a["src"])
		a["src"] = "https://raw.githubusercontent.com/cvanlent/SI206/master/HW3-StudentCopy/media/logo.png"
		print(a["src"])

result = str(soup)

element = soup.prettify()
htmlcode = re.sub('student', 'AMAZING student', element)
htmlcode = re.sub ('students', 'AMAZING students', element)

f = open("project.html", "w")
f.write(htmlcode)
f.close()

#Part C
import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "791353066612224000-8X2ZLy6ZXe0Hcs0Yet5Rw0jYCi3i96e"
access_token_secret = "FtJzRNSTabKedppBg7P25loeF08emDPXFf3dNRwlY3dd6"
consumer_key = "dPHhI8kGXbWv3zZcWGlQD1Ebx"
consumer_secret = "QomDeBs0IlKRP5MPTdiUwBx1mBV8Ynl74NDowuj3OyQp4XFGQe"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

img = "/Users/averywein/Desktop/picture.jpg"
api.update_with_media(img, status="Coding is fun! I love gamedays! #UMSI-206 #Proj3")


public_tweets = api.search('Go Blue!')

accum = 0
accum2 = 0
accum3 = 0

for tweet in public_tweets:
	print(tweet.text)
	accum += 1
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	original = analysis.sentiment.polarity
	accum3 += original
	original2 = analysis.sentiment.subjectivity
	accum2 += original2
total = accum2/accum
total2 = accum3/accum

print("Average subjectivity is")
print (total)
print("Average polarity is")
print (total2)







