from config.db import app, db, ma

class Comments(db.Model):
    __tablename__ = "tblcomments"  # Corregido: __tablename__ en lugar de tablename

    id_comentario = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey('tblpost.id_post'))  # Corregido: tblPosts en lugar de tblPost
    contenido = db.Column(db.String(250))
    fecha_hora = db.Column(db.Date)
    
    def __init__(self, id_post, contenido, fecha_hora):
        self.id_post = id_post
        self.contenido = contenido
        self.fecha_hora = fecha_hora

with app.app_context():
    db.create_all()

class CommentsSchema(ma.Schema):
    class Meta:
        fields = ('id_comentario', 'id_post', 'contenido', 'fecha_hora')