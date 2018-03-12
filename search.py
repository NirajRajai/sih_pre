from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['RailMinIndia']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    tso.set_search_url('q=RailMinIndia&-filter:retweets&-filter:replies&tweet_mode=extended&count=1731')
    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'i1uLbgbfigwhDPaqEd2FFhFaF',
        consumer_secret = 'WzKU46BZloHztcHzRkUfRZaJ5Pqt6VSsAucQ4eJBsWGZalKDiu',
        access_token = '969576094407057408-UPSzwvMLEcYNIe2nAewlX56vIdYUtyl',
        access_token_secret = 'Rq5fDXOF6AMKZx7nLJo7XFo8xFN1lLPlTqnaDLXlP1hcK'
     )

     # this is where the fun actually starts :)
#     for tweet in ts.search_tweets_iterable(tso):
#         print( '%s' % ( tweet['text'] ) )

# except TwitterSearchException as e: # take care of all those ugly errors if there are some
#     print(e)
    todo = True
    next_max_id = 0
    i=0
    f = open('tweet.txt','a')
    # let's start the action
    while(todo):

        # first query the Twitter API
        response = ts.search_tweets(tso)

        # print rate limiting status
        #print( "Current rate-limiting status: %s" % ts.get_metadata()['x-rate-limit-reset'])

        # check if there are statuses returned and whether we still have work to do
        todo = not len(response['content']['statuses']) == 0
        
        # check all tweets according to their ID
        for tweet in response['content']['statuses']:
            tweet_id = tweet['id']
            a=str(tweet['full_text'].encode('utf-8'))
            i=i+1
            print(i)

            # current ID is lower than current next_max_id?
            if (tweet_id < next_max_id) or (next_max_id == 0):
                next_max_id = tweet_id
                next_max_id -= 1 # decrement to avoid seeing this tweet again
            
        # set lowest ID as MaxID
        tso.set_max_id(next_max_id)
    print("finished")
    f.close()
except TwitterSearchException as e:
    print(e)