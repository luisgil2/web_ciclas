from config.db import db, app, ma

class Post(db.Model):
    __tablename__ = "tblpost"

    id_post = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('tblusers.id_user'))
    titulo = db.Column(db.String(250))
    contenido = db.Column(db.String(250))
    fecha_hora = db.Column(db.Date)
    
    def __init__(self, id_user, titulo, contenido, fecha_hora):
        self.id_user = id_user
        self.titulo = titulo
        self.contenido = contenido
        self.fecha_hora = fecha_hora

with app.app_context():
    db.create_all()

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id_post', 'id_user', 'titulo', 'contenido', 'fecha_hora')
