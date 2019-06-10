import pymysql


# we will be using this function to add our offers to the DB
def addToDatabase(offer):
    # Open a database connection
    db = pymysql.connect(host="localhost",
                         user="username",
                         password="my_password",
                         db="indeed",
                         charset="utf8")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
