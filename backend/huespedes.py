from backend.db import get_db

def listar_huespedes():
    db = get_db()
    return db.execute("SELECT * FROM huespedes").fetchall()

def agregar_huesped(data):
    db = get_db()
    db.execute("INSERT INTO huespedes (nombre, documento) VALUES (?, ?)", (data["nombre"], data["documento"]))
    db.commit()

def eliminar_huesped(id):
    db = get_db()
    db.execute("DELETE FROM huespedes WHERE id = ?", (id,))
    db.commit()
