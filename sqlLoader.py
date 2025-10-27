import psycopg2

def ejecutar_sql(archivo_sql: str, host: str, dbname: str, user: str, password: str, port: int = 5432):
    # Leer el archivo SQL
    with open(archivo_sql, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    # Conectar a PostgreSQL
    try:
        conexion = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=password,
            port=port
        )

        conexion.autocommit = True  # Permite ejecutar CREATE DATABASE, etc.
        cursor = conexion.cursor()

        print(f"Ejecutando script SQL desde: {archivo_sql}...")
        cursor.execute(sql_script)
        print("Script ejecutado correctamente.")

    except Exception as e:
        print("Error al ejecutar el script SQL:")
        print(e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexion' in locals():
            conexion.close()

if __name__ == "__main__":
    ejecutar_sql(
        archivo_sql="RiwiSport.sql",
        host="localhost",
        dbname="riwisport",
        user="alberto",
        password="alberto123"
    )
