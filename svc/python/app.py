import os
from flask import Flask,render_template
import boto3
import psycopg2
import sys
import json 

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello from python copilot'

@app.route('/db')
def connection():
    db_info=json.loads(os.environ['DB_INFO'])
    
    try:
        conn = psycopg2.connect(dbname=db_info["dbname"],
                        user=db_info["username"],
                        host=db_info["host"],
                        password=db_info["password"],
                        port=db_info["port"])
        
        conn.close()
        return f'connected to {db_info["host"]}'
    except Exception as e:
        err_type, err_obj, traceback = sys.exc_info()
        err_msg = f'traceback: {traceback}<br> type: {err_type}<br> obj:{err_obj}'
        return f'{err_msg}'