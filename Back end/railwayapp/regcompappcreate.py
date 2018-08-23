from flask import request, Response
from flask_json import FlaskJSON, JsonError, json_response, as_json
import sqlalchemy
from sqlalchemy import create_engine
import json
from fetchtweet.collecttweets import storeTweet

def shawCompunre(request) :
	from app import User,db
	if request.method == 'GET' :
		
		appcrtreq = str(request.args.get('created'))
		appcrtobj = str(request.args.get('department'))
		#print(appcrtreq)
		#print(appcrtobj)
		#users=User.query.all()
		#print(users)
		#storeTweet()
		
		if appcrtreq == 'True' :
			notresolved = User.query.filter_by(comp_resolve = False, comp_department = appcrtobj).all()
	
			empList = []
		
			for emp in notresolved :
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
    			
    				empList.append(empDict)
		
			empjson = json.dumps(empList)
		
			return Response(empjson, content_type="application/json")
		return "outside"
