import sqlite3
from pathlib import Path
DB_PATH=Path(__file__).with_name('inventory.db')
def connect():
    c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row; return c
def init_db():
    with connect() as c:
        c.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, weight REAL NOT NULL CHECK(weight>0), profit REAL NOT NULL CHECK(profit>=0))')
        if c.execute('SELECT COUNT(*) FROM products').fetchone()[0]==0:
            c.executemany('INSERT INTO products(name,weight,profit) VALUES(?,?,?)',[('Laptop',3,60000),('Monitor',5,25000),('Keyboard',1,3000),('Printer',4,18000),('Tablet',2,22000)])
def get_products():
    with connect() as c: return [dict(r) for r in c.execute('SELECT * FROM products ORDER BY id').fetchall()]
def add_product(name,weight,profit):
    with connect() as c: return c.execute('INSERT INTO products(name,weight,profit) VALUES(?,?,?)',(name,weight,profit)).lastrowid
def delete_product(pid):
    with connect() as c: c.execute('DELETE FROM products WHERE id=?',(pid,))
