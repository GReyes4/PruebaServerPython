from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return "Bienvenido a la API de ejemplo con Flask!"

@app.route('/status')
def status():
    return jsonify({"status": "El servidor esta funcionando correctamente."})

if __name__ == '__main__':
    app.run(debug=True)
