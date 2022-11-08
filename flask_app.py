from flask import Flask
# from flask_api import FlaskAPI
# from flask_api import status
from waitress import serve

app = Flask(__name__)

@app.route("/api/v1/hello-world-6")
@app.route("/")
def hello_world():
    content = 'Hello World 6'
    return content, 200

if __name__ == "__main__":
    serve(app, host='127.0.0.1', port=5000)



# http://127.0.0.1:5000
#  waitress-serve --port=5000 --host=127.0.0.1 main:app
