import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib


meses_alta = [6, 7, 12, 1]  # Junio, Julio, Diciembre, Enero

# Obtener todos los archivos CSV en la carpeta data/
data_folder = "data"
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

def es_temporada_alta(mes):
    return 1 if mes in meses_alta else 0


# Recorrer cada archivo CSV
for file in csv_files:
    nombre_empresa = file.replace("data", "").replace(".csv", "")  # Extraer nombre
    print(f"\n--- Procesando: {nombre_empresa} ---")

    # Cargar datos
    df = pd.read_csv(os.path.join(data_folder, file))
    df["publishedAtDate"] = pd.to_datetime(df["publishedAtDate"])
    df["fecha"] = df["publishedAtDate"].dt.date
    df["dia_semana"] = df["publishedAtDate"].dt.day_name()
    df["dia_semana_num"] = df["publishedAtDate"].dt.weekday
    df["mes"] = df["publishedAtDate"].dt.month
    df["temporada_alta"] = df["mes"].apply(es_temporada_alta)
    df["visitas"] = np.where(df["publishAt"] == "registro click", 0.5, 1)

    # Agrupar por día
    df_agrupado = df.groupby(["fecha", "dia_semana", "dia_semana_num", "mes", "temporada_alta"]).agg({"visitas": "sum"}).reset_index()

    # Entrenamiento
    X = df_agrupado[["dia_semana_num", "mes", "temporada_alta"]]
    y = df_agrupado["visitas"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    # Evaluar
    y_pred = modelo.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"MAE para {nombre_empresa}: {mae:.2f}")

    # Guardar modelo
    ruta_modelo = os.path.join("modelos", f"modelo_{nombre_empresa}.pkl")
    joblib.dump(modelo, ruta_modelo)
    print(f"Modelo guardado en: {ruta_modelo}")
