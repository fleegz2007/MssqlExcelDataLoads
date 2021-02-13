import pyodbc
import config


def create_connection(driver, server, database):
    #create a database connection localhost
    cnxn = pyodbc.connect('DRIVER='+driver+';'
                          'SERVER='+server+';'
                          'DATABASE='+database+';'
                          'Trusted_Connection=yes;')##Use trusted connection only if using a local server
    return cnxn


def fieldnames(cur):
    tablenames = '''SELECT * FROM tablename;'''
    cur.execute(tablenames)
    names = list(map(lambda x: x[0], cur.description))
    print(names)


def masterinsert(conn, cur, datalist):
    print("Inserting data into table...")
    for i in range(len(datalist[0])):
        cur.execute('''INSERT INTO field1, field2, field3 VALUES (?, ?, ?);''', (datalist[0][i], datalist[2][i], datalist[3][i]))
        conn.commit()


    
    
    
    
    






