from backend.db import get_db

def check_in(reserva_id):
    db = get_db()
    db.execute("UPDATE reservas SET check_in = 1 WHERE id = ?", (reserva_id,))
    db.commit()

def check_out(reserva_id):
    db = get_db()
    db.execute("UPDATE reservas SET check_out = 1 WHERE id = ?", (reserva_id,))
    db.commit()
