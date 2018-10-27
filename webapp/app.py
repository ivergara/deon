from pathlib import Path

from flask import Flask, render_template, request, jsonify

import deon

app = Flask(__name__)

DEFAULT_CHECKLIST = Path(__file__).parent.parent / 'deon' / 'assets' / 'checklist.yml'


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    return render_template('400.html', msg=error.message), error.status_code


@app.route('/foo')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)


@app.route("/create")
def create():
    if 'format' in request.args:
        format_ = request.args['format']
    else:
        format_ = 'html'

    try:
        result = deon.create(DEFAULT_CHECKLIST, format_, None, False, False)
    except deon.FormatException:
        raise InvalidUsage(f'Format {format_} not supported or invalid', status_code=400)

    return render_template('index.html', format=format_, content=result)
