from flask import Flask,jsonify
import pymongo
import datetime
from pprint import pprint
from date_time_parse import break_down_hours,find_restaurant_hours
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

def create_hours_collection():
    mydoc = mycol.find({})
    data = [x for x in mydoc]
    pprint(data)
    for d in data:
        restaurant_id = d['_id']
        restaurant_name = d['Restaurant Name']
        restaurant_hours = d['Hours']
        print(d)
        h = break_down_hours(restaurant_hours)
        for i in h:
            date_data = find_restaurant_hours(i)
            print(date_data)
            mydb.hours.insert_one({"restaurant_id": restaurant_id,
                                   "restaurant_name":restaurant_name,
                                   "date_range":date_data[0],
                                   "opening_hour":date_data[1][0], 
                                   "opening_minute":date_data[1][1], 
                                   "closing_hour": date_data[1][2],
                                   "closing_minute": date_data[1][3]}
                                   )

if __name__ == "__main__":
    app.run()


