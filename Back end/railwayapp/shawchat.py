import json
from sqlalchemy import create_engine
from flask import request, Response

def setResolved(request) :
	from app import User,db
	
	if request.method == 'GET' :
		getid = int(request.args.get('id'))
		
		en = create_engine('sqlite:///example.db')
		conn = en.connect()
		
		s5 = User.query.filter_by(id = getid)
		
		s5.comp_resolve = True
		
		return Response(status=200)
