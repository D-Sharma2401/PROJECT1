import mysql.connector as db

class DBHelper:

    def __init__(self):
        #step1: create connection with database
        self.connection = db.connect(user= 'root',
                                     password='',
                                     host='127.0.0.1',
                                     database='dsharma')

        #step2: Obtain cursor to perform SQL operations
        self.cursor = self.connection.cursor()
        print("[DBHelper] Connection Created and Cursor obtained...")

    def execute_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        #stel3: Execute SQL Command
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] SQL Statement Executed...")

    def execute_select_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        # step3: Execute SQL Command
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows