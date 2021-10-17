from flask import Flask, render_template, request, redirect, url_for, flash, jsonify


app = Flask(__name__)


@app.route('/',)
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    code = request.form['code']
    return code

# @app.route('/api/v1/generate/')
# def generate():
    



if __name__ == '__main__':
    app.run(debug=True)