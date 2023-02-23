from flask import Flask
from flask_restful import reqparse
import pymongo
from datetime import datetime

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_connect = myclient["iot_server"]  # database name
db_collection = db_connect["sensor_data"]  # collection name


# REST API to receive sensor data
@app.route("/update", methods=["GET"])
def update():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str)
    parser.add_argument('sensor_data', type=float)
    args = parser.parse_args()
    args["date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db_collection.insert_one(args)
    return {"data": "Inserted"}


# REST API to send sensor data
@app.route("/feeds", methods=["GET"])
def feeds():
    parser = reqparse.RequestParser()
    parser.add_argument('key', type=str)
    args = parser.parse_args()

    reply_got = [i for i in db_collection.find(args)][-1]
    print(reply_got)
    reply = {"data": reply_got['sensor_data'], "date": reply_got['date']}
    return reply


if __name__ == "__main__":
    app.run()
