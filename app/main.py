import flask
import omdb

app = flask.Flask(__name__)
omdb.set_default('apikey', open('omdb.api.key').read().strip())


@app.route('/')
def hello():
    return flask.jsonify(**dict(omdb.get(title='True Grit', year=1969, fullplot=True, tomatoes=True)))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
