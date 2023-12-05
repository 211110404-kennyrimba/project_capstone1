import mysql.connector


def getMysqlConnection():
    return mysql.connector.connect(
        user="root", host="localhost", port="3306", password="", database="pa_web"
    )


def getData(sqlstr):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute(sqlstr)
    data = cur.fetchall()
    return data


def execute(sqlstr):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute(sqlstr)
    db.commit()


def getOneData(sqlstr):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute(sqlstr)
    data = cur.fetchone()
    return data
