import sqlite3 as sq

async def bd_conect(user_id):
    db = sq.connect(f"Korzina//{user_id}.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(Id TEXT PRIMARY KEY)")
    db.commit()
    db.close()

async def add_korzina_to_db(user_id, id):
    db = sq.connect(f"Korzina//{user_id}.db")
    cur = db.cursor()
    cur.execute("SELECT * FROM profile")
    bimbam = cur.fetchall()
    blayt = []
    for i in bimbam:
        blayt.append(*i)
    if id in blayt:
        db.close()
        return "Товар уже в корзине!"
    else:
        cur.execute("""
                INSERT INTO profile(Id) VALUES(?)
                """, (id,))
        db.commit()
        db.close()
        return "Добавлена в корзину!"

async def get_id(user_id):
    db = sq.connect(f"Korzina//{user_id}.db")
    cur = db.cursor()
    cur.execute("SELECT Id FROM profile")
    id = cur.fetchall()
    id_bim = []
    for i in id:
        id_bim.append(*i)
    db.commit()
    db.close()
    return id_bim

async def delete_korzina_to_db(user_id, id):
    db = sq.connect(f"Korzina//{user_id}.db")
    cur = db.cursor()
    cur.execute("DELETE FROM profile WHERE Id=?", (id,))
    db.commit()
    db.close()