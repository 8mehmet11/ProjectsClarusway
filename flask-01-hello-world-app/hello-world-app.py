from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world from Mehmet"

@app.route('/second')
def second():
    return "Hello world from Mehmet's second page"

@app.route('/third/subthird')
def third():
    return "Hello world from Mehmet's third page's subpage"



if __name__ == '__main__':
    app.run(debug=True, port=2000)