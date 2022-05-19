from invicoliqpy import db
from invicoliqpy.models import Factureros, HonorariosFactureros
import random
import sys
from faker import Faker
from datetime import datetime


faker = Faker('es_ES')
actividad = ['01-00-01', '01-00-02', '01-00-03', 
'01-00-04', '11-00-01', '12-00-01']

def fake_factureros(n):
    """Generate fake users."""
    for i in range(n):
        facturero = Factureros(
                    nombre_completo=faker.name(),
                    actividad=random.choice(actividad),
                    partida=random.randint(300, 399)
                    )
        db.session.add(facturero)
    db.session.commit()
    print(f'Added {n} fake factureros to the database.')

def fake_honorarios_factureros(n):
    """Generate fake Honorarios Factureros."""
    for i in range(n):
        honorario = HonorariosFactureros(
                    fecha = datetime.utcnow(),
                    facturero=faker.name(),
                    importe_bruto=random.randint(10000, 100000),
                    actividad=random.choice(actividad),
                    partida=random.randint(300, 399)
                    )
        db.session.add(honorario)
    db.session.commit()
    print(f'Added {n} fake honorarios factureros to the database.')

""" if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of factureros you want to create as an argument.')
        sys.exit(1)
    fake_factureros(int(sys.argv[1])) """