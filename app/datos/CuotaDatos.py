from app.datos.BaseDatos import BaseDatos
from app.datos.models import Cuota


class CuotaDatos(BaseDatos):

    # def get_by_dni(self, _dni):
    #     return super(SocioDatos, self).get_session().query(Socio).filter(Socio.dni==_dni).first()
    #
    # def get_all(self):
    #     return super(SocioDatos, self).get_session().query(Socio)

    def insert(self, _cuota):
        try:
            ses = super(CuotaDatos, self).get_session()
            ses.add(_cuota)
            ses.commit()
            return True
        except Exception as e:
            return False

    def get_last_by_dni(self, _dni):
        ses = super(CuotaDatos, self).get_session()
        all = ses.query(Cuota).filter(Cuota.dni_socio == _dni)
        return all.order_by(Cuota.fecha_desde.desc()).first()

    def get_all_by_dates(self, _desde, _hasta):
        ses = super(CuotaDatos, self).get_session()
        return ses.query(Cuota).filter(Cuota.fecha_pago.between(_desde, _hasta)).order_by(Cuota.fecha_pago.asc())


 # c = CuotaDatos()
 # for item in c.get_all_by_dates('2016-11-10','2016-11-22'):
 #     print(item.fecha_pago)
# cuota = c.get_last_by_dni("37448343")
# if cuota.fecha_hasta < '2016-11-24':
#     print(cuota.fecha_hasta)
