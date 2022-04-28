from invicoliqpy import db
from invicoliqpy.models import Factureros
import random
import sys
from faker import Faker


def create_fake_factureros(n):
    """Generate fake users."""
    faker = Faker('es_ES')
    for i in range(n):
        facturero = Factureros(
                    nombre_completo=faker.name(),
                    actividad=random.randint(100, 500),
                    partida=random.randint(300, 399)
                    )
        db.session.add(facturero)
    db.session.commit()
    print(f'Added {n} fake factureros to the database.')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of factureros you want to create as an argument.')
        sys.exit(1)
    create_fake_factureros(int(sys.argv[1]))

