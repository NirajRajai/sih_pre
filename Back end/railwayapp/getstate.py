import sqlalchemy
from sqlalchemy import create_engine
from flask import request, Response
import json

	
def showResolved(request) :
	from app import User,db
	if request.method == 'GET' :
		
		appshawdept = str(request.args.get('department'))
	

		showresolved = User.query.filter_by(comp_resolve = True, comp_department = appshawdept).all()
		
		empList = []
		
		for emp in showresolved :
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
		
		shawson = json.dumps(empList)
		
		return Response(shawson, content_type="application/json")
	

