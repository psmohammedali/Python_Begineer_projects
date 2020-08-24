import sqlite3

DB = "todo.db"    # Database name
table_name = 'tasks'   # table name in the db
conn = sqlite3.connect(DB) # open connection
c = conn.cursor()

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS '+ table_name + \
          '(ID INTEGER PRIMARY KEY AUTOINCREMENT, ' \
          'TaskName Text)'
    c.execute(sql)

def data_entry(task):
   # sql = 'INSERT INTO '+table_name + '(TaskName) VALUES (?),', [task]
    c.execute('INSERT INTO '+ table_name + '(TaskName) VALUES (?)', [task])
    conn.commit()
    print(task + " had been added successfully in "+table_name+ " database. ")

def print_data():
    sql = "SELECT * FROM "+table_name
    c.execute(sql)
    print(c.fetchall())

def delete_task(index):
    c.execute('DELETE FROM '+ table_name + ' WHERE ID = ? ', (index, ))

def closeconection():
    c.close()
    conn.close()



