from app.datos.BaseDatos import BaseDatos
from app.datos.CuotaDatos import CuotaDatos
from app.datos.models import Socio, Cuota


class SocioDatos(BaseDatos):
    def get_by_nombre(self, _nombre):
        return super(SocioDatos, self).get_session().query(Socio).filter(Socio.nombre == _nombre)

    def get_by_dni(self, _dni):
        return super(SocioDatos, self).get_session().query(Socio).filter(Socio.dni == _dni).first()

    def get_all(self):
        return super(SocioDatos, self).get_session().query(Socio).order_by(Socio.apellido.asc())

    def insert(self, _socio):
        try:
            ses = super(SocioDatos, self).get_session()
            ses.add(_socio)
            ses.commit()
            return True
        except Exception as e:
            return False

    def update(self, _socio):
        try:
            ses = super(SocioDatos, self).get_session()
            ses.merge(_socio)
            ses.commit()
            return True
        except Exception as e:
            return False

    def delete(self, socio):
        try:
            ses = super(SocioDatos, self).get_session()
            ses.delete(socio)
            ses.commit()
            return True
        except Exception as e:
            return False

    def get_socios_activos(self):
        return super(SocioDatos, self).get_session().query(Socio).filter(Socio.activo == Socio.ACTIVO)


# ej = SocioDatos()
# socios = ej.get_socios_activos()
# for socio in socios:
#     cuota = CuotaDatos.get_last_by_dni(socio.dni)
#     print(cuota.fecha_hasta)

# socio = Socio("37448343","juan2","sanchez2","12312",0)
# ej.update(socio)
# if ej.get_by_dni("37573140"):
#     print("Existe")
# else:
#     print("no existe")
#
# socios = ej.getAll(Socio)
# for socio in socios:
#     print(socio.nombre)
#


# ej = SocioDatos()
# socio = ej.get_by_dni("37448344")
# print(socio.get_ultima_cuota().fecha_hasta)


# ej.delete(socio)
# for socio in socios:
#     print(socio.nombre)
#
#
# socios = ej.getAll(Socio)
# for socio in socios:
#     print(socio.nombre)
