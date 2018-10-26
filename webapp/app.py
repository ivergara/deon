from pathlib import Path

from flask import Flask, render_template, request

import deon

app = Flask(__name__)

DEFAULT_CHECKLIST = Path(__file__).parent.parent / 'deon' / 'assets' / 'checklist.yml'

@app.route("/create")
def create():
    if 'format' in request.args:
        format_ = request.args['format']
    else:
        format_ = 'html'

    result = deon.create(DEFAULT_CHECKLIST, format_, None, False, False)

    return render_template('index.html', format=format_, content=result)
