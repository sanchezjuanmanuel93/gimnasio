from app.datos.BaseDatos import BaseDatos
from app.datos.models import Socio


class SocioDatos(BaseDatos):

    def get_socios_by_nombre(self,_nombre):
        return super(SocioDatos,self).get_session().query(Socio).filter(Socio.nombre==_nombre)

    def get_socios_by_dni(self, _dni):
        return super(SocioDatos,self).get_session().query(Socio).filter(Socio.dni==_dni).first()

    def get_socios(self):
        return super(SocioDatos,self).get_session().query(Socio)

# ej = SocioDatos()
#
# socios = ej.getAll(Socio)
# for socio in socios:
#     print(socio.nombre)
#
# socios = ej.get_socios_by_dni("37448343")
# for socio in socios:
#     print(socio.nombre)
#
#
# socios = ej.getAll(Socio)
# for socio in socios:
#     print(socio.nombre)