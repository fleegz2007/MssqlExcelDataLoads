import config
import sys
import sqlScripts
import excelScripts

conn = sqlScripts.create_connection(config.driver, config.server, config.database)
cur = conn.cursor()

datalist = excelScripts.extractExcel(config.landingzone+config.interchangefilename)
print('Extracted all data from Excel document')
sqlScripts.masterinsert(conn, cur, config.table1 , datalist, config.landingzone+config.interchangefilename)
print('Data loaded. Deleting any null rows')
sqlScripts.cleanSqlLoad(conn, cur, config.table1)
print('Complete!')

datalist = excelScripts.extractExcel(config.landingzone+config.mdfilename)
print('Extracted all data from Excel document')
sqlScripts.masterinsert(conn, cur, config.table2, datalist, config.landingzone+config.interchangefilename)
print('Data loaded. Deleting any null rows')
sqlScripts.cleanSqlLoad(conn, cur, config.table1)
print('Complete!')

sys.exit()





