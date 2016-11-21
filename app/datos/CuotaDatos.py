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