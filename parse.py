import re
f = open("tweet.txt","r")
data=f.read()
data=re.sub(r'[@,\\,#]\w+',"",data)
f1=open("new.txt","a")
f1.write(data)
f.close()
f1.close()