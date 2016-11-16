from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

# class ModelBase(Base):
#
#     def __json__(self):
#         return self.fields()
#
#     def fields(self):
#         d = []
#         for column in self.__table__.columns:
#             d[column.name] = getattr(self, column.name)
#         return d
#
#     def keys(self):
#         columns = self.__table__.primary_key.columns
#         return tuple([getattr(self, c.name) for c in columns])
#

class Socio(Base):
    __tablename__ = 'socio'

    dni = Column(String(10), primary_key=True)
    nombre = Column(String(45))
    apellido = Column(String(45))
    telefono = Column(String(45))
    activo = Column(String(45), nullable=False)

    def __init__(self, dni, nombre, apellido, telefono, activo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.activo = activo

