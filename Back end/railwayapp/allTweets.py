import time
import csv
import re
import sqlalchemy
from sqlalchemy import create_engine
from flask import request, Response
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json
from trainstatus.pnrstatus import pnrStatusFunc
from trainstatus.livetrainstatus import liveTrainStatusFunc

def gettweets(request) :
	from app import User,db
	
	getreq = request.get_json(force=False, silent=False, cache=True)
	getobj = json.loads(getreq)
	
	engine1	 = create_engine('sqlite:///example.db')
	con1 = engine1.connect()
	
	pnr =sta = train = None
	p1 = [None, None, None]
	s1 = None
	trainstartdate = time.strftime("%d/%m/%Y")
	
	pnr1 = re.findall(r"\D(\d{10})\D",getobj['tweet'])
	train1 = re.findall(r"\D(\d{5})\D",getobj['tweet'])
        pnr=' '.join(pnr1)
        train=' '.join(train1)
	
	if pnr != None :
		
		p1 = pnrStatusFunc(pnr)
		
		if p1 != None :
			s1= liveTrainStatusFunc(p1[0], trainstartdate)
			
		if(s1 != None) :
			chatreguser = User(comp_department=getobj['label'], comp_query= getobj['tweet'], comp_email="na", comp_pts=pnr, comp_train_no=p1[0], comp_train_name=p1[1], comp_seat_no=p1[2], 				comp_station=s1, comp_link="na", comp_resolve=False, comp_new=True)
		
	elif train != None :
		getstatus = liveTrainStatusFunc(train, trainstartdate)
			
		if(getstatus != None) :	
			chatreguser = User(comp_department=getobj['label'], comp_query= getobj['tweet'], comp_email="na", comp_pts="na", comp_train_no="na", comp_train_name=train, comp_seat_no="na", 				comp_station=getstatus,comp_link="na", comp_resolve=False, comp_new=True)
		
	con1.close()
	return Response(status=200)
