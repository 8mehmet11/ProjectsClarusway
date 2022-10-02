from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 =700230, number2 = 903200)


@app.route("/mehmet")
def number():
    num1 = 23
    num2 = 54
    return render_template("body.html", num1=num1, num2=num2, sum=num1*num2)
    

if __name__== "__main__":
    app.run(debug=True)