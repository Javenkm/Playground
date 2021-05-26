from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html', boxNum = 3)

@app.route('/play/<int:numBoxes>')
def insertBoxes(numBoxes):
    return render_template ('index.html', boxNum = numBoxes)

@app.route('/play/<int:numBoxes>/<string:color>')
def insertBoxes2(numBoxes, color):
    return render_template('index.html', boxNum = numBoxes, boxColor = color)

if __name__ == "__main__":
    app.run(debug = True)