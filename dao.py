from functions import *

def connection():
     return mysql.connector.connect(
              host="localhost",
              port=3308,
              user="root",
              password="",
              database="forumweb-db"
     )