from src.database_utils import *

def rebuildTables():
    conn = connect()
    cur = conn.cursor()
    buildUsers(cur)
    buildComments(cur)
    buildGroups(cur)
    buildPassions(cur)
    buildPosts(cur)
    conn.commit()
    conn.close()

def buildUsers(cur):
    drop_sql = """
        DROP TABLE IF EXISTS users
    """
    create_sql = """
        CREATE TABLE users(
            userID SERIAL PRIMARY KEY,
            username VARCHAR(40) NOT NULL,
            firstName VARCHAR(40),
            middleName VARCHAR(40),
            lastName VARCHAR(40),
            preferredName VARCHAR(40),
            town VARCHAR(40),
            country VARCHAR(40),
            state VARCHAR(40)
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)

def buildComments(cur):
    drop_sql = """
        DROP TABLE IF EXISTS comments
    """
    create_sql="""
        CREATE TABLE comments(
            commentID SERIAL PRIMARY KEY
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)

def buildPassions(cur):
    drop_sql = """
        DROP TABLE IF EXISTS passions
    """
    create_sql="""
        CREATE TABLE passions(
            passionID SERIAL PRIMARY KEY
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)

def buildPosts(cur):
    drop_sql = """
        DROP TABLE IF EXISTS posts
    """
    create_sql="""
        CREATE TABLE posts(
            postID SERIAL PRIMARY KEY
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)

def buildGroups(cur):
    drop_sql = """
        DROP TABLE IF EXISTS groups
    """
    create_sql="""
        CREATE TABLE groups(
            groupID SERIAL PRIMARY KEY
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)