from src.venn_table_builder import *

def build_tables():
    rebuild_tables()

def start_with_test_data():
    build_tables()
    conn = connect()
    cur = conn.cursor()
    insert_users(cur)
    insert_passions(cur)
    insert_users_to_passions(cur)
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

def insert_users_to_passions(cur):
    insert_sql="""
        INSERT INTO usersToPassions(userID, passionID)
        VALUES (1,1), (1,2), (2,3), (2,4), (3,1),(3,3),(3,4)
    """
    cur.execute(insert_sql)