from flask import Flask, request, jsonify
from backend import huespedes, reservas, ocupacion, disponibilidad

app = Flask(__name__)

@app.route("/huespedes", methods=["GET", "POST"])
def api_huespedes():
    if request.method == "POST":
        huespedes.agregar_huesped(request.json)
        return '', 201
    return jsonify([dict(row) for row in huespedes.listar_huespedes()])

@app.route("/reservas", methods=["POST"])
def api_reservas():
    reservas.crear_reserva(request.json)
    return '', 201

@app.route("/checkin/<int:id>", methods=["POST"])
def api_checkin(id):
    ocupacion.check_in(id)
    return '', 200

@app.route("/checkout/<int:id>", methods=["POST"])
def api_checkout(id):
    ocupacion.check_out(id)
    return '', 200

@app.route("/disponibilidad", methods=["GET"])
def api_disponibilidad():
    fecha = request.args.get("fecha")
    disponibles = disponibilidad.habitaciones_disponibles(fecha)
    return jsonify([dict(row) for row in disponibles])

if __name__ == "__main__":
    app.run(debug=True)
