from flask import Flask, render_template

app = Flask(__name__) #indica que este es el arichivo que arranca la aplicacion

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)