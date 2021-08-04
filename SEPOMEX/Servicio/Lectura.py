from Dominio.Clases import Colonia, Municipio, Estado, Registro
from Servicio.ManejoArchivo import ManejoArchivos
from Servicio.LoggerBase import log



def cargaObjeto():
    with ManejoArchivos("CPdescarga.txt") as archivo:
        colonias = list()
        municipios = list()
        estados = list()
        cambioMunicipio = "Álvaro Obregón"  # Cambia cada que el municipio cambia
        cambioEstado = "Ciudad de México"  # Cambia cada que el estado cambia
        for linea in archivo:
            lista = linea.split("|")
            if len(lista) == 15 and lista[0] != "d_codigo":
                tupla = tuple(lista)
                if tupla[4] == cambioEstado:
                    if tupla[3] == cambioMunicipio:
                        colonia = Colonia(tupla[1], tupla[12], tupla[6])
                        colonias.append(colonia)
                    # Se alcamacenan las colonias cuando cambia el municipio
                    else:
                        municipio = Municipio(cambioMunicipio, colonias)
                        municipios.append(municipio)
                        cambioMunicipio = tupla[3]
                        colonias = []
                # Se almacenan las colonias y los municipios cuando cambia el estado
                else:
                    municipio = Municipio(cambioMunicipio, colonias)
                    municipios.append(municipio)
                    cambioMunicipio = tupla[3]
                    colonias = []
                    estado = Estado(cambioEstado, municipios)
                    estados.append(estado)
                    cambioEstado = tupla[4]
                    municipios = []
    # En este bloque se almacena todo lo restrante de guardar desde el ultimo cambio de estado o municipio
    municipio = Municipio(cambioMunicipio, colonias)
    municipios.append(municipio)
    estado = Estado(cambioEstado, municipios)
    estados.append(estado)

    return estados


# Realiza la carga de la información de SEPOMEX a la base de datos
def cargaBase():
    with ManejoArchivos("CPdescarga.txt") as archivo:
        for linea in archivo:
            lista = linea.split("|")
            if len(lista) == 15 and lista[0] != "d_codigo":
                registro = Registro(lista[4], lista[3], lista[1], lista[6], lista[12])
                DAO.insertar(registro)
    log.info("Todo el archivop fue registrado en la base")


if __name__ == "__main__":
    cargaBase()
