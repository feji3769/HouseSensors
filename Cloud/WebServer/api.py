import flask
from flask import request, jsonify
#from flask_mysqldb import MySQL
import sys
sys.path.append("/home/felix/Documents/HouseSensors/Cloud")
from Database.InsertData.insertJson import insert_json
from Database.ReadData.readMySql import select_record


app = flask.Flask(__name__)
app.config["DEBUG"] = True

#app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password'
#app.config['MYSQL_DB'] = 'hello_db'
#mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/sensor', methods=['GET', 'POST'])
def api_all():

    if request.method == "GET":
       return jsonify(select_record())
    elif request.method == "POST":
        data = request.data
        print(data)
        insert_json(data)
        return "that worked!"
        
    else:
        return "Nothing found."





app.run()