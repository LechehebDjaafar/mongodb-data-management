import json
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# الاتصال بقاعدة بيانات MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]  # اسم قاعدة البيانات
collection = db["population_data"]  # اسم المجموعة

# الصفحة الرئيسية: عرض البيانات
@app.route('/')
def index():
    # استرجاع البيانات من قاعدة البيانات
    items = collection.find()
    return render_template('index.html', items=items)

# إضافة البيانات من JSON
@app.route('/load_data', methods=['GET'])
def load_data():
    # تحميل البيانات من ملف JSON
    with open('population_data.json', 'r') as file:
        data = json.load(file)

    # إدخال البيانات إلى MongoDB
    for entry in data:
        collection.insert_one(entry)

    return redirect('/')

# إضافة البيانات
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        country_name = request.form['countryName']
        country_code = request.form['countryCode']
        year = request.form['year']
        value = request.form['value']
        
        # إدخال البيانات إلى MongoDB
        collection.insert_one({
            "Country Name": country_name,
            "Country Code": country_code,
            "Year": year,
            "Value": value
        })
        return redirect('/')

# تعديل البيانات
@app.route('/edit/<item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item = collection.find_one({"_id": ObjectId(item_id)})
    
    if request.method == 'POST':
        updated_data = {
            "Country Name": request.form['countryName'],
            "Country Code": request.form['countryCode'],
            "Year": request.form['year'],
            "Value": request.form['value']
        }
        collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_data})
        return redirect('/')
    
    return render_template('edit.html', item=item)

# حذف البيانات
@app.route('/delete/<item_id>', methods=['GET'])
def delete(item_id):
    collection.delete_one({"_id": ObjectId(item_id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
