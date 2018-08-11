import csv
from nltk.tokenize import TweetTokenizer # doesn't split at apostrophes
import nltk
from nltk import Text
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier


from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
f1=open("final/final_test.csv","a")


print(len(words))
f_main=open('tweets.txt','r')
tweets=f.read().split('\n')
txt1 = ['His smile was not perfect', 'His smile was not not not not perfect', 'she not sang']
tf = TfidfVectorizer(smooth_idf=False, sublinear_tf=False, norm=None, analyzer='word',stopwords='english',ngram_range=(1,3),lowercase=True)
txt_fitted = tf.fit(tweets)

filenames=['food.txt','security.txt','clean.txt','booking.txt','water.txt','irctc.txt','late.txt','medical.txt']
i=1
for name in filenames:

    f=open(name,"r")
    text=f.read()
       #header=['platform','bribe','corrupt','staff','respond','bully','rpf','police','harassment','harassed','drunk','drinking','attack','stolen','theft','force','molest','robbery','badgering','lost','bother','unwanted','rude','behaviour','crime','loot','illegal','abuse','assault','harm','money','refund','bank','medical','emergency','heart', ' ill','medicines','fever','fatigue','late','delay','hrs','hour','food','unhyg','irctc','meal','bad quality','electri','charging','socket','fan','light','overpacked','more train','congested','overcrowd','crowded','packed','no space','overfilled','medical','assistance','emergency','heart','ill','medicines','fever','fatigue','booking','cancellation','allocated','toilet','dirty','filthy','cleanliness','smell','stink','clogged','choke','garbage','not clean','leakage',' bug','insects','cockroach','running','help','ticket','pnr','boarding','water','seat','berth','traveling',' ac','tte','ticket','checker',' tc','charge',' coach','official',' bad','worst','more','extra',' fare','selling','deducted','rs','fine','serious','problem','authority','bottle','vendor','stopping','broken','vacant',' rat','jammed','senior','citizen','lower','black money','door','reserved',' no','horrible','unhealthy','passenger','issue','pillow','bed','sick','boarded','outside','strict','action','many','route',' halt','sleeper','occupied','display','type']
    lines=text.split("\n")
    print(len(words))
    txt_transformed = txt_fitted.transform(lines)
    rows,columns=txt_transformed.shape
    row=np.zeros((rows,columns+1))
    row[:,:-1]=txt_transformed
    row[:,-1]=i
    #idf = tf.idf_
    #print(dict(zip(txt_fitted.get_feature_names(), idf)))

    #f2=open("none.txt","w")
    csvwriter = csv.writer(f1)
    #csvwriter.writerow(header)


    csvwriter.writerow(row)

    print(i)
    i+=1
    f.close()
f1.close()