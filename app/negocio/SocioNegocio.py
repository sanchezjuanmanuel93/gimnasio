from app.datos.SocioDatos import SocioDatos


class SocioNegocio(object):
    def __init__(self):
        self.socioDatos = SocioDatos()

    def get_socios(self):
        return self.socioDatos.get_all()

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
            return self.socioDatos.delete(socio)
        else:
            return None
#
# ej = SocioNegocio()
# ej.update_socio("37448343","juan23","sanchez23","12312",0)