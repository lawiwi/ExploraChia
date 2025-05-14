from flask import Flask, render_template, request, send_file, jsonify
from datetime import datetime
import sqlite3
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from flask import Flask, render_template, request, jsonify, send_file
import joblib

app = Flask(__name__, template_folder='Templates')

# Home 

@app.route("/")
def chiaentre():
    return render_template('Chia/iniciachia.html')

@app.route('/prediccion/<empresa>')
def mostrar_prediccion(empresa):
    return render_template('Prediccion/prediccion_empresa.html', empresa=empresa)

@app.route("/registrar_click", methods=["POST"])
def registrar_click():
    data = request.get_json()
    empresa = data.get("empresa")
    

    if not empresa:
        return jsonify({"error": "No se proporcionó el nombre de la empresa"}), 400

    # Obtener fecha actual
    fecha_actual = datetime.now().date()

    # Ruta del archivo CSV para la empresa
    ruta_csv = f"data/{empresa}.csv"

    # Verificar si el archivo existe, si no, crearlo con encabezados
    archivo_nuevo = not os.path.exists(ruta_csv)
    with open(ruta_csv, mode="a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo, quoting=csv.QUOTE_NONNUMERIC)
        if archivo_nuevo:
            writer.writerow(["publishedAtDate", "comentario"])  # encabezados mínimos
        writer.writerow([fecha_actual.strftime('%Y-%m-%dT%H:%M:%S.%fZ'), "registro click"])

    return jsonify({"mensaje": f"Click registrado para {empresa} en {fecha_actual}"})

@app.route("/Chia/Restaurantes")
def chiacomida():
    return render_template('Chia/Restaurantes.html')

@app.route("/Chia/Arte")
def chiaarte():
    return render_template('Chia/Arte.html')

@app.route("/Chia/Deportes")
def chiadeportes():
    return render_template('Chia/Deportes.html')

@app.route("/Chia/Ocio")
def chiaocio():
    return render_template('Chia/Ocio.html')

@app.route("/Chia/Shopping")
def chiashopping():
    return render_template('Chia/Shopping.html')

@app.route("/Chia/Naturaleza")
def chianatu():
    return render_template('Chia/Recreacion.html')

@app.route("/Chia/Acercade/EntendimientoDelNegocio")
def entendimiento():
    return render_template('Machine/EntendimientoDelNegocio.html')

@app.route("/Chia/Acercade/IngenieriaDatos")
def IngenieriaDatos():
    return render_template('Machine/IngenieriaDatos.html')

@app.route("/Chia/Acercade/IngenieriaModelo")
def IngenieriaModelo():
    return render_template('Machine/IngenieriaModelo.html')

@app.route("/Chia/Acercade")
def Acercade():
    return render_template('Machine/Acercade.html')

@app.route("/Chia/Empresas")
def Empresas():
    return render_template('Prediccion/einicio.html')