#import psycopg2

"""def crear_conexion():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="albany_housing",
            user="postgres",
            password="universal12",
            port="5434"
        )
        print("[INFO] Conexion a PostgreSQL establecida correctamente.")
        return conexion
    except Exception as e:
        print("[ERROR] Error al conectar a la base de datos: {e}")
        raise
"""

#Usando SQLAlchemy para la conexion

from sqlalchemy import create_engine

def obtener_engine():
    usuario = "postgres"
    password = "universal12"
    host = "localhost"
    puerto = "5434"
    base_datos = "albany_housing"

    url = f"postgresql://{usuario}:{password}@{host}:{puerto}/{base_datos}"
    engine = create_engine(url)
    return engine
