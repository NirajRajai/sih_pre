from flask import request, Response
from sqlalchemy import create_engine

def setOld(request) :
	from app import User,db
	if request.method == 'GET' :
		markid = str(request.args.get('id'))
	
		engine = create_engine('sqlite:///example.db')
		con = engine.connect()
		
		s6 = User.query.filter_by(id = markid).first()
        	s6.comp_new=False
        	db.session.commit()
        	
        	con.close()
        	return Response(status=200)
