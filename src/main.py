from flask import Flask 
from db_connection import DB_connection
import json
import logging

app = Flask(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

@app.route('/test')
def test():
	return "working"

@app.route('/') 
def hello_world(): 
	logging.debug('received request')
	op_res = dict()
	db_conn_obj = DB_connection()
	query = "SELECT 'Hello World!';"
	myresult = db_conn_obj.execute_query(query)
	op_res['result'] = myresult
	db_conn_obj.clone_db_cursor()
	response = json.dumps(op_res)
	logging.info('response sent: %s', response)
	return response



# main driver function 
if __name__ == '__main__': 

	# run() method of Flask class runs the application 
	# on the local development server. 
    app.run(host='0.0.0.0', port=8080, debug=True)
