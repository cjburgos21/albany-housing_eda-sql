import pandas as pd
from eda.conexion import obtener_engine

"""
def obtener_resumen_dataset():
    conn = crear_conexion()
    query = 
    SELECT
        COUNT(*) AS total_registros,
        COUNT(DISTINCT neighbourhood) AS zonas_distintas,
        COUNT(DISTINCT room_type) AS tipos_alojamiento
    FROM listings_limpio;
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def estadisticas_precio():
    conn = crear_conexion()
    query = 
        SELECT
            MIN(price) AS precio_minimo,
            MAX(price) AS precio_maximo,
            ROUND(AVG(price), 2) AS promedio,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) AS mediana
        FROM listings_limpio;
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def precio_por_tipo_alojamiento():
    conn = crear_conexion()
    query = 
        SELECT
            room_type,
            COUNT(*) AS cantidad,
            ROUND(AVG(price), 2) AS precio_promedio,
            MIN(price) AS precio_min,
            MAX(price) AS precio_max
        FROM listings_limpio
        GROUP BY room_type
        ORDER BY precio_promedio DESC;
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    print("[INFO] Resumen genral del dataset:")
    print(obtener_resumen_dataset())
    print("\n[INFO] Estadisticas de precios:")
    print(estadisticas_precio())
    print("\n[INFO] Precios por tipo de alojamiento:")
    print(precio_por_tipo_alojamiento())

"""

def obtener_resumen_dataset():
    print("[INFO] Resumen general del dataset:")
    engine = obtener_engine()
    query = """
        SELECT
            COUNT(*) AS total_registros,
            COUNT(DISTINCT neighbourhood) AS zonas_distintas,
            COUNT(DISTINCT room_type) AS tipo_alojamiento
        FROM listings_limpio;
    """
    df = pd.read_sql_query(query, engine)
    return df

def estadisticas_precio():
    print("[INFO] Estadisticas de precios:")
    engine = obtener_engine()
    query = """
        SELECT
            MIN(price) AS precio_minimo,
            MAX(price) AS precio_maximo,
            ROUND(AVG(price), 2) AS promedio,
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) AS mediana
        FROM listings_limpio;
    """
    df = pd.read_sql_query(query, engine)
    return df

def precio_por_tipo_alojamiento():
    print("[INFO] Precios por el tipo de alojamiento")
    engine = obtener_engine()
    query = """
        SELECT 
            room_type,
            COUNT(*) AS cantidad,
            ROUND(AVG(price), 2) AS precio_promedio,
            MIN(price) AS precio_min,
            MAX(price) AS precio_max
        FROM listings_limpio
        GROUP BY room_type
        ORDER BY precio_promedio DESC;
    """
    df = pd.read_sql_query(query, engine)
    return df