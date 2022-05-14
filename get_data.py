from distutils.command.build_scripts import first_line_re
import sgs
import pyodbc 
from datetime import datetime
import math
import pandas as pd

import sys

start = sys.argv[1]
end = sys.argv[2]

server = 'tcp:localhost' 
database = 'sucri' 
username = 'sa' 
password = 'mssql1Ipw' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
    
format_date = "%Y/%m/%d %H:%M:%S"

def get_series_metadata():
    codes_response = []
    results = []
    series_fail = []
    print("Searching range: ", start, end)
    for serie in range(int(start), int(end), 1):
        results = sgs.search_ts(serie, language = "pt")
        print('######################################################')
        print('Searching code: {}'.format(serie))
        if results:
            print('------------------------------------------------------')
            codes_response.append(serie)
            print(serie)
            print(results[0]["frequency"])
            # if results[0]["frequency"] == 'M':
            code = results[0]["code"]
            name = str(results[0]["name"])
            unit = str(results[0]["unit"])
            frequency = str(results[0]["frequency"])
            first_value = str(results[0]["first_value"])
            last_value = str(results[0]["last_value"]) if not str(results[0]["last_value"]) == '-' else ''
            source = str(results[0]["source"])
            query = "INSERT INTO SGS.series_meta (code, name, unit, frequency, first_value, last_value, source) VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}');".format(
                code, name, unit, frequency, first_value , last_value, source)
            print(query)
            cursor.execute(query)
            record_id = cursor.execute('SELECT @@IDENTITY AS id;').fetchone()[0]
            print("record_id: ", record_id)
            cnxn.commit()  
            get_series_data(record_id, results[0]["code"], series_fail)
    print('######################################################')
    f = open("codes_found-{}.txt".format(datetime.now()), "w")
    f.write(str(codes_response))
    f.close()
    print(codes_response)
    f = open("series_fail-{}.txt".format(datetime.now()), "w")
    f.write(str(series_fail))
    f.close()
    print(series_fail)
    print('######################################################')
            
            
def get_series_data(record_id, code, series_fail):
    print(record_id, code)
    try:
        df = sgs.dataframe([code], start='02/01/2017', end='31/12/2030')
    except:
        series_fail.append(code)
        return
    for row in df.iterrows():
        value_number = float(row[1]) if not math.isnan(float(row[1])) else -1
        value_date = str(row[0])
        print(code, value_number, value_date, record_id)
        query = "INSERT INTO SGS.series_data (code, value_number, value_date, meta_id) VALUES ({}, {}, '{}', '{}');".format(
                code, value_number, value_date, record_id)
        print(query)
        cursor.execute(query) 
        cnxn.commit()



def set_inatives():
        query = "EXEC SGS.get_inactives;"
        cursor.execute(query) 
        for row in cursor.fetchall():
            query = "UPDATE SGS.series_meta SET active = 0 WHERE code = {};".format(row[0])
            print(query)
            cursor.execute(query) 
            cnxn.commit()

get_series_metadata()
set_inatives()
