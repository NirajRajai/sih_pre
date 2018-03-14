from birdy.twitter import StreamClient, UserClient
import io
import re

ACCESS_TOKEN = '969576094407057408-UPSzwvMLEcYNIe2nAewlX56vIdYUtyl'
ACCESS_SECRET = 'Rq5fDXOF6AMKZx7nLJo7XFo8xFN1lLPlTqnaDLXlP1hcK'
CONSUMER_KEY = 'i1uLbgbfigwhDPaqEd2FFhFaF'
CONSUMER_SECRET = 'WzKU46BZloHztcHzRkUfRZaJ5Pqt6VSsAucQ4eJBsWGZalKDiu'

client = StreamClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

resource = client.stream.statuses.filter.post(track='India')


with open("tweet.txt", "a") as file:
    for data in resource.stream():
        text = data.text
        if not data.text.startswith('RT'):
            print ("------------------------------------------------------------------------")
            print (data)
            print ("------------------------------------------------------------------------")
            print("\n"+text+"\n")
            if data.truncated == True:
                print ('===================================================================================')
                text=data.extended_tweet.full_text
                print (text)
                print('====================================================================================\n\n\n')
            text = str(text.encode('utf-8'))
            text = re.sub(r'[@,\\,#]\w+',"",text[2:-1])
            file.write(text + '\n')
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n' + text + '\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                
                
    

