from sqlalchemy import ColumnDefault
from invicoliqpy import db

class Factureros(db.Model):
    __tablename__ = 'factureros'

    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100))
    actividad = db.Column(db.String(8))
    partida = db.Column(db.String(3))

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_completo': self.nombre_completo,
            'actividad': self.actividad,
            'partida': self.partida,
        }

    def __str__(self):
        return (
            f'ID: {self.id},'
            f'Nombre Completo: {self.nombre_completo}, '
            f'Estructura: {self.actividad}-{self.partida}'
        )

class HonorariosFactureros(db.Model):
    __tablename__ = 'honorarios_factureros'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    facturero = db.Column(db.String(100))
    sellos = db.Column(db.Float, ColumnDefault(0))
    seguro = db.Column(db.Float, ColumnDefault(0))
    nro_comprobante = db.Column(db.String(8))
    tipo = db.Column(db.String(1), ColumnDefault("H"))
    importe_bruto = db.Column(db.Float, ColumnDefault(0))
    iibb = db.Column(db.Float, ColumnDefault(0))
    libramiento_pago = db.Column(db.Float, ColumnDefault(0))
    otras_retenciones = db.Column(db.Float, ColumnDefault(0))
    anticipo = db.Column(db.Float, ColumnDefault(0))
    descuento = db.Column(db.Float, ColumnDefault(0))
    actividad = db.Column(db.String(8))
    partida = db.Column(db.String(3))

    def to_dict(self):
        return {
            'id': self.id,
            'fecha': self.fecha,
            'facturero': self.facturero,
            'sellos': self.sellos,
            'seguro': self.seguro,
            'nro_comprobante': self.nro_comprobante,
            'tipo': self.tipo,
            'importe_bruto': self.importe_bruto,
            'iibb': self.iibb,
            'libramiento_pago': self.libramiento_pago,
            'otras_retenciones': self.otras_retenciones,
            'anticipo': self.anticipo,
            'descuento': self.descuento,
            'actividad': self.actividad,
            'partida': self.partida,
        }

    def __str__(self):
        return (
            f'ID: {self.id},'
            f'Nro Comprobante: {self.nro_comprobante}, '
            f'Estructura: {self.actividad}-{self.partida}'
        )