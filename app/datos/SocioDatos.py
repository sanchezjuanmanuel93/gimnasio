from app.datos.BaseDatos import BaseDatos
from app.datos.models import Socio


class SocioDatos(BaseDatos):

    def get_by_nombre(self,_nombre):
        return super(SocioDatos, self).get_session().query(Socio).filter(Socio.nombre==_nombre)

    def get_by_dni(self, _dni):
        return super(SocioDatos, self).get_session().query(Socio).filter(Socio.dni==_dni).first()

    def get_all(self):
        return super(SocioDatos, self).get_session().query(Socio)

    def insert(self, _socio):
        try:
            ses = super(SocioDatos, self).get_session()
            ses.add(_socio)
            ses.commit()
            return True
        except Exception as e:
            return False

# ej = SocioDatos()
# if ej.get_by_dni("37573140"):
#     print("Existe")
# else:
#     print("no existe")
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