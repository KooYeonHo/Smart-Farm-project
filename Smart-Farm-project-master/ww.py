from flask import Flask, render_template, request
import db
# import final

app = Flask(__name__)

@app.route('/')
def toIndex():
    data = db.getLastData()
    return render_template("main.html", data=data)

@app.route("/fan/on")
def fan_on():
	try:
		# final.fan_on()
		return "OK"
	except:
		return "FAIL"

@app.route("/fan/off")
def fan_off():
	try:
		# final.fan_off()
		return "OK"
	except:
		return "FAIL"


if __name__ == '__main__':
    app.run()