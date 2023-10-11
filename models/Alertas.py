from config.db import app, db, ma

class Alertas(db.Model):
  
    __tablename__ = "tblalertas"
    id_ruta = db.Column(db.Integer, db.ForeignKey('tblusers.id_user'))
    id_alarma = db.Column(db.Integer, primary_key = True)
    tipo = db.Column(db.String(250))

    def __init__(self ,tipo):
        self.tipo = tipo
        
with app.app_context():
    db.create_all()

class AlertasSchema(ma.Schema):
    class Meta:
        fields = ('id_alarma', 'id_ruta','tipo')       