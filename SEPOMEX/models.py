from app import db


class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(250))
    municipio = db.Column(db.String(250))
    colonia = db.Column(db.String(250))
    cp = db.Column(db.String(5))
    idasent = db.Column(db.String(4))

    def __str__(self):
        return (
            f"Id: {self.id}, "
            f"Estado: {self.estado}, "
            f"Municipio: {self.municipio}. "
            f"Colonia: {self.colonia}"
            f"Codigo Postal: {self.cp}"
            f"Id SEPOMEX: {self.idasent}"
        )