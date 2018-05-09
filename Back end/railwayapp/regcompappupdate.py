from flask import request, Response
from flask_json import FlaskJSON, JsonError, json_response, as_json
import sqlalchemy
from sqlalchemy import create_engine
import json
from fetchtweet.collecttweets import storeTweet

def updateComp(request) :
	from app import User,db
	if request.method == 'GET' :
		
		appupcrt = str(request.args.get('created'))
		appupreq = str(request.args.get('department'))
		
		#storeTweet()
		
		if appupcrt == 'False' :
			notresolvedu = User.query.filter_by(comp_resolve = False, comp_new = True, comp_department = appupreq).all()
		
			eng = create_engine('sqlite:///example.db')
			con = eng.connect()
		
			for d in notresolvedu :
    				s3=User.query.filter_by(comp_resolve=False, comp_new = True, comp_department = appupreq)
        			s3.comp_new=False
        			db.session.commit()
        	
        			#con.commit()
        			
			#con.close()
		
			empListu = []
		
			for emp in notresolvedu :
    				empDict = {
        				'id' : emp.id,
        				'department': emp.comp_department,
        				'query' : emp.comp_query,
        				'email' : emp.comp_email,
        				'pts' : emp.comp_pts,
        				'train-no' : emp.comp_train_no,
        				'train-name' : emp.comp_train_name,
        				'seat-no' : emp.comp_seat_no,
        				'station' : emp.comp_station,
        				'link' : emp.comp_link,
        				'resolved' : emp.comp_resolve,
        				'new' : emp.comp_new
        			}
    			
    				empListu.append(empDict)
		
			empjsonu = json.dumps(empListu)
			
			return Response(empjsonu, content_type="application/json")
		return "hello"
	return "hel"
