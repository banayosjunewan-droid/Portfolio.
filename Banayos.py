from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("banayos.html")

@app.route("/about")
def about():
    return render_template("aboutbanayos.html")
    
@app.route("/myportfolio")
def myportfolio():
    return render_template("banayosportfolio.html")

if __name__ == '__main__':
    app.run(debug=True)