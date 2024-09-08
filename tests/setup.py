from src.venn_table_builder import *

def build_tables():
    rebuild_tables()

def start_with_test_data():
    build_tables()
    conn = connect()
    cur = conn.cursor()
    insert_users(cur)
    insert_passions(cur)
    conn.commit()
    conn.close()
    
def insert_users(cur):
    insert_sql="""
        INSERT INTO users(username)
        VALUES ('test_user_1'), ('test_user_2'), ('test_user_3')
    """
    cur.execute(insert_sql)

def insert_passions(cur):
    insert_sql="""
        INSERT INTO passions(title)
        VALUES ('Sports'), ('Board Games'), ('Videogames'), ('Vehicles')
    """
    cur.execute(insert_sql)