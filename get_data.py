import sgs
import pyodbc 
from datetime import datetime

server = 'tcp:localhost' 
database = 'sucri' 
username = 'sa' 
password = 'mssql1Ipw' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
    
format_date = "%Y/%m/%d %H:%M:%S"

# CDI = 12
# INCC = 192  #  National Index of Building Costs
# df = sgs.dataframe([CDI, INCC], start='02/01/2018', end='31/12/2018')

# print(sgs.metadata(df))
# print('-----------------------')
# print(df.head(20))

codigos = []

for x in range(50):
  CDI_CODE = x + 1
  results = sgs.search_ts(CDI_CODE, language = "pt")
  if results:
      query = "INSERT INTO SGS.series_meta (code, name, unit, frequency, first_value, last_value, source) VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}');".format(
          results[0]["code"], str(results[0]["name"]), str(results[0]["unit"]), str(results[0]["frequency"]), 
         str(results[0]["first_value"]) , str(results[0]["last_value"]), str(results[0]["source"]))
      print(query)
      cursor.execute(query) 
      cnxn.commit()