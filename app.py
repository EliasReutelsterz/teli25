from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('seite1.html')

@app.route('/seite1')
def seite1():
    return render_template('seite1.html')

@app.route('/seite2')
def seite2():
    return render_template('seite2.html')

if __name__ == '__main__':
    app.run(debug=True)