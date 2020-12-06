import mysql.connector
import os
import logging


class DB_connection:
    def __init__(self):
        self.host = os.environ.get('HOST', 'mysql')
        self.user = os.environ.get('DB_USER', 'root')
        self.password = os.environ['MYSQL_ROOT_PASSWORD']


        self.mydb = mysql.connector.connect(user=self.user,
                                            password=self.password,
                                            host=self.host)
        self.mycursor = self.mydb.cursor()
        #print('db connection constructor created')
        logging.debug('db connection constructor created')

    def execute_query(self, query):
        self.mycursor.execute(query)
        myresult = self.mycursor.fetchall()
        return myresult

    def clone_db_cursor(self):
        self.mycursor.close()
        self.mydb.close()
        #print('db_cursor destroyed')
        logging.debug('db_cursor destroyed')
        
        

