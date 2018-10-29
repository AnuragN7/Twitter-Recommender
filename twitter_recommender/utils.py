import twitter
import nltk 
import json 
import collections

# Some starter code to the get the twitter api up and running

data = dict()
with open('credentials.json') as data_file:
	data = json.load(data_file) 

auth = twitter.oauth.OAuth(data['OAUTH_TOKEN'], data['OAUTH_TOKEN_SECRET'], data['CONSUMER_KEY'], data['CONSUMER_SECRET'])
api = twitter.Twitter(auth=auth) 

def get_hashtags(screen_name):
	""" Returns the 10 most common hashtags for a specific user 

	Args:
	screen_name: The screen_name of the twitter user we are interested in """
	
	statuses = api.statuses.user_timeline(screen_name=screen_name) # Get the 'n' most recent tweets of the user in question 
	hashtag_lst = [] # This will hold all the most common hashtags of the user concerned 
	for status in statuses:
		for item in status['entities']['hashtags']: # iterate through list of dictionaries 
			hashtag_lst.append(item['text']) # Get the hashtag 
		 
	return hashtag_lst 
	
def get_most_common_hashtag(hashtag_lst):
	""" Returns the most popular hashtag of a twitter user 
	
	Args: 
	hashtag_lst = a list of hashtags
	"""
	
	hashtag_fdist = nltk.FreqDist(hashtag_lst) # Obtain a frequency distribution from the hashtag_lst
	return hashtag_fdist.max() # Return the most commonly occuring hashtag


def get_similar_users(screen_name):
	""" Returns a list of 'person' named tuples. Each person represents a
	    twitter user with interests similar to the target user 
	
	Args:
	screen_name: the twitter_handle of the target_user
	"""
	
	hashtag_lst = get_hashtags(screen_name) 
	mc_hashtag = get_most_common_hashtag(hashtag_lst)
	tweets = api.search.tweets(q="#" + mc_hashtag, count=20) # Search the twitter verse for users who have used the same 
						       # hashtag in their tweets
	twitter_users = [status['user']['screen_name'] for status in tweets['statuses']] # Return a list of twitter screen_names
	person_lst = [] # will hold a list of 'Person' named_tuples
	for user in twitter_users:
		Person = collections.namedtuple('Person', 'name sim_score')
		person_lst.append(Person(name=user, sim_score=get_score(mc_hashtag, user)))
	return person_lst

def get_score(most_common_hashtag, user):
	""" Returns how similar a certain user is to the target user 
	
	Args:
	most_common_hashtag: The hash_tag that will serve as a reference point to calculate the user's score
	user: The user whose similarity score we want to calculate
	"""
	hashtag_lst = get_hashtags(user) 
	f_dist = nltk.FreqDist(hashtag_lst)
	raw_value = f_dist[most_common_hashtag] # Find the value in the dictionary that corresponds to the target user's most common hashtag
	if raw_value == 0: return 1
	return 1/raw_value
	
