from datetime import datetime

from app.datos.CuotaDatos import CuotaDatos
from app.datos.SocioDatos import SocioDatos
from app.datos.models import Cuota, Socio


class SocioNegocio(object):
    def __init__(self):
        self.socioDatos = SocioDatos()
        self.cuotaDatos = CuotaDatos()

    def get_socios(self):
        return self.socioDatos.get_all()

    def get_socios_activos(self):
        return self.socioDatos.get_socios_activos()

    def get_socios_by_dni(self, _dni):
        return self.socioDatos.get_by_dni(_dni)

    def insert_socio(self, socio):
        if self.get_socios_by_dni(socio.dni):
            return None
        else:
            return self.socioDatos.insert(socio)

    def update_socio(self, dni, nombre, apellido, telefono, activo):
        socio = self.get_socios_by_dni(dni)
        if socio:
            socio.nombre = nombre
            socio.apellido = apellido
            socio.telefono = telefono
            socio.activo = activo
            return self.socioDatos.update(socio)
        else:
            return None

    def delete_socio(self, dni):
        socio = self.get_socios_by_dni(dni)
        if socio:
            socio.activo = Socio.NO_ACTIVO
            return self.socioDatos.update(socio)
        else:
            return None

    def get_socios_deudores(self):
        socios = self.socioDatos.get_socios_activos()
        deudores = []
        for socio in socios:
            cuota = socio.get_ultima_cuota()
            if cuota:
                if cuota.fecha_hasta < datetime.now().date():
                    deudores.append(socio)
        return deudores

    def update_socio(self, socio):
        socio = self.get_socios_by_dni(socio.dni)
        if socio:
            return self.socioDatos.update(socio)
        else:
            return None
#
# ej = SocioNegocio()
# socio = ej.get_socios_by_dni("37448343")
# cuota = Cuota('2016-11-22','2016-12-22',222,socio)
# socio.cuotas.append(cuota)
# ej.update_socio(socio)
