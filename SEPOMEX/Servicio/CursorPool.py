# Genera el cursos para manejar las conexxiones
from Servicio.LoggerBase import log
from Servicio.Conexion import Conexion


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._curor = None

    def __enter__(self):
        log.debug(f"Se inicio el metodo with __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._curor = self._conexion.cursor()
        return self._curor

    def __exit__(self, tipoExcepcion, valorExcepcion, detalleExcepcion):
        log.debug(f"Se ejecuta el metodo __exit__")
        if tipoExcepcion:
            self._conexion.rollback()
            log.error(f"Ocurrio un error, ser realizo rollback: {valorExcepcion} {tipoExcepcion} {detalleExcepcion}")
        else:
            self._conexion.commit()
            log.debug(f"Se realizo commit")
        self._curor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())
