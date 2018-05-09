import json
import requests

def pnrStatusFunc(pot) :
	railapipnr = "https://api.railwayapi.com/v2/pnr-status/pnr/" + str(pot) + "/apikey/dyi51bc7th/"
	getpnr = requests.get(url = railapipnr).json()
			
	if(request.status == 200) :
		pnrobj = json.loads(getpnr)
			
		train_no = pnrobj[train][0]['number']
		train_name = pnrobj[train][0]['name']
		seat_no = pnrobj[passengers][0]['current_status']
		
		return train_no, train_name, seat_no
	else :
		return None, None, None
