from flask import Flask
from negocio.SocioNegocio import SocioNegocio

app = Flask(__name__)

socioNegocio = SocioNegocio()

@app.route('/')
def hello_world():
    socio = socioNegocio.get_socios()
    return socio[0].nombre

@app.route('/<dni>')
def get_socio_by_dni(dni):
    socio = socioNegocio.get_socios_by_dni(dni)
    return socio.nombre + " " + socio.apellido

app.run(debug=True)