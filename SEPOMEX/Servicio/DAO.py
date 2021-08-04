from Servicio.CursorPool import CursorDelPool
from Servicio.LoggerBase import log
from Servicio.Lectura import cargaBase
from Servicio.ManejoArchivo import ManejoArchivos
from Dominio.Clases import Registro


class DAO:
    '''
    DAO (Data Access Objet)
    '''
    _TABLA = "CREATE TABLE registro (id serial PRIMARY KEY, estado varchar, municipio varchar, colonia varchar, " \
             "cp varchar, idasent varchar)"
    _INSERTAR = "INSERT INTO registro(estado, municipio, colonia, cp, idasent) VALUES(%s, %s, %s, %s, %s)"
    _BUSCARCP = "SELECT registro.id FROM registro WHERE registro.cp = %s"
    _BUSCARCOL = "SELECT registro.id FROM registro WHERE registro.colonia = %s"
    _BUSCARMUN = "SELECT registro.id FROM registro WHERE registro.municipio = %s"
    _BUSCAREST = "SELECT registro.id FROM registro WHERE registro.estado = %s"
    _SELECCIONAR = "SELECT * FROM registro"

    @classmethod
    def crearBase(cls):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._TABLA)
            return
        finally:
            return

    @classmethod
    def insertar(cls, registro):
        with CursorDelPool() as cursor:
            valores = (registro.estado, registro.municipio, registro.colonia, registro.cp, registro.id)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Registro insertado')
            return

    @classmethod
    def buscar(cls, busqueda):
        if busqueda.isdigit():
            with CursorDelPool() as cursor:
                valores = (busqueda,)
                cursor.execute(cls._BUSCARCP, valores)
                registro = cursor.fetchall()
                lista = []
                for elemento in registro:
                    lista.append(elemento[0])
                return lista
        else:
            busqueda = busqueda.title()
            with CursorDelPool() as cursor:
                valores = (busqueda,)
                cursor.execute(cls._BUSCARCOL, valores)
                registro = cursor.fetchall()
                log.info(f"Registros agregados de colonias: {cursor.rowcount}")
                lista = []
                for elemento in registro:
                    lista.append(elemento[0])
            with CursorDelPool() as cursor:
                valores = (busqueda,)
                cursor.execute(cls._BUSCARMUN, valores)
                registro = cursor.fetchall()
                log.info(f"Registros agegados de Municipios: {cursor.rowcount}")
                for elemento in registro:
                    lista.append(elemento[0])
            with CursorDelPool() as cursor:
                valores = (busqueda,)
                cursor.execute(cls._BUSCAREST, valores)
                registro = cursor.fetchall()
                log.info(f"Registros agregados de Estados: {cursor.rowcount}")
                for elemento in registro:
                    lista.append(elemento[0])
        log.info(f"Registros todales: {len(lista)}")
        arreglo = set(lista)
        log.info(f"Registros sin duplicados: {len(arreglo)}")
        lista = list(arreglo)
        return lista

    @classmethod
    def cargaBase(cls):
        try:
            with ManejoArchivos("CPdescarga.txt") as archivo:
                for linea in archivo:
                    lista = linea.split("|")
                    if len(lista) == 15 and lista[0] != "d_codigo":
                        registro = Registro(lista[4], lista[3], lista[1], lista[6], lista[12])
                        DAO.insertar(registro)
            log.info("Todo el archivo fue registrado en la base")
        finally:
            log.info("La base ya esta registrada")

    @classmethod
    def baseNoVacia(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            conteo = cursor.rowcount
            return conteo


if __name__ == '__main__':
    DAO.crearBase()
    print(DAO.baseNoVacia()==0)
    # registro = DAO.buscar("aguascalientes")
    # print(registro != [])
    # print(len(registro))

    # with CursorDelPool() as cursor:
    #     valores = ("registro.cp", ("13011", ))
    #     cursor.execute("SELECT registro.id FROM registro WHERE registro.cp = '13011'")
    #     registro = cursor.fetchall()
    #
    # print(registro)
