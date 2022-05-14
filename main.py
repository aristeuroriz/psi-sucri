from flask import Flask
from flask import jsonify
import pyodbc 
from datetime import datetime
import math

server = 'tcp:localhost' 
database = 'sucri' 
username = 'sa' 
password = 'mssql1Ipw' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sgs/inactives')
def sgs_inactives():
    try:
        data = []
        query = "SELECT * FROM SGS.series_meta sm WHERE sm.active = 0;"
        print(query)
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        print(columns)
        for row in rows:
            obj = {
                columns[0]: row[0],
                columns[1]: row[1],
                columns[2]: row[2],
                columns[3]: row[3],
                columns[4]: row[4],
                columns[5]: row[5],
                columns[6]: row[6],
                columns[7]: row[7],
                columns[8]: row[8]
                }
            data.append(obj)
        return jsonify(data)
    except:
        print("exception on get inactives")
        return jsonify(Exception = "exception on get inactives")

@app.route('/sgs/actives')
def sgs_actives():
    try:
        data = []
        query = "SELECT * FROM SGS.series_meta sm WHERE sm.active = 1;"
        print(query)
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        print(columns)
        for row in rows:
            obj = {
                columns[0]: row[0],
                columns[1]: row[1],
                columns[2]: row[2],
                columns[3]: row[3],
                columns[4]: row[4],
                columns[5]: row[5],
                columns[6]: row[6],
                columns[7]: row[7],
                columns[8]: row[8]
                }
            data.append(obj)
        return jsonify(data)
    except:
        print("exception on get inactives")
        return jsonify(Exception = "exception on get inactives")

@app.route('/sgs/get_all_metadata')
def sgs_get_all_metadata():
    try:
        data = []
        query = "SELECT * FROM SGS.series_meta;"
        print(query)
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        print(columns)
        for row in rows:
            obj = {
                columns[0]: row[0],
                columns[1]: row[1],
                columns[2]: row[2],
                columns[3]: row[3],
                columns[4]: row[4],
                columns[5]: row[5],
                columns[6]: row[6],
                columns[7]: row[7],
                columns[8]: row[8]
                }
            data.append(obj)
        return jsonify(data)
    except:
        print("exception on get inactives")
        return jsonify(Exception = "exception on get all metadata")

