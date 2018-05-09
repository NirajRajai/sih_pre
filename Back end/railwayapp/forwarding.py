import sqlalchemy
from sqlalchemy import create_engine
from flask import request, Response
import json

def forward(request) :
	fid = str(request.args.get('id'))
	fdept = str(request.args.get('department'))
	
	f = User.query.filter_by(id = fid).first()
	f.comp_department = fdept
	
	return Response(status=200)
