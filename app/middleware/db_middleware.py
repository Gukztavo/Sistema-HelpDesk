from controller.db_controller import Db
from sqlalchemy import text

db = Db("mysql","pymysql","root","","localhost","3306","db_chamados")
    
def get_itens():
    with db.connect() as conn:
        return conn.execute(text(f"SELECT * FROM tickets"))
    
def insert_item(title, category_id, description, deadline, created_at, created_by ):
    with db.connect() as conn:
        conn.execute(text(f"INSERT INTO tickets(title, category_id, description, deadline, created_at, created_by ) VALUES ('{title}', '{category_id}','{description}','{deadline}','{created_at}','{created_by}')"))
        conn.commit()


def excluir(id):
    with db.connect() as conn:
        conn.execute(text(f"DELETE FROM tickets WHERE id = '{id}'"))
        conn.commit()