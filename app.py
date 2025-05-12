from flask import Flask, render_template, request, send_file
import sqlite3


app = Flask(__name__, template_folder='Templates')

# Home 

@app.route("/")
def chiaentre():
    return render_template('Chia/iniciachia.html')

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

@app.route("/Chia/EntendimientoDelNegocio")
def entendimiento():
    return render_template('Chia/EntendimientoDelNegocio.html')

@app.route("/Chia/IngenieriaDatos")
def IngenieriaDatos():
    return render_template('Chia/IngenieriaDatos.html')

@app.route("/Chia/IngenieriaModelo")
def IngenieriaModelo():
    return render_template('Chia/IngenieriaModelo.html')

