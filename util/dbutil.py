import mysql.connector

class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            conn = (mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port='3306',
                database="TicketBookingSystem"
            ))
            return conn
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")
            return None

