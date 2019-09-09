from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/deploy', methods=['GET'])
def deploy():
    return "<h1> Testando deploy </h1>"

if __name__ == '__main__':
    app.run()
