import sqlite3 as sq

async def bd_conect(user_id):
    db = sq.connect(f"SQL//{user_id}.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(Id TEXT PRIMARY KEY)")
    cur.execute("CREATE TABLE IF NOT EXISTS profile2(Target TEXT, Sum INT, User_sum INT)")
    db.commit()
    db.close()

async def add_korzina_to_db(user_id, id):
    db = sq.connect(f"SQL//{user_id}.db")
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
    db = sq.connect(f"SQL//{user_id}.db")
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
    db = sq.connect(f"SQL//{user_id}.db")
    cur = db.cursor()
    cur.execute("DELETE FROM profile WHERE Id=?", (id,))
    db.commit()
    db.close()

async def get_pay_target(user_id):
    db = sq.connect(f"SQL//{user_id}.db")
    cur = db.cursor()
    cur.execute("SELECT Target, Sum, User_sum FROM profile2")
    get_pay = cur.fetchall()
    if get_pay:
        db.commit()
        db.close()
        return get_pay
    else:
        db.commit()
        db.close()
        return False

async def create_target_pay(user_id, data_target, data_sum):
    db = sq.connect(f"SQL//{user_id}.db")
    cur = db.cursor()
    cur.execute("INSERT INTO profile2(Target, Sum, User_sum) VALUES(?,?,?)",
                (data_target, data_sum, 0,))
    db.commit()
    db.close()

async def delete_target_pay(user_id, data_target, data_sum):
    db = sq.connect(f"SQL//{user_id}.db")
    cur = db.cursor()
    cur.execute("DELETE FROM profile2 WHERE Target=?", (data_target,))
    cur.execute("DELETE FROM profile2 WHERE Sum=?", (data_sum,))
    db.commit()
    db.close()

async def update_user_sum(user_id, target, price):
    count = 0
    count += int(price)
    db = sq.connect(f"SQL//{user_id}.db")
    cur = db.cursor()
    cur.execute("SELECT User_sum FROM profile2")
    num = cur.fetchone()
    for i in num:
        count += int(i)
    cur.execute("UPDATE profile2 SET User_sum = ? WHERE Target = ?", (count, target,))
    db.commit()
    db.close()