"""
    This module contains a flask application
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
        a simple function tahat returns a template
    """
    return render_template('templates/0-index.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)