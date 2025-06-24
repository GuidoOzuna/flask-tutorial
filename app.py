from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/tabla")
def acerca():
    return render_template("tabla.html")

@app.route("/grafico")
def contacto():
    return render_template("grafico.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)