from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html", titulo="Inicio")

# Ruta con parámetro dinámico
@app.route("/saludo/<nombre>")
def saludar(nombre):
    return render_template("saludo.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta en http://localhost:5000