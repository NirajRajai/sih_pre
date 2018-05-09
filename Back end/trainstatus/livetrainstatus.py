import json
import requests

def liveTrainStatusFunc(tno, tjdate) :
	railapilive = "https://api.railwayapi.com/v2/live/train/" + str(tno) + "/date/" + tjdate + "/apikey/dyi51bc7th/"
	getlive = requests.get(url=railapilive).json()
			
	if(request.status == 200) :
		liveobj = json.loads(getlive)
			
		i = 0
			
		for platform in liveobj['route'][i] :
			if platform['has_arrived'] == True and platform['has_departed'] == False:
				upcoming_station = platform[i]['station'][0]['name'];
				break
			elif platform['has_arrived'] == True and platform['has_departed'] == True :
				upcoming_station = platform[i+1]['station'][0]['name'];
			i+=1;
						
		return upcoming_station
	else :
		return None
