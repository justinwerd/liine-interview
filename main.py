from flask import Flask,jsonify
import pymongo
import datetime

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["liine-interviews"]
mycol = mydb["restaurants"] 

@app.route('/get-open-restaurants/<date>')
def get_open_restaurants(date):
    try:
        formatted_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M")
        d = formatted_date.weekday() + 1
        h = formatted_date.time().hour
        m = formatted_date.time().minute
        
        mydoc = mydb.hours.find({
            "date_range": d,
            "$or": [
                {"opening_hour": {"$lt": h}}, 
                {"$and": [{"opening_hour": {"$eq": h}},{"opening_minute": {"$lte": m}}]}
                ],
            "$or": [
                {"closing_hour": {"$gt": h}}, 
                {"$and": [{"closing_hour": {"$eq": h}},{"closing_minute": {"$gte": m}}]}
                ],
                                })
        data = [x['restaurant_name'] for x in mydoc]

        return jsonify(data), 200
    except:
        return '''Error: Invalid Date
                Make sure the date is in the format YYYY-mm-ddTHH:MM''', 400


if __name__ == "__main__":
    app.run()


