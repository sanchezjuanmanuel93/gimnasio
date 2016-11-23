from sqlalchemy import Column, String
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Boolean
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from decorated.base.dict import Dict

Base = declarative_base()
metadata = Base.metadata


class Cuota(Base):
    __tablename__ = 'cuota'

    dni_socio = Column(ForeignKey('socio.dni'), primary_key=True, nullable=False)
    fecha_desde = Column(Date, primary_key=True, nullable=False)
    fecha_hasta = Column(Date)
    fecha_pago = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    monto = Column(Float)
    socio = relationship('Socio')

    def __init__(self, fecha_desde, fecha_hasta, fecha_pago, monto, socio):
        self.dni_socio = socio.dni
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.fecha_pago = fecha_pago
        self.monto = monto

    def __init__(self, fecha_desde, fecha_hasta, monto, socio):
        self.dni_socio = socio.dni
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.monto = monto

    def __json__(self):
        return self.fields()

    def fields(self):
        d = Dict()
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d


class Socio(Base):
    __tablename__ = 'socio'

    ACTIVO = 1;
    NO_ACTIVO = 0;

    dni = Column(String(10), primary_key=True)
    nombre = Column(String(45))
    apellido = Column(String(45))
    telefono = Column(String(45))
    activo = Column(Integer, server_default=text("'1'"))

    cuotas = relationship("Cuota", back_populates="socio")


    def __init__(self, dni, nombre, apellido, telefono, activo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.activo = activo

    def get_apellido_nombre(self):
        return self.apellido+' '+self.nombre

    def get_ultima_cuota(self):
        if len(self.cuotas) > 0:
            return self.cuotas[-1]
        else:
            return None

    def __json__(self):
        return self.fields()

    def fields(self):
        d = Dict()
        for column in self.__table__.columns:
            d[column.name] = getattr(self, column.name)
        return d
