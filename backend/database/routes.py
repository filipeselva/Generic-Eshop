from database import app
from flask import jsonify

@app.route("/")
@app.route("/home")
def index():
    return jsonify({"hello":"World"})

@app.route("/carrito")
def carrito():
    return "<p>carrito</p>"

@app.route("/crearusuario")
def crear_usuario():
    return "crear usuario"

@app.route("/perfildelusuario")
def perfil_usuario():
    return "perfil del usuario"

@app.route("/dadospersonales")
def dados_personales():
    return "dados del usuario"

@app.route("/misproductos")
def mis_productos():
    return "mis productos"

@app.route("/registrarproducto")
def registrar_producto():
    return "registrar producto"

@app.route("/editarproducto")
def editar_producto():
    return "editar producto"

@app.route("/teladeproducto")
def tela_producto():
    return "tela producto" 

@app.route("/sobrenosotros")
def sobre_nosotros():
    return "sobre nosotros"

@app.route("/contactanosostros")
def contacta_nosotros():
    return "contacta con nosotros"

@app.route("/admin")
def admin():
    return "admin"