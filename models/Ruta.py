from config.db import app, db, ma

class Ruta(db.Model):
    tablename = "tblrutas"

    id_ruta = db.Column(db.Integer, primary_key = True)
    id_user = db.Column(db.Integer, db.ForeignKey('tblusers.id_user'))
    dir_inicio = db.Column(db.String(250))
    dir_fin = db.Column(db.String(250))

    def __init__(self, id_u, dir_inicio, dir_fin):
        self.id_u = id_u
        self.dir_inicio = dir_inicio
        self.dir_fin = dir_fin

with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id_ruta', 'id_user', 'dir_inicio', 'dir_fin')