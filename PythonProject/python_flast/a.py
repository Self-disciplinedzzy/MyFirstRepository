from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "这是主页面, 要去福页面:main"


@app.route('/main')
def host():
    return "这是福页面"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
