import sqlScripts
import config

def createhdctTable():
    sql_create_ichg_table = "CREATE TABLE " + config.table1 + """ (
                                    
                                );"""

    # create a database connection
    sql_create_detail_table = "CREATE TABLE  " + config.table2 + """ (
                                    
                                                        );"""

    conn = sqlScripts.create_connection(config.driver, config.server, config.database)
    cur = conn.cursor()
    # create tables
    if conn is not None:
        # create headcount table
        cur.execute(sql_create_ichg_table)
        cur.execute(sql_create_detail_table)
        cur.commit()
        cur.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    createhdctTable()
