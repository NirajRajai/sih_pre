import sqlalchemy
from sqlalchemy import create_engine
from flask import request, Response
import json


def shawResolved(request) :
	if request.method == 'GET' :
		from app import User,db
		
		apptid = int(request.args.get('id'))
		
		eng = create_engine('sqlite:///example.db')
		con = eng.connect()
		
		resolved = User.query.filter_by(id = apptid, comp_resolve = True).all()
		
		return Response(status=200)
