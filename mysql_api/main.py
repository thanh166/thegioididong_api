import mysql.connector
from fastapi import FastAPI,Path
import json
import requests


app = FastAPI()

cnx = mysql.connector.connect(
    user='root', 
    password='psw123', 
    port='3306',
    host='127.17.0.2',
    database='thegioididong_db'
    )
cursor = cnx.cursor()

@app.get("/insertRecord/{new_title}/{new_price}/{images}")
def insertData(new_title: str, new_price: str,images: str):
    sql = f"INSERT INTO product (title, price,images) VALUES ('{new_title}', '{new_price}','{images}')"
    cursor.execute(sql)
    cnx.commit() 
    # cursor.close()
    # cnx.close()
    return 'ok'

@app.get("/searchData/{data}")
def getData(data: str):
    sql = f"SELECT * FROM product WHERE title LIKE '%{data}%'"
    cursor.execute(sql)
    result = cursor.fetchall()
    list = []
    for x in result:
        list.append(x)
    #cursor.close()   
    #cnx.close()
    return list   
# @app.get("/insertData")
# def insertData():
#     response = requests.get("http://0.0.0.0:8001/getData")
#     data = response
#     result = [(item['name'], item['price'], item['image']) for item in data]
#     add_data = (f"INSERT INTO product "
#     "(title, price,images) "
#     "VALUES (%s, %s, %s)")
#     cursor.executemany(add_data, result)
#     cnx.commit()
#     #cursor.close()
#     #cnx.close()  
#     return "ok"  

@app.get("/getData")
def getData():
    sql = "SELECT * FROM product;"
    cursor.execute(sql)
    result = cursor.fetchall()
    list = []
    for x in result:
        list.append(x)
    #cursor.close()   
    #cnx.close()
    return list
