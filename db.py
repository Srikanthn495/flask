from flask_mysqldb import MySQL
import logging

def db_con(app):
    """ This function is used to connect database and return the cursor """
    try:
        app.config["MYSQL_HOST"] = 'localhost'
        app.config["MYSQL_USER"] = 'root'
        app.config["MYSQL_PASSWORD"] = ''
        app.config["MYSQL_DB"] = 'school'
        db_conn = MySQL(app)

        if db_conn:
            logging.info("DB connected")
        else:
            logging.info("DB not connected")
    
        cur = db_conn.connection.cursor()
    
        if cur:
            logging.info("cur is created")
        else:
            logging.info("cur is not created")
        return cur
    except :
        logging.error("there is an error on db connection at db.py")