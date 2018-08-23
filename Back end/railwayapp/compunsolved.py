import sqlalchemy
from sqlalchemy import create_engine
from flask import request, Response
import json

def unResolved(request) :
	if request.method == 'GET' :
		from app import User,db
		
		undept = str(request.args.get('department'))
		
		eng = create_engine('sqlite:///example.db')
		con = eng.connect()
		
		unresolved = User.query.filter_by(comp_department = undept, comp_resolve = False).all()
		
  		empList = []
		
		for emp in unresolved :
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
