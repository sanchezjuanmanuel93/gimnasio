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


