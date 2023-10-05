from flask import Flask, render_template,request
import json
import requests
app = Flask(__name__, template_folder='../main')

# # Load the product data from a JSON file
# with open('../dataCrawling_api/data.json', 'r') as f:
#     product_data = json.load(f)

# Define a route to display the list of products
@app.route('/')
def index():
    response = requests.get('http://127.0.0.1:9001/getData')
    data = response.json()
    products = []
    for i in range(len(data)): 
        product = {
            'name': data[i][1],
            'price': data[i][2],
            'image': data[i][3]
        }
        products.append(product)

    return render_template('index.html', products=products)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['search_query'] # Lấy giá trị tìm kiếm từ form
    print(query)
    response = requests.get('http://localhost:9001/searchData/'+query)
    data = response.json()
    products = []
    for i in range(len(data)): 
        product = {
            'name': data[i][1],
            'price': data[i][2],
            'image': data[i][3]
        }
        products.append(product)
    if len(products) == 0:
        print("Mảng rỗng")
        return render_template('index.html', text='Không có sản phẩm cần tìm')
    else:
        print("Mảng không rỗng")
        return render_template('index.html', products=products)  

@app.route('/insertRecord',methods=['POST'])
def insertRecord():
    title = request.form['title'] 
    print(title)
    price = request.form['price']
    print(price)
    images = request.form['images']
    print(images)
    response = requests.get('http://localhost:9001/insertRecord/'+title+'/'+price+'/'+images)
    data = response
    print(data)
    if str(data) == '<Response [200]>':
        return render_template('index.html', text='ok')
    else:
        return render_template('index.html', text='no ok')  


@app.route('/craw',methods=['GET'])
def crawData():
    response = requests.get('http://0.0.0.0:8001/getData')
    data = response.json()
    print(data)
    if len(data) == 0:
        return render_template('index.html', text='erro crawling')
    else:
        return render_template('index.html', text='success')        
if __name__ == '__main__':
    app.run(debug=True)
