from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    mysql.init_app(app)

def query_db(query, args=(), one=False):
    cur = mysql.connection.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def execute_db(query, args=()):
    cur = mysql.connection.cursor()
    cur.execute(query, args)
    mysql.connection.commit()
    cur.close()
