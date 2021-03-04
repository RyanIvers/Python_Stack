from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def checker():
    return render_template("index.html", times1 = 8, times2 = 8)

@app.route('/four')
def checker_eight():
    return render_template("index.html", times1 = 8, times2 = 4)

@app.route('/<int:numone>/<int:numtwo>')
def checker_four(numone, numtwo):
    return render_template("index.html", times1 = numone, times2 = numtwo)



if __name__=="__main__":
    app.run(debug=True)