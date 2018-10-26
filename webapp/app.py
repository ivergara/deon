from pathlib import Path

from flask import Flask

import deon

app = Flask(__name__)

DEFAULT_CHECKLIST = Path(__file__).parent.parent / 'deon' / 'assets' / 'checklist.yml'

@app.route("/create")
def create():
    return deon.create(DEFAULT_CHECKLIST, "html", None, False, False)
