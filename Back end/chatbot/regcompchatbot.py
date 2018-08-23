import time
from flask import request, Response
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json
from trainstatus.pnrstatus import pnrStatusFunc
from trainstatus.livetrainstatus import liveTrainStatusFunc

def regComp(request, chatobj) :
	chatdep = chatobj['result']['parameters']['category']
	chatcomp = chatobj['result']['parameters']['complaint-data']
	chatem = chatobj['result']['parameters']['email']
	chatpts = chatobj['result']['parameters']['pnr']	
					
	ptlen = len(chatpts)
	pot = sta = None
		
	try:
        	pot = int(chatpts)
    	except ValueError:
        	sta = chatpts
		
	getpnr = [None, None, None] 
	getstatus = None
	getstation = None
		
	trainstartdate = time.strftime("%d/%m/%Y")
		
	if pot != None and ptlen == 10 :
		getpnr = pnrStatusFunc(pot)
			
		if getpnr != None :
			getstatus = liveTrainStatusFunc(getpnr[0], trainstartdate)
			
		if(getstatus != None) :
			chatreguser = User(comp_department=chatdep, comp_query=chatcomp, comp_email=chatem, comp_pts=chatpts, comp_train_no=getpnr[0], comp_train_name=getpnr[1], 						comp_seat_no=getpnr[2], comp_station=None, comp_link=None, comp_resolve=False, 						comp_new=True)
		
	elif pot != None and ptlen == 5 :
		getstatus = liveTrainStatusFunc(pot, trainstartdate)
			
		if(getstatus != None) :	
			chatreguser = User(comp_department=chatdep, comp_query=chatcomp, comp_email=chatem, comp_pts=chatpts, comp_train_no=None, comp_train_name=None, 						comp_seat_no=None,comp_station=getstatus,comp_link=None, comp_resolve=False, 						comp_new=True)
		
	else :
		getstation = station
		chatreguser = User(comp_department=chatdep, comp_query=chatcomp, comp_email=chatem, comp_pts=chatpts, comp_train_no=None,comp_train_name=None,comp_seat_no=None,comp_station=getstation, 					comp_link=None, comp_resolve=False, comp_new=True)
	
	successjson = { displayText : 'Your complain has been successfully registered',
				data : {
					facebook : 'Your complain has been successfully registered'
				}	
			}
		
	return Response(successjson, content_type="application/json")

