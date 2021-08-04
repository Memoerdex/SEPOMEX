from flask import Flask, render_template, request, url_for
from flask_migrate import Migrate
from werkzeug.utils import redirect

from Servicio.DAO import DAO
from Servicio.Conexion import Conexion
from database import db
from forms import RegistroForm
from models import Registro

app = Flask(__name__)

# Configuracion de la base de datos
USER_DB = "postgres"
PASS_DB = "veravera965"
URL_DB = "localhost"
NAME_DB = "SEPOMEX"
FULL_URL_DB = f"postgresql://{Conexion._USERNAME}:{Conexion._PASSWORD}@{Conexion._HOST}/{Conexion._DATABASE}"

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Inicializacion del objeto db de sqqlalchemy
db.init_app(app)

# Configutat flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

# Configuracion flask_wtf
app.config["SECRET_KEY"] = "llave_secreta"


@app.route("/")
@app.route("/api/index")
@app.route("/api/index.html")
def inicio():
    DAO.crearBase()
    if DAO.baseNoVacia() == 0:
        DAO.cargaBase()
    totalResgistros = Registro.query.count()
    app.logger.debug(f"Total Personas: {totalResgistros}")
    return render_template("index.html", totalRegistros=totalResgistros)


# Realiza una busqueda del registro solicitado sin importar si es nombre o CP, la diferencia la delega a la funcion
# alojada en DAO
@app.route("/buscar/", methods=["GET", "POST"])
def buscar():
    busqueda = request.form['nm']
    app.logger.debug(f"Colonia: {busqueda}")
    app.logger.debug(f"Respuesta DAO: {DAO.buscar(busqueda)}")
    identificadores = DAO.buscar(busqueda)
    app.logger.debug(f"registros: {identificadores}")
    if identificadores != []: # Revisa si hay resultados de la busqueda, si no hay devuelve a la pagina principal
        registros = []
        for id in identificadores:
            registro = Registro.query.get_or_404(id)
            registros.append(registro)
        app.logger.debug(f"Ver registro: {registros}")
        return render_template("listaCoincidencias.html", registros=registros, busqueda=busqueda.title())
    else:
        return render_template("index.html")


# Muestra toda la informacion del registro seleccionado
@app.route("/buscar/ver/<int:id>")
def ver(id):
    registro = Registro.query.get_or_404(id)
    app.logger.debug(f"Ver registro: {registro}")
    return render_template("detalle.html", registro=registro)


# Agrega un nuevo registro, revisa si no existe y si no lo agrega
@app.route("/api/agregar", methods=["GET", "POST"])
def agregar():
    registro = Registro()
    registroForm = RegistroForm(obj=registro)
    if request.method == "POST":
        if registroForm.validate_on_submit():
            registroForm.populate_obj(registro)
            app.logger.debug(f"Registro a insertar: {registro}")
            # Insertamos el nuevo registro
            db.session.add(registro)
            db.session.commit()
            return redirect(url_for("inicio"))
    return render_template("agregar.html", forma=registroForm)


# Abre una solicitud del regirtro y hace las modificaciones necesarias
@app.route("/buscar/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    # Recuperamos el registro a editar
    registro = Registro.query.get_or_404(id)
    registroForm = RegistroForm(obj=registro)
    if request.method == "POST":
        if registroForm.validate_on_submit():
            registroForm.populate_obj(registro)
            app.logger.debug(f"Registro a insertar: {registro}")
            # Insertamos el nuevo registro
            db.session.commit()
            return redirect(url_for("inicio"))
    return render_template("editar.html", forma=registroForm)


# Elimina el registro
@app.route("/buscar/eliminar/<int:id>")
def eliminar(id):
    registro = Registro.query.get_or_404(id)
    app.logger.debug(f"Registro a eliminar: {registro}")
    db.session.delete(registro)
    db.session.commit()
    return redirect(url_for("inicio"))
