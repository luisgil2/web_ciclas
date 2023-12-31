from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Alertas import Alertas, AlertasSchema

ruta_alarmas = Blueprint("ruta_alarmas",__name__)

alarma_schema = AlertasSchema()
alarmas_schema = AlertasSchema(many=True)

@ruta_alarmas.route("/alarmas", methods=["GET"])
def alarmas(): 
    resultall = Alarmas_ruta.query.all()
    result = alarmas_schema.dump(resultall)
    return jsonify(result)

@ruta_alarmas.route("/savealarma", methods=["POST"])
def savealarma():
    data = request.get_json()
    db.session.add(Alarmas_ruta(**data))
    db.session.commit()
    return alarma_schema.jsonify(Alarmas_ruta(**data))

@ruta_alarmas.route("/updatealarma", methods=["PUT"])
def updatealarma():
    id = request.json['id_alarma']
    nalertas = Alarmas_ruta.query.get(id)
    nalertas.tipo = request.json['tipo']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_alarmas.route("/deletealarma/<id>", methods=["DELETE"])
def deletealarma(id):
    alarma = Alarmas_ruta.query.get(id)
    db.session.delete(alarma)
    db.session.commit()
    return jsonify(alarma_schema.dump(alarma))