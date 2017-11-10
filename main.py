#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, send_file, request, jsonify
from flask_restful import reqparse, abort, Api, Resource, url_for
import socket
import random


app = Flask(__name__)
api = Api(app)


class Movimiento(Resource):
    def get(self):
        #distancias que envía el sensor ultrasónico
        frente = request.args.get('frente')
	inicio = request.args.get('inicio')
        derecha = request.args.get('derecha')
        izquierda = request.args.get('izquierda')
        atras = request.args.get('atras')
        foo =["izquerda", "derecha", "frente"]
        return {"avazar": {random.choice(foo): "50"},
		"inicio": inicio, 
                "imagen": "https://pruebamoodle.ga/imagen?derecha="+derecha+"&izquierda="+izquierda+"&frente="+frente
    }


api.add_resource(Movimiento, '/movimiento')

@app.route("/imagen")
def serveImage():
    #generacion de la imagen de manera dinámica 
    frente = request.args.get('frente')
    derecha = request.args.get('derecha')
    izquierda = request.args.get('izquierda')
    atras = request.args.get('atras')
    try:
        image = Image.new('RGB', (300, 300))
        draw = ImageDraw.Draw(image)
        draw.line((150, 70, 150, 150), fill=None)
        draw.line((70, 150, 230, 150), fill=None)
        #distancia al frente
        draw.text((140, 50), frente, font=None, fill=None)
        #distancia a la derecha
        draw.text((235, 145), derecha, font=None, fill=None)
        #distancia a la izquierda
        draw.text((50, 145), izquierda, font=None, fill=None)
        image.save("./tmp/img.jpg")
        return send_file("./tmp/img.jpg")
    except:
        return jsonify({"Error": "Argumentos insuficientes para generar imagen"})
        
if __name__ == '__main__':
    app.run(debug=True)
