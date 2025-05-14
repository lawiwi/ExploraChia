from flask import Flask, render_template, request, send_file, jsonify
from datetime import datetime
import sqlite3
import csv
import os
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

# Cargar el modelo previamente guardado
def cargar_modelo(nombre_empresa):
    ruta_modelo = f"modelos/modelo_{nombre_empresa}.pkl"
    return joblib.load(ruta_modelo)

@app.route('/predicciones/<nombre_empresa>', methods=['GET'])
def predicciones(nombre_empresa):
    # Cargar modelo
    modelo = cargar_modelo(nombre_empresa)
    
    # Generar predicciones para los días de la semana (0 a 6)
    dias_semana = np.arange(0, 7)
    visitas_predichas = modelo.predict(dias_semana.reshape(-1, 1))
    
    # Crear gráfico
    fig, ax = plt.subplots()
    ax.plot(dias_semana, visitas_predichas, marker='o', color='b', label="Visitas Predichas")
    ax.set_title(f"Predicciones de Visitas por Día de la Semana ({nombre_empresa})")
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('Visitas')
    ax.set_xticks(dias_semana)
    ax.set_xticklabels(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    ax.legend()
    
    # Guardar la imagen en un buffer
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    
    # Enviar el archivo de imagen como respuesta
    return send_file(img_buf, mimetype='image/png')

def cargar_datos_empresa(empresa):
    # Cargar los datos específicos de la empresa (por ejemplo, desde un CSV)
    df = pd.read_csv(f"data/{empresa}.csv")
    # Filtra o procesa los datos según sea necesario
    return df

def obtener_predicciones(empresa):
    # Lógica para obtener predicciones (por ejemplo, usando el modelo entrenado)
    modelo = joblib.load(f"modelos/modelo_{empresa}.pkl")
    df_empresa = cargar_datos_empresa(empresa)
    
    # Suponiendo que quieres predecir visitas por día de la semana
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    visitas_predichas = modelo.predict(df_empresa[["dia_semana_num"]])  # Usando el modelo

    # Organiza las predicciones para la visualización
    predicciones = {
        "dias_semana": dias_semana,
        "visitas_predichas": visitas_predichas.tolist()  # Convertir a lista para pasar a Jinja2
    }
    return predicciones

@app.route("/predicciones/<empresa>")
def predicciones_empresa(empresa):
    # Cargar datos históricos, predicciones y demás información relevante
    # Asegúrate de cargar solo los datos de la empresa seleccionada
    empresa_data = cargar_datos_empresa(empresa)  # Función para cargar los datos

    # Aquí se puede realizar la predicción con el modelo entrenado y agregar la lógica
    # para obtener las predicciones de la empresa
    predicciones = obtener_predicciones(empresa)

    return render_template("predicciones_empresa.html", empresa=empresa, 
                           empresa_data=empresa_data, predicciones=predicciones)


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