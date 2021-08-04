# Se define la clase que va a contener la informacion de obtenida de SEPOMEX, de tal forma que cada codigo genere un
# objeto con todas las propiedades que ofece el concentreado de datos
class CodigoPostal:
    def __init__(self, dCodigo, dAsentamiento, dTipoAsentamiento, dMunicipio, dEstado, dCiudad, dCodigoPostal, cEstado,
                 cOficina, cCodigoPostal, cTipoAsentamiento, cmunicipio, idAsentamiento, dZona, cCveCiudad):
        self._d_codigo = dCodigo
        self._d_asentamiento = dAsentamiento
        self._d_tipo_asentamiento = dTipoAsentamiento
        self._d_municipio = dMunicipio
        self._d_estado = dEstado
        self._d_ciudad = dCiudad
        self._d_codigoPostal = dCodigoPostal
        self._c_estado = cEstado
        self._c_oficina = cOficina
        self._c_codigoPostal = cCodigoPostal
        self._c_tipo_asentamiento = cTipoAsentamiento
        self._c_municipio = cmunicipio
        self._idAsentamiento = idAsentamiento
        self._d_zona = dZona
        self._c_cve_ciudad = cCveCiudad

    # Se general las funciones Get y Set para el manejor de las propiedades de cada objeto

    @property
    def dCodigo(self):
        return self._d_codigo

    @dCodigo.setter
    def dCodigo(self, codigo):
        self._d_codigo = codigo

    @property
    def dAsentamiento(self):
        return self._d_asentamiento

    @dAsentamiento.setter
    def dAsentamiento(self, asentamiento):
        self._d_asentamiento = asentamiento

    @property
    def dMunicipio(self):
        return self._d_municipio

    @dMunicipio.setter
    def dMunicipio(self, municipio):
        self._d_municipio = municipio

    @property
    def dTipoAsentamiento(self):
        return self._d_tipo_asentamiento

    @dTipoAsentamiento.setter
    def dTipoAsentamiento(self, tipoAsentamiento):
        self._d_tipo_asentamiento = tipoAsentamiento

    @property
    def dEstado(self):
        return self._d_estado

    @dEstado.setter
    def dEstado(self, estado):
        self._d_estado = estado

    @property
    def dCiudad(self):
        return self._d_ciudad

    @dCiudad.setter
    def dCiudad(self, ciudad):
        self._d_ciudad = ciudad

    @property
    def dCodigoPostal(self):
        return self._d_codigoPostal

    @dCodigoPostal.setter
    def dCodigoPostal(self, codigoPostal):
        self._d_codigoPostal = codigoPostal

    @property
    def cEstado(self):
        return self._c_estado

    @cEstado.setter
    def cEstado(self, estado):
        self._d_estado = estado

    @property
    def cOficina(self):
        return self._c_oficina

    @cOficina.setter
    def cOficina(self, oficina):
        self._c_oficina = oficina

    @property
    def cCodigoPostal(self):
        return self._c_codigoPostal

    @cCodigoPostal.setter
    def cCodigoPostal(self, codigoPostal):
        self._c_codigoPostal = codigoPostal

    @property
    def cTipoAsentamiento(self):
        return self._c_tipo_asentamiento

    @cTipoAsentamiento.setter
    def cTipoAsentamiento(self, tipoAsentamiento):
        self._c_tipo_asentamiento = tipoAsentamiento

    @property
    def cmunicipio(self):
        return self._c_municipio

    @cmunicipio.setter
    def cmunicipio(self, municipio):
        self._c_municipio = municipio

    @property
    def idAsentamiento(self):
        return self._idAsentamiento

    @idAsentamiento.setter
    def idAsentamiento(self, idMunicipio):
        self._idAsentamiento = idMunicipio

    @property
    def dZona(self):
        return self._d_zona

    @dZona.setter
    def dZona(self, zona):
        self._d_zona = zona

    @property
    def cCveCiudad(self):
        return self._c_tipo_asentamiento

    @cCveCiudad.setter
    def cCveCiudad(self, cveCiudad):
        self._c_cve_ciudad = cveCiudad

    def __str__(self):
        return f" {self._d_codigo}, {self._d_asentamiento}, {self._d_tipo_asentamiento}, {self._d_municipio}, " \
               f"{self._d_estado}, {self._d_ciudad}, {self._d_codigoPostal}, {self._c_estado}, {self._c_oficina}, " \
               f"{self._c_codigoPostal}, {self._c_tipo_asentamiento}, {self._c_municipio}, {self._idAsentamiento}, " \
               f"{self._d_zona}, {self._c_cve_ciudad}"


class Colonia:
    def __init__(self, colonia, id, cp):
        self._colonia = colonia
        self._id = id
        self._cp = cp

    @property
    def colonia(self):
        return self._colonia

    @colonia.setter
    def colonia(self, colonia):
        self._colonia = colonia

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, cp):
        self._cp = cp

    def __str__(self):
        return f" Colonia: {self._colonia}; Codigo Postal: {self._cp}; Id: {self._id} "


class Municipio:
    def __init__(self, municipio, colonias):
        self._municipio = municipio
        self._colonias = colonias

    @property
    def municipio(self):
        return self._municipio

    @municipio.setter
    def municipio(self, municipio):
        self._municipio = municipio

    @property
    def colonias(self):
        return self._colonias

    @colonias.setter
    def colonias(self, colonias):
        self._colonias = colonias

    def __str__(self):
        lcolonias = " "
        for colonia in self._colonias:
            lcolonias += colonia.__str__() + "\n  "
        return f"Municipio: {self._municipio}\n {lcolonias}"


class Estado:
    def __init__(self, estado, municipios):
        self._estado = estado
        self._municipios = municipios

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def municipios(self):
        return self._municipios

    @municipios.setter
    def municipios(self, municipios):
        self._municipios = municipios

    def __str__(self):
        lmunicipios = " "
        for municipio in self._municipios:
            lmunicipios += municipio.__str__() + "\n  "
        return f"Estado: {self._estado}\n {lmunicipios}"


class Registro:
    def __init__(self, estado, municipio, colonia, cp, id):
        self._estado = estado
        self._municipio = municipio
        self._colonia = colonia
        self._cp = cp
        self._id = id

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado

    @property
    def municipio(self):
        return self._municipio

    @municipio.setter
    def municipio(self, municipio):
        self._municipio = municipio

    @property
    def colonia(self):
        return self._colonia

    @colonia.setter
    def colonia(self, colonia):
        self._colonia = colonia

    @property
    def cp(self):
        return self._cp

    @cp.setter
    def cp(self, cp):
        self._cp = cp

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

# Realizo las pruebas de clase
if __name__ == "__main__":
    colonia = Colonia("Del mar", "09", "12330")
    colonia2 = Colonia("olivos", "09", "12330")
    colonia3 = Colonia("arboledas", "09", "12330")
    colonias1 = [colonia, colonia2, colonia3]
    tlahuac1 = Municipio("Tlahuac", colonias1)
    tlahuac2 = Municipio("iztapalapa", colonias1)
    tlahuac3 = Municipio("iztacalco", colonias1)
    municipios1 = [tlahuac1, tlahuac2, tlahuac3]
    estado1 = Estado("CDMX", municipios1)
    print(estado1)



