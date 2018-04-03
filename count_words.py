from collections import Counter
from nltk.corpus import stopwords
f=open("final/staff_n.txt","r")

f1=open('final/staff_feature.txt','w')
w=f.read()
stop_words = list(stopwords.words('english'))
words=w.split()
filtered_words = [w for w in words if not w in stop_words]
counts=Counter(filtered_words)

for w in counts:
    f1.write(w+',')
f.close()
f1.close()