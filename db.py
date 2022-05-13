import pyodbc 

server = 'tcp:localhost' 
database = 'sucri' 
username = 'sa' 
password = 'mssql1Ipw' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT * from SGS.series_meta;") 
row = cursor.fetchone() 
while row: 
    print(row)
    row = cursor.fetchone()
