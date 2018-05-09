from flask import request, Response
import json

def praChat(request, chatobj) :
	from app import User,db
	
	idemail = chatobj['result']['parameters']['email']
	
	s7=User.query.filter_by(id = idemail)
        
        jsan = { displayText : 'Your complain has been successfully resolved',
				data : {
					facebook : 'Your complain has been successfully resolved'
				}	
			}
        
        return Response(jsan, content_type="application/json")
       	
