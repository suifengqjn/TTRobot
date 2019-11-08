import dbm

db_path = './kv_db'

def init():
    set("a", "alice")
    v = get("a")
    print(v)

def set(key,value):
    db = dbm.open(db_path, 'c')
    db[key] = value
    db.close()

def delete(key):
    with dbm.open(db_path, 'c') as db:
        if key.encode(encoding='utf8') in db.keys():
            del db[key]

def get(key):
    with dbm.open(db_path, 'c') as db:
        if key.encode(encoding='utf8') in db.keys():
            return db[key].decode('utf8')
        return None

def has_key(key, db):
    if key.encode(encoding='utf8') in db.keys():
        return True
    return False

def allKeys():
    with dbm.open(db_path, 'c') as db:
        return db.keys()


def main():
    print(allKeys())

    set("a", "alice")
    print(get("a"))

    v = get("a")
    if v != None:
        print("----")





if __name__=="__main__":  
    main()
