from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
from chatbot.regcompchatbot import regComp 
from railwayapp.shawcomp import praChat
from railwayapp.regcompappcreate import shawCompunre
from railwayapp.regcompappupdate import updateComp
from railwayapp.appread import setOld
from railwayapp.compunsolved import unResolved
from railwayapp.shawchat import setResolved
from railwayapp.getstate import showResolved
from railwayapp.compresol import shawResolved
from railwayapp.allTweets import gettweets
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

app.secret_key = "flask rocks!"
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, index=True, primary_key=True)
	comp_department = db.Column(db.String(20), index=True, nullable=False)
	comp_query = db.Column(db.String(280), index=True, nullable=False) 
   	comp_email = db.Column(db.String(254), index=True, default=None)
   	comp_pts = db.Column(db.String(30), index=True)
	comp_train_no = db.Column(db.Integer, index=True, default=None)
	comp_train_name = db.Column(db.String(30), index=True,  default=None)
	comp_seat_no = db.Column(db.String(30), index=True, default=None)
	comp_station = db.Column(db.String(30), index=True,  default=None)
	comp_link = db.Column(db.String(253), index=True, default=None)
	comp_resolve = db.Column(db.Boolean, index=True, default=False)
	comp_new = db.Column(db.Boolean, index=True, default=True)
	
    	def __repr__(self):
        	return '<User {}>'.format(self.id)  

@app.route('/')
def rus() :
	return "hello"
	
@app.route('/chatbotr')
def test1() :
	chatreq = request.get_json(force=False, silent=False, cache=True)
	chatobj = json.loads(chatreq)
		
	if chatobj['metadata']['intentName'] == 'compaint status email':
		praChat(request, chatobj)
	else :
		shawCompunre(request, chatobj)
			
@app.route('/cappcreate')
def test3() :
	return shawCompunre(request)
	
@app.route('/cappu')
def test3() :
	return updateComp(request)

@app.route('/cappmark')
def test4() :
	return setOld(request)
		
@app.route('/cappunresolve')
def test5() :
	return unResolved(request)	
	
@app.route('/cappshaw')
def test6() :
	return setResolved(request)
	
@app.route('/cappallresolve')	
def test7() :
	return shawResolved(request)	
	
@app.route('/cappresolve')	
def test8() :
	return forward(request)

@app.route('/gettweets')		
def test9() :
	return gettweets(request)
	
if __name__ == "__main__":
   	app.run()
   	app.debug = True
