from prisma import Prisma, register

def get_db():
    db = Prisma()
    db.connect()
    register(db)
    return db

db = get_db()