from Controladores.ControladorEstudiante import ControladorEstudiante
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import conexionData


# ------------------------------------------------------------------------------------------------------
# permite conexión con Postman

app = Flask(__name__)
cors = CORS(app)
miControladorEstudiante = ControladorEstudiante()

# ------------------------------------------------------------------------------------------------------
# Luego se implementarán los métodos en la main en los cuales se definen las rutas
# y tipos de peticiones a las cuales el servidor responderá, este código se puede
# copiar a continuación


@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    json = miControladorEstudiante.index()
    return jsonify(json)


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = miControladorEstudiante.create(data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['GET'])
def getEstudiante(id):
    json = miControladorEstudiante.show(id)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json = miControladorEstudiante.update(id, data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    json = miControladorEstudiante.delete(id)
    return jsonify(json)

# ------------------------------------------------------------------------------------------------------


# Fx que lee el archivo de configuracion del servidor


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

# Crea Json con Metodo GET para correr el servidor "muestra mensaje de servidor corriendo"


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


# Fx que si el servidor corre, va a mostrar la inf del servidor

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://" +
          dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
