import sys
import psycopg2 as bd
from logger_base import log

# POOL DE CONEXIONES PYTHON Y POSTGRESQL
class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASWORD = '1004'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

# Metodo de Clase
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexion Exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._conexion

# Metodo de Clase
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor:{cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio un error: {e}')
                sys.exit()
        else:
            return cls._cursor

# Programa Principal
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()