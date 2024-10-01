from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/submit")
def render_calculator():
    rd1 = request.args['rd1']
    rd2 = request.args['rd2']
    rd3 = request.args['rd3']
    rd4 = request.args['rd4']
    rd5 = request.args['rd5']
    response1 = (float(rd1) + float(rd2) + float(rd3) + float(rd4) + float(rd5))/5
    return render_template('calculator.html',response = response1)


if __name__=="__main__":
    app.run(debug=False)
