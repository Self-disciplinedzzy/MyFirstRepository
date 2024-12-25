from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "我是wjj他爸"


@app.route("/zzy")
def zzy():
    return "我是zzy"


@app.route("/wjj")
def wjj():
    return "wjj在那里"


if __name__ == "__main__":
    app.run()
