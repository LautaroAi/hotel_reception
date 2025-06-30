from backend.db import get_db

def crear_reserva(data):
    db = get_db()
    db.execute("INSERT INTO reservas (huesped_id, habitacion, fecha_entrada, fecha_salida) VALUES (?, ?, ?, ?)", (data["huesped_id"], data["habitacion"], data["entrada"], data["salida"]))
    db.commit()
    