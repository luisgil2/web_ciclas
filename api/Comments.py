from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Comentario import Comments, CommentsSchema

ruta_comments = Blueprint("ruta_comments",__name__)

comment_schema = CommentsSchema()
comments_schema = CommentsSchema(many=True)

@ruta_comments.route("/comments", methods=["GET"])
def comments(): 
    resultall = Comments.query.all()
    result = comments_schema.dump(resultall)
    return jsonify(result)

@ruta_comments.route("/savecomments", methods=["POST"])
def savecomments():
    data = request.get_json()
    db.session.add(Comments(**data))
    db.session.commit()
    return comment_schema.jsonify(Comments(**data))

@ruta_comments.route("/updatecomments", methods=["PUT"])
def updatecomments():
    id = request.json['id_comentario']
    nalertas = Comments.query.get(id)
    nalertas.contenido = request.json['contenido']
    nalertas.fecha_hora = request.json['fecha_hora']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_comments.route("/deletecomments/<id>", methods=["DELETE"])
def deletecomments(id):
    comentario = Comments.query.get(id)
    db.session.delete(comentario)
    db.session.commit()
    return jsonify(comment_schema.dump(comentario))