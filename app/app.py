from flask import Flask
from datetime import datetime
import requests
import responses

app = Flask(__name__)

API_KEY = "892ac4245af18b32aeb77969a8b3248c"

@app.route("/")
def home():
    return f"Hello world!"

@app.route("/<int:uid>", methods=['GET'])
def store_weather(uid):
    now = datetime.now()
    url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_KEY}"
    return f"Hello world! {uid} - {now}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
