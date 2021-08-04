# Maneja la lectura de el documento con informacion de SEPOMEX
from Servicio.LoggerBase import log


class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        log.debug("Se abrio el recurso")
        self.nombre = open(self.nombre, 'r')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        log.debug("Se cerro el recurso")
        if self.nombre:
            self.nombre.close()
