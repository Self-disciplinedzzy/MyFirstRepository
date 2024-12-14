from flask import Flask

app = Flask("__name__")


@app.route("/")
def index():
    return "Hello My First Flask_web!"


@app.route("/book")
def book():
    return "This is a web_page that prepare to develop bookApp!"


if __name__ == "__main__":
    app.run(host="192.168.1.13", port=8080, debug=True)
