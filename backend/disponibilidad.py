from backend.db import get_db

def habitaciones_disponibles(fecha):
    db = get_db()
    return db.execute(""" SELECT * FROM habitaciones WHERE id NOT IN (
    SELECT habitacion FROM reservas WHERE ? BETWEEN fecha_entrada AND fecha_salida
    )
    """, (fecha,)).fetchall()
