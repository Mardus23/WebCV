from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/My Information/')
def myInfo():
    return render_template('myInfo.html')

@app.route('/experience/')
def exp():
    return render_template('experience.html')

if __name__ == '__main__':
    app.run(debug=True)
