import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
APIurl = os.getenv("API_URL", "https://0.0.0.0:8000/api/")

print("DB HOST : ", DB_HOST)
print("API_URL : ", APIurl)
print("DB USER : ", DB_USER)
print("DB PASSWORD : ", DB_PASSWORD)


def getMysqlConnection():
    return mysql.connector.connect(
        user=DB_USER, host=DB_HOST, port="3306", password=DB_PASSWORD, database="pa_web"
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
