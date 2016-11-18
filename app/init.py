from flask import Flask, render_template
from app.negocio import SocioNegocio

app = Flask(__name__)

# Configurations
app.config.from_object('config')


socioNegocio = SocioNegocio.SocioNegocio()

@app.route('/')
def hello_world():
    socio = socioNegocio.get_socios()
    return socio[0].nombre

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/getSocioDni=<dni>')
def get_socio_by_dni(dni):
    socio = socioNegocio.get_socios_by_dni(dni)
    return socio.nombre + " " + socio.apellido

@app.route('/socio/alta')
def altaSocio():
    return render_template('socio/altaSocio.html')

app.run(debug=True)