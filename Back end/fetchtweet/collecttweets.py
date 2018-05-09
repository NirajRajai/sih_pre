import csv
import sqlalchemy
from sqlalchemy import create_engine

def storeTweet() :
	from app import User,db
	engine1	 = create_engine('sqlite:///example.db')
	con1 = engine1.connect()
		
	with open('tweets.csv') as f:
    		
    		reader = csv.reader(f)
    		
    		for row in reader:
    			cd=''.join(row[0])
    			cq=''.join(row[1])
    			cl=''.join(row[2])
    			
    			s1=User(comp_department=cd, comp_query=cq, comp_link=cl,comp_email='adasda',comp_pts='12569',comp_train_no=None,comp_train_name='s2',comp_seat_no='s2',comp_station='Vadodara',comp_resolve=False,comp_new=True) 
			db.session.add(s1)
			db.session.commit()
		f1 = open("tweets.csv", "w")
		
	con1.close()

