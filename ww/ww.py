from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def toIndex():
    return render_template("main.html", data = 10)


if __name__ == '__main__':
    app.run()