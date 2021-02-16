import pyodbc
import excelScripts
import establishtables
import config


def create_connection(driver, server, database):
    #create a database connection localhost
    cnxn = pyodbc.connect('DRIVER='+driver+';'
                          'SERVER='+server+';'
                          'DATABASE='+database+';'
                          'Trusted_Connection=yes;')##Use trusted connection only if using a local server
    return cnxn

def insertText(cur, tablename):
    cur.execute('SELECT * FROM '+tablename+';')
    names = list(map(lambda x: x[0], cur.description))
    strfields = ''
    for field in names:
        strfields+=field+', '
    strfields = strfields[:-2]
    strfields = "(" + strfields + ")"
    qmarks = ' VALUES ('
    for i in range(len(names)):
        qmarks+='?, '
        i+1
    qmarks = qmarks[:-2]
    qmarks = qmarks +');'
    return strfields + qmarks


def fieldnames(cur, tablename):
    cur.execute('SELECT * FROM '+tablename+';')
    names = list(map(lambda x: x[0], cur.description))
    strfields = ''
    for field in names:
        strfields+=field+' IS NULL AND '
    strfields = strfields[:-5]
    return strfields


def variables(datalist):
    dataliststr = []
    for i in range(len(datalist[0])):
        dataliststr.append([])
        for j in range(len(datalist)):
            dataliststr[i].append(datalist[j][i])
    return dataliststr


def masterinsert(conn, cur, tablename, datalist, filepath):
    try:
        print("Inserting data into table "+tablename+" ...")
        datalist = variables(datalist)
        for i in range(len(datalist)):
            cur.execute('INSERT INTO ' + tablename +' '+ insertText(cur, tablename), datalist[i])
            conn.commit()
    except:
        print('Error inserting data. Running debug:')
        debugTypeCast(conn, cur, tablename, datalist, filepath)

def cleanSqlLoad(conn, cur, tablename):
    fieldname = fieldnames(cur, tablename)
    cur.execute('DELETE FROM '+tablename+ ' WHERE ' + fieldname + ';')
    cur.commit()


def debugTypeCast(conn, cur, tablename, datalist, filepath):
    cur.execute('SELECT * FROM '+tablename+';')
    colname = list(map(lambda x: x[0], cur.description))
    coltype = list(map(lambda x: x[1], cur.description))
    #for i in range(len(colname)):
    #    print(colname[i] + ' - ' + str(coltype[i]))
    datalist = variables(datalist)
    exceltype = []
    excelname = excelScripts.colNames(filepath)
    for val in datalist[0]:
        exceltype.append(type(val))
    if len(colname) != len(excelname):
        print('ERROR: NUMBER OF COLUMNS IN THE EXCEL FILE DOES NOT MATCH COLUMNS IN THE DATABASE')
    if len(colname) == len(excelname):
        for i in range(len(coltype)):
            if coltype[i] != exceltype[i]:
                print('ERROR: TYPE CAST IN SQL TABLE COLUMN ' + colname[i] + ' ' + (str(coltype[i])) + ' DOES NOT MATCH EXCEL COLUMN ' + excelname[i] + ' ' + (str(exceltype[i])))
    print("Debug Complete")
    
    
    
    






