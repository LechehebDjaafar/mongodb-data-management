# MongoDB Data Management

## Overview

This project demonstrates a Flask-based web application for managing data in MongoDB, providing a simple and intuitive interface for performing CRUD (Create, Read, Update, Delete) operations on a NoSQL database.

## MongoDB Command-Line Operations

### Starting MongoDB Server

#### On Windows:
```bash
# Start MongoDB service
net start mongodb

# Alternative method
"C:\Program Files\MongoDB\Server\<version>\bin\mongod.exe"
```

#### On macOS (using Homebrew):
```bash
brew services start mongodb-community
```

#### On Linux:
```bash
# For systemd
sudo systemctl start mongod

# Alternative method
sudo service mongod start
```

### Connecting to MongoDB

#### Launch MongoDB Shell
```bash
# Connect to local MongoDB instance
mongo

# Connect to a specific host
mongo "mongodb://hostname:port"
```

### Database Operations

#### Create and Switch to a New Database
```bash
# Create or switch to a database
use mydatabase
```

#### Check Current Database
```bash
# Display current database
db
```

#### List All Databases
```bash
# Show available databases
show dbs
```

### Collection Management

#### Create a New Collection
```bash
# Create a collection explicitly
db.createCollection("users")

# Collections are also created automatically when you first insert a document
db.users.insertOne({"name": "John Doe", "age": 30})
```

#### List Collections
```bash
# Show all collections in current database
show collections
```

### Basic CRUD Operations in MongoDB Shell

#### Insert Documents
```bash
# Insert a single document
db.users.insertOne({
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
})

# Insert multiple documents
db.users.insertMany([
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
])
```

#### Query Documents
```bash
# Find all documents in a collection
db.users.find()

# Find documents with a specific condition
db.users.find({"age": {"$gt": 25}})

# Find a single document
db.users.findOne({"name": "Alice"})
```

#### Update Documents
```bash
# Update a single document
db.users.updateOne(
    {"name": "Alice"},
    {"$set": {"age": 26}}
)

# Update multiple documents
db.users.updateMany(
    {"age": {"$lt": 30}},
    {"$inc": {"age": 1}}
)
```

#### Delete Documents
```bash
# Delete a single document
db.users.deleteOne({"name": "Bob"})

# Delete multiple documents
db.users.deleteMany({"age": {"$gte": 30}})
```

### User Management

#### Create a New User
```bash
# Switch to admin database
use admin

# Create a new user with read/write access
db.createUser({
    user: "myappuser",
    pwd: "strongpassword",
    roles: [
        { role: "readWrite", db: "mydatabase" }
    ]
})
```

### Backup and Restore

#### Backup a Database
```bash
# Backup a single database
mongodump --db mydatabase

# Backup with authentication
mongodump -u myappuser -p strongpassword --authenticationDatabase admin --db mydatabase
```

#### Restore a Database
```bash
# Restore a database
mongorestore --db mydatabase /path/to/backup

# Restore with authentication
mongorestore -u myappuser -p strongpassword --authenticationDatabase admin --db mydatabase /path/to/backup
```

### Troubleshooting

#### Check MongoDB Service Status
```bash
# Windows
net start mongodb

# Linux (systemd)
sudo systemctl status mongod

# macOS (Homebrew)
brew services list
```

## Additional Resources

- [Official MongoDB Documentation](https://docs.mongodb.com/)
- [MongoDB University](https://university.mongodb.com/)
- [MongoDB Community Forums](https://www.mongodb.com/community/forums/)

## Features

- **Flexible Data Management**: Leverage MongoDB's schema-less document structure
- **Web Interface**: User-friendly Flask application for data interaction
- **JSON Data Import**: Easy methods to import data from JSON files
- **Basic MongoDB Operations**: Perform insert, query, update, and delete operations

## Prerequisites

- Python 3.x
- Flask
- PyMongo
- MongoDB (local or remote)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mongodb-data-management.git
   cd mongodb-data-management
   cd my_flask_app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure MongoDB is running on your local machine or configure a remote MongoDB instance.

## Usage

Start the Flask application:
```bash
python app.py
```

Navigate to `http://127.0.0.1:5000/` in your web browser to access the application.

## Learning MongoDB: Basics for Beginners

### What is MongoDB?

MongoDB is a popular NoSQL database that stores data in flexible, JSON-like documents called BSON (Binary JSON). Unlike traditional relational databases, MongoDB allows for more dynamic and scalable data storage.

### Key Concepts to Understand

1. **Documents**
   - Basic unit of data in MongoDB
   - Similar to JSON objects
   - Can have different structures within the same collection
   ```json
   {
     "name": "John Doe",
     "age": 30,
     "city": "New York"
   }
   ```

2. **Collections**
   - Equivalent to tables in relational databases
   - Group of related documents
   - Can contain documents with varying structures

3. **Database**
   - Container for collections
   - Can have multiple databases in a single MongoDB instance

### Basic Operations

#### 1. Connecting to MongoDB
```python
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
```

#### 2. Inserting Data
```python
# Insert a single document
collection.insert_one({
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
})

# Insert multiple documents
collection.insert_many([
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
])
```

#### 3. Querying Data
```python
# Find all documents
all_users = collection.find()

# Find specific documents
young_users = collection.find({"age": {"$lt": 30}})

# Find a single document
user = collection.find_one({"name": "Alice"})
```

#### 4. Updating Documents
```python
# Update a single document
collection.update_one(
    {"name": "Alice"},
    {"$set": {"age": 26}}
)

# Update multiple documents
collection.update_many(
    {"age": {"$lt": 30}},
    {"$inc": {"age": 1}}
)
```

#### 5. Deleting Documents
```python
# Delete a single document
collection.delete_one({"name": "Bob"})

# Delete multiple documents
collection.delete_many({"age": {"$gte": 30}})
```

### Advanced Querying

#### Projection (Selecting Specific Fields)
```python
# Retrieve only name and age
results = collection.find({}, {"name": 1, "age": 1, "_id": 0})
```

#### Sorting
```python
# Sort users by age in ascending order
sorted_users = collection.find().sort("age", 1)
```

### Best Practices

1. **Indexing**: Create indexes on frequently queried fields
2. **Schema Design**: 
   - Embed related data when possible
   - Avoid overly deep nesting
3. **Data Validation**: Use schema validation to enforce document structure
4. **Performance**: Use appropriate indexes and query optimization

## Key MongoDB Concepts

- **Documents**: JSON-like objects storing data
- **Collections**: Groups of documents (similar to tables in relational databases)
- **Flexible Schema**: No need to define structure in advance




## Project Structure

- Flask App: Web interface for data management
- MongoDB Operations: CRUD functionality
- User Interface: Bootstrap-powered frontend
