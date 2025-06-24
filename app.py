from flask import Flask, render_template, request, redirect, url_for, send_file
import csv
import os
from datetime import datetime

app = Flask(__name__)

# Nombre del archivo CSV
CSV_FILE = 'datos_censo.csv'

# Crear el archivo CSV con encabezados si no existe
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'edad', 'ocupacion', 'tipo_vivienda', 'ingresos', 'fecha_registro'])

@app.route("/", methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        # Obtener datos del formulario
        edad = request.form['edad']
        ocupacion = request.form['ocupacion']
        tipo_vivienda = request.form['tipo_vivienda']
        ingresos = request.form['ingresos']
        fecha_registro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Generar ID (simplemente incrementamos el último ID)
        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar encabezados
            ids = [int(row[0]) for row in reader if row]
            nuevo_id = max(ids) + 1 if ids else 1
        
        # Guardar en CSV
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nuevo_id, edad, ocupacion, tipo_vivienda, ingresos, fecha_registro])
        
        return redirect(url_for('inicio'))
    
    return render_template("index.html")

@app.route("/tabla")
def tabla():
    # Leer datos del CSV
    datos = []
    with open(CSV_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            datos.append(row)
    
    return render_template("tabla.html", datos=datos)

@app.route("/grafico")
def grafico():
    # Leer datos para las estadísticas
    datos = []
    with open(CSV_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            datos.append(row)
    
    return render_template("grafico.html", datos=datos)

@app.route("/exportar")
def exportar():
    return send_file(
        CSV_FILE,
        as_attachment=True,
        download_name='datos_censo.csv',
        mimetype='text/csv'
    )

if __name__ == "__main__":
    app.run(debug=True, port=8000)