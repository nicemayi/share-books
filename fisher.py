from flask import Flask
from flask import make_response

app = Flask(__name__)
app.config.from_object('config')

@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.google.com',
    }
    # response = make_response('<h1>Hello, Zhe Wang</h1>', 301)
    # response.headers = headers
    # return response
    return '<html>hehe</html>', 301, headers

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
