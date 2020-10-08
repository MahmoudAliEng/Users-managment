from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    routing the index page
    """
    return 'Salam 3likoum'


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 80
    debug = True
    app.run(host=host, port=port, debug=debug)
