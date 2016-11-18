from app.datos.SocioDatos import SocioDatos

class SocioNegocio(object):

    def __init__(self):
        self.socioDatos = SocioDatos()

    def get_socios(self):
        return self.socioDatos.get_all()

    def get_socios_by_dni(self,_dni):
        return self.socioDatos.get_by_dni(_dni)

    def insert_socio(self,_socio):
        return self.socioDatos.insert(_socio)
