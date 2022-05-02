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