from functions import *

def connection():
     return mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="forumweb-db"
     )