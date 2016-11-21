from app.datos.forms import AltaSocioForm, AltaCuotaForm, GetEstadoSocio
from app.negocio.SocioNegocio import SocioNegocio
from app.negocio.CuotaNegocio import CuotaNegocio
from flask import Flask, redirect, request, render_template
from app.datos.models import Socio,Cuota
from datetime import datetime
import calendar

app = Flask(__name__)

# Configurations
app.config.from_object('config')

socioNegocio = SocioNegocio()
cuotaNegocio = CuotaNegocio()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetEstadoSocio(request.form)
    if request.method == 'POST' and form.validate():
        socio = socioNegocio.get_socios_by_dni(form.dni.data)
        if(socio):
            ultima_cuota = cuotaNegocio.get_last_by_dni(socio.dni)
            if(ultima_cuota):
                fecha_hasta = ultima_cuota.fecha_hasta
                if (fecha_hasta > datetime.now().date()):
                    dias_restantes = (fecha_hasta - datetime.now().date()).days
                    message = "Socio al dia. Quedan " + str(dias_restantes) + " dias restantes"
                    return render_template('index.html', success=message, form=form)
                else:
                    error = "Cuota vencida"
                    return render_template('index.html', error=error, form=form)
            else:
                error = "Cuota vencida"
                return render_template('index.html', error=error, form=form)
        else:
            error="El socio no existe"
            return render_template('index.html', error=error, form=form)
    return render_template('index.html', form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/getSocioDni=<dni>')
def get_socio_by_dni(dni):
    socio = socioNegocio.get_socios_by_dni(dni)
    return socio.nombre + " " + socio.apellido


@app.route('/socio/alta', methods=['GET', 'POST'])
def altaSocio():
    form = AltaSocioForm(request.form)
    if request.method == 'POST' and form.validate():
        if socioNegocio.insert_socio(
                Socio(form.dni.data, form.nombre.data, form.apellido.data, form.telefono.data, Socio.ACTIVO)):
            return redirect("socio")
        else:
            message = "Error al insertar el socio"
            return render_template('socio/altaSocio.html', error=message, form=form)
    return render_template('socio/altaSocio.html', form=form)


@app.route('/socio/modificar/<dni>', methods=['GET', 'POST'])
def modificarSocio(dni):
    form = AltaSocioForm(request.form)
    message = ""
    if request.method == 'POST' and form.validate():
        if socioNegocio.update_socio(form.dni.data, form.nombre.data, form.apellido.data, form.telefono.data,
                                     form.activo.data):
            return redirect("socio")
        else:
            message = "Error al modificar el Socio"
    elif request.method == 'GET':
        socio = socioNegocio.get_socios_by_dni(dni)
        if socio:
            form.apellido.data = socio.apellido
            form.nombre.data = socio.nombre
            form.dni.data = socio.dni
            form.telefono.data = socio.telefono
            form.activo.data = socio.activo
        else:
            message = 'No se encontro le Socio con DNI: ' + dni
    return render_template('socio/modificarSocio.html', error=message, form=form)

@app.route('/socio/borrar/<dni>')
def borrarSocio(dni):
    message=""
    if socioNegocio.delete_socio(dni):
        return redirect("socio")
    else:
        message="No se puede eliminar el Socio"
    return render_template('socio/modificarSocio.html', error=message)


@app.route('/socio/')
def socios():
    return render_template('socio/index.html', socios=socioNegocio.get_socios())


@app.route('/altaok')
def altaok():
    return "<h1>Socio ingresado correctamente</h1>"

@app.route('/cuota/alta', methods=['GET', 'POST'])
def altaCuota():
    form = AltaCuotaForm(request.form)
    if request.method == 'POST':
        socio = socioNegocio.get_socios_by_dni(form.dni.data)
        fecha_desde = form.fechaDesde.data
        fecha_hasta = add_month(fecha_desde)
        res = cuotaNegocio.insert_cuota(Cuota(fecha_desde, fecha_hasta, datetime.now().date(), form.monto.data, socio))
        return redirect('altaok')
    return render_template('cuota/altaCuota.html', form=form)

def add_month(sourcedate):
    month = sourcedate.month
    year = int(sourcedate.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime(year=year, month=month, day=day).date()

app.run(debug=True)
