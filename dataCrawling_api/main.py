import mysql.connector
import requests
from bs4 import BeautifulSoup
import json
from fastapi import FastAPI
app = FastAPI()

cnx = mysql.connector.connect(
    user='root', 
    password='psw123', 
    port='3306',
    host='127.17.0.2',
    database='thegioididong_db'
    )
cursor = cnx.cursor()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
# Sử dụng User-Agent khác
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"

url = 'https://www.thegioididong.com/'
category = ['dtdd/','may-tinh-bang/','laptop/']
data = []
@app.get("/getData")
def getData():
    data = []
    for i in ['dtdd','may-tinh-bang','laptop']:
        url ="https://www.thegioididong.com/"+i
        response = requests.get(url,headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('a', {'class': 'main-contain'})
        for product in products:
            name = product.find('h3').text.strip()
            price = product.find('strong', {'class': 'price'}).text.strip()
            img_tag = product.find('div', {'class': 'item-img'}).find('img', {'class': 'thumb'})
            if 'src' in img_tag.attrs:
                image = img_tag['src']
            else:
                image = img_tag['data-src']
            data.append({'name': name, 'price': price,'image':image}) 
            print(image)
    with open('data.json', 'w') as f:
        json.dump(data, f)   
    result = [(item['name'], item['price'], item['image']) for item in data]
    add_data = (f"INSERT INTO product "
    "(title, price,images) "
    "VALUES (%s, %s, %s)")
    cursor.executemany(add_data, result)
    cnx.commit() 
    return (data)
