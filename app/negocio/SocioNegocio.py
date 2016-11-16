from app.datos.SocioDatos import SocioDatos

class SocioNegocio(object):

    def __init__(self):
        self.socioDatos = SocioDatos()

    def get_socios(self):
        return self.socioDatos.get_socios()

    def get_socios_by_dni(self,_dni):
        return self.socioDatos.get_socios_by_dni(_dni)
