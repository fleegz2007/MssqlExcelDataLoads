import config
import sqlScripts
import excelScripts

conn = sqlScripts.create_connection(config.driver, config.server, config.database)
cur = conn.cursor()

datalist = excelScripts.extracthdct()
print('Extracted all data from Excel Document')
sqlScripts.masterinsert(conn, cur, datalist)




