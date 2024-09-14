from src.venn_table_builder import *

def build_tables():
    rebuild_tables()

def start_with_test_data():
    build_tables()
    conn = connect()
    cur = conn.cursor()
    insert_users(cur)
    insert_passions(cur)
    insert_posts(cur)
    insert_groups(cur)
    insert_comments(cur)

    insert_users_to_passions(cur)
    conn.commit()
    conn.close()
    
def insert_users(cur):
    insert_sql="""
        INSERT INTO users(username)
        VALUES ('test_user_1'), ('test_user_2'), ('test_user_3'), ('test_user_4'), ('test_user_5'), ('test_user_6')
    """
    cur.execute(insert_sql)

def insert_passions(cur):
    insert_sql="""
        INSERT INTO passions(title)
        VALUES ('Sports'), 
        ('Board Games'), 
        ('Videogames'), 
        ('Vehicles')
    """
    cur.execute(insert_sql)

def insert_posts(cur):
    insert_sql="""
        INSERT INTO posts(title, body, author)
        VALUES ('Soccer Game','Soccer is super cool and I want to play in the park. Anybody else?', 3), 
        ('Cybertruck Fire','My CYBERTRUCK BURST INTO FLAMES. HOW REFUND?', 3), 
        ('Genshin AR 59','Been playing genshin for a while. Feels like im stuck at ar 59. Any ideas?', 2), 
        ('Chutes and ladders','I want to add landmines to the chutes and ladders map. They move you to a random spot somewhere.', 1),
        ('Football or American Football','Anyone want to play one of the footballs? Or combine them into an amalgamation called Feetball.', 1)
    """
    cur.execute(insert_sql)

def insert_groups(cur):
    insert_sql="""
        INSERT INTO groups(name, description)
        VALUES ('Oxford Volleyball Team','We are the volleyball team for Oxford!'), 
        ('Electric Cars', 'Do you like electric vehicle? Join our group! Save the Planet')
    """
    cur.execute(insert_sql)

def insert_comments(cur):
    insert_sql="""
        INSERT INTO comments(authorID, postID, body)
        VALUES (1,1,'Call it football like the rest of the world America!'), 
        (3, 3, 'Use your resin!')
    """
    cur.execute(insert_sql)

#Relationship Tables
def insert_users_to_passions(cur):
    insert_sql="""
        INSERT INTO usersToPassions(userID, passionID)
        VALUES (1,1), (1,2), (2,3), (2,4), (3,1),(3,3),(3,4)
    """
    cur.execute(insert_sql)