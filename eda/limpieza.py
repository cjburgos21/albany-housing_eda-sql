import os
import pandas as pd


def limpiar_datos_airbnb():
    # Paso 1: Detectar la ruta base del proyecto automáticamente
    directorio_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Paso 2: Construir rutas completas para origen y destino
    ruta_origen = os.path.join(directorio_proyecto, "data", "listings.csv")
    ruta_destino = os.path.join(directorio_proyecto, "data", "listings_limpio.csv")

    print(f"[DEBUG] Buscando archivo en: {ruta_origen}")

    # Paso 3: Verificar existencia del archivo original
    if not os.path.exists(ruta_origen):
        print("[ERROR] El archivo 'listings.csv' no fue encontrado. Verifica que esté en la carpeta 'data'.")
        return

    print("[INFO] Archivo encontrado. Comenzando limpieza...")

    # Paso 4: Cargar el archivo CSV original
    df = pd.read_csv(ruta_origen)

    # Paso 5: Seleccionar columnas relevantes para análisis de precios por tipo de alojamiento
    columnas_relevantes = ["id", "name", "neighbourhood", "room_type", "price", "minimum_nights", "number_of_reviews"]
    df_filtrado = df[columnas_relevantes].copy()

    print("[INFO] Columnas seleccionadas:")
    print(df_filtrado.columns)

    # Paso 6: Limpiar el campo 'price'
    df_filtrado["price"] = df_filtrado["price"].replace(r'[\$,]', '', regex=True).astype(float)

    # Paso 7: Eliminar filas con datos nulos en columnas clave, incluyendo neighbourhood
    columnas_clave = ["price", "room_type", "minimum_nights", "neighbourhood"]
    registros_antes = len(df_filtrado)
    df_filtrado.dropna(subset=columnas_clave, inplace=True)
    registros_despues = len(df_filtrado)
    print(f"[INFO] Registros eliminados por nulos: {registros_antes - registros_despues}")

    # Paso 8: Eliminar filas con precios o noches mínimas no realistas
    df_filtrado = df_filtrado[df_filtrado["price"] > 0]
    df_filtrado = df_filtrado[df_filtrado["minimum_nights"] <= 365]

    # Paso 9: Guardar el archivo limpio
    df_filtrado.to_csv(ruta_destino, index=False)
    print(f"[INFO] Limpieza completada. Archivo guardado en: {ruta_destino}")


if __name__ == "__main__":
    limpiar_datos_airbnb()
