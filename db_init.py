from db.db import engine
from db.models import base

def init_db():
    base.metadata.drop_all(bind=engine)
    print ("Tablas borradas correctamente")
    base.metadata.create_all(bind=engine)
    print ("Tablas creadas = OK")
    
if __name__ == "__main__":
    init_db()