import json
from pymongo import MongoClient

# الاتصال بقاعدة بيانات MongoDB المحلية
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]  # اسم قاعدة البيانات
collection = db["population_data"]  # اسم المجموعة

# تحميل البيانات من ملف JSON
with open('population_data.json', 'r') as file:
    data = json.load(file)

# إدخال البيانات إلى MongoDB
collection.insert_many(data)

print("Data entered successfully!")