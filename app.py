from flask import Flask, redirect, jsonify, render_template, request
from config.db import app

from api.Users import ruta_user
from api.Rutas import ruta_rutas
from api.Alarmas import ruta_alarmas
from api.Post import ruta_post
from api.Comments import  ruta_comments







app.register_blueprint(ruta_user, url_prefix="/api_user")
app.register_blueprint(ruta_alarmas, url_prefix="/ruta_alarmas")
app.register_blueprint(ruta_post, url_prefix="/api_post")
app.register_blueprint(ruta_comments, url_prefix="/api_comments")
app.register_blueprint(ruta_rutas, url_prefix="/api_rutas")


@app.route("/")
def index():
    return render_template('layout.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')