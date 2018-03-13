from birdy.twitter import StreamClient, UserClient
import io

ACCESS_TOKEN = '969576094407057408-UPSzwvMLEcYNIe2nAewlX56vIdYUtyl'
ACCESS_SECRET = 'Rq5fDXOF6AMKZx7nLJo7XFo8xFN1lLPlTqnaDLXlP1hcK'
CONSUMER_KEY = 'i1uLbgbfigwhDPaqEd2FFhFaF'
CONSUMER_SECRET = 'WzKU46BZloHztcHzRkUfRZaJ5Pqt6VSsAucQ4eJBsWGZalKDiu'

client = StreamClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

resource = client.stream.statuses.filter.post(track='India')

with open("tweet.txt", "a") as file:
    for data in resource.stream():
        if 'RT @' not in data.text:
            print (data.text+"\n\n\n")
            file.write(data.text)
    

