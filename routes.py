from flask import Blueprint, jsonify, request
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Thanapon:XXZSMHfsskEH5nlY@thanapon.imw6e4r.mongodb.net/?retryWrites=true&w=majority")
db = cluster['MyData']
collection = db["Data"]

main = Blueprint('main', __name__)

@main.route('/about_me', methods=['GET', 'POST', 'PUT', 'DELETE'])
def about_me():
    global data
    try:
        if request.method == "POST" or request.method == "PUT":
            print(f"Received {request.method} Request")

            data = request.get_json(force=True)
            collection.insert_one(data)

            return "Data received", 201
        
        if request.method == "GET":
            print("Received GET Request")
            arg = request.args
            name = arg.get("Name")
            result = collection.find_one({"Name": name})
            try:
                del result["_id"]
            except:
                raise Exception("User Not Found")

            return result, 201
        
        if request.method == "DELETE":
            print("Received DELETE Request")
            arg = request.args
            name = arg.get("Name")
            result = collection.delete_one({"Name": name})
            return "data deleted", 201

    except Exception as e:
        print(f"Error : {e}")

    return f"{request.method} Request failed", 404