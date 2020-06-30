from flask import Flask
import datetime
import string
import random

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def test_hello():
	N=10
	rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
	now = datetime.datetime.now()
	now = now.strftime("%Y-%m-%d %H:%M:%S")
	return "<h1>Hello "+ rand_str + ", Current time is " + str(now) + "</h1>"


if __name__ == "__main__":
	app.run(host='0.0.0.0')