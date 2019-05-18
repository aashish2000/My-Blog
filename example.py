from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("page1.html")

@app.route('/page')
def info():
    return render_template("page2.html")

@app.route('/features/<name>')
def feature(name):
    return "<h1>This is a page for feature {}</h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True)
