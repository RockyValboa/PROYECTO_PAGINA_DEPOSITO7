# Importamos la libreria Flask
# mongodb+srv://sebastianvillanuevamosquera:Sebastian_20041@sebastianvillanueva.axpkrnv.mongodb.net/?retryWrites=true&w=majority&appName=SebastianVillanueva
from flask import Flask, render_template, jsonify
# Importamos la librería de Pymongo para conectarnos a la base de datos MongoDB
from pymongo import MongoClient
# Importamos flask_cors para poder enviar y recibir datos con nuestra aplicación
from flask_cors import CORS # CORS: Intercambio de recursos de origen cruzado

#Creamos la aplicación Flask con Flask
app = Flask(__name__)

# Habilitamos nuestra API
CORS(app)
# Copiamos la cadena de conexión a la BD de Mongo
MONGO_URI = "mongodb+srv://sebastianvillanuevamosquera:Sebastian_20041@sebastianvillanueva.axpkrnv.mongodb.net/?retryWrites=true&w=majority&appName=SebastianVillanueva"
# Conectamos con la BD mediante la cadena de conexión
mongo= MongoClient(MONGO_URI)
# Seleccionamos la base de datos
base_datos = mongo.proyecto_pagina_deposito
colection_products = base_datos.products


#Definimos las rutas de la aplicación
@app.route("/", methods = ["GET"])
def principal():
    # Consultamos los productos en la colección
    products = list(colection_products .find())
    # Convertimos los _id a cadena de caractéres
    for item in products:
        item["_id"] = str(item["_id"])

    # Enviamos la lista de productos al archivo html
    return render_template("index.html", products = products)
# Tambien podemos crear una API
@app.route("/api/videos", methods = ["GET"])
def api_products():
    products = list(colection_products.find())
    for item in products:
        item["_id"] = str(item["_id"])

    # La API retorna la lista de videos al FrontEnd
    return jsonify ({"products": products}),201 # 201: Código HTTP de solicitud exitoso
    
#Indicamos a Python que esta es la aplicación principal
if __name__ == "__main__":
    app.run(debug = True)