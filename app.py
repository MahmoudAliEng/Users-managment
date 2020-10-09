from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """
    routing the index page
    """
    return 'Salam 3likoum'


if __name__ == '__main__':
    host, port = ('52.255.179.241', 5008)
    debug = True
    app.run(host=host, port=port, debug=debug)
