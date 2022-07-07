from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

API_KEY = "892ac4245af18b32aeb77969a8b3248c"

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, unique=True, nullable=False)
    data = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return self.data

@app.route("/")
def home():
    return "Hello World!"

def save_weather(uid):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={uid}&appid={API_KEY}"
    now = datetime.now()

    response = requests.get(url)
    response = response.json()

    data = {
            "city_id": uid,
            "temp": response['main']['temp'],
            "humidity": response['main']['humidity'],
    }

    a = User(uid=uid, date=now, data=json.dumps(data))
    db.session.add(a)
    db.session.commit()

@app.route("/<int:uid>", methods=['GET'])
def store_weather(uid):
    save_weather(uid)
    # background_tasks = set()

    # for i in range(10):
    #     task = asyncio.create_task(some_coro(param=i))
    #     background_tasks.add(task)
    #     task.add_done_callback(background_tasks.discard)

    return "Success"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
