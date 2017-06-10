from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    #app.run(host='192.168.1.184', port=80, debug=True)
    app.run(debug=True)
