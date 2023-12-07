import mysql.connector
import os
DB_HOST = os.getenv("DB_HOST", "serverless-1-instance-1.cbr7wdswraiy.ap-southeast-2.rds.amazonaws.com")

def getMysqlConnection():
    return mysql.connector.connect(
        user="root", host=DB_HOST, port="3306", password="", database="pa_web"
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
