import flask
import omdb

from forms import SearchForm


app = flask.Flask(__name__)
app.config.from_object('config')


omdb.set_default('apikey', open('omdb.api.key').read().strip())


@app.route('/')
def hello():
    return flask.render_template('starter.html', form=SearchForm(), results='')


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if flask.request.method == 'POST':
        return flask.redirect((flask.url_for('search_results', search_term=form.search_term.data)))
    return flask.render_template('starter.html', form=SearchForm(), results='')


@app.route('/search_results/<search_term>')
def search_results(search_term):
    results = str(omdb.search(search_term))
    return flask.render_template('starter.html', form=SearchForm(), results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
