from app.datos.CuotaDatos import CuotaDatos


class CuotaNegocio(object):
    def __init__(self):
        self.cuotaDatos = CuotaDatos()

    def insert_cuota(self, cuota):
        return self.cuotaDatos.insert(cuota)

    def get_last_by_dni(self, dni):
        return self.cuotaDatos.get_last_by_dni(dni)

