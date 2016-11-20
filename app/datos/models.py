from sqlalchemy import Column, String
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Cuota(Base):
    __tablename__ = 'cuota'

    dni_socio = Column(ForeignKey('socio.dni'), primary_key=True, nullable=False)
    fecha_desde = Column(Date, primary_key=True, nullable=False)
    fecha_hasta = Column(Date)
    fecha_pago = Column(Date)
    monto = Column(Float)
    # socio = relationship('Socio')

    def __init__(self, fecha_desde, fecha_hasta, fecha_pago, monto, socio):
        self.dni_socio = socio.dni
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.fecha_pago = fecha_pago
        self.monto = monto
        # self.socio = socio


class Socio(Base):
    __tablename__ = 'socio'

    ACTIVO = 1;
    NO_ACTIVO = 0;

    dni = Column(String(10), primary_key=True)
    nombre = Column(String(45))
    apellido = Column(String(45))
    telefono = Column(String(45))
    activo = Column(Integer)

    def __init__(self, dni, nombre, apellido, telefono, activo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.activo = activo
