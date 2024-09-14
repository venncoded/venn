from src.database_utils import *

def rebuild_tables():
    conn = connect()
    cur = conn.cursor()
    buildUsers(cur)
    buildComments(cur)
    buildGroups(cur)
    buildPassions(cur)
    buildPosts(cur)
    buildUserToPassions(cur)
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
            commentID SERIAL PRIMARY KEY,
            authorID int NOT NULL,
            postID int NOT NULL,
            body VARCHAR(5000),
            postedTime TIMESTAMP default CURRENT_TIMESTAMP
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
            passionID SERIAL PRIMARY KEY,
            title VARCHAR(80) NOT NULL,
            description VARCHAR(5000)
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
            postID SERIAL PRIMARY KEY,
            title VARCHAR(80),
            body VARCHAR(5000),
            author int,
            postedTime TIMESTAMP default CURRENT_TIMESTAMP
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
            groupID SERIAL PRIMARY KEY,
            name VARCHAR(80),
            description VARCHAR(2000)
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)


#Relationship Table Builder
def buildUserToPassions(cur):
    drop_sql = """
        DROP TABLE IF EXISTS usersToPassions
    """
    create_sql="""
        CREATE TABLE usersToPassions(
            userID int,
            passionID int
        )
    """
    cur.execute(drop_sql)
    cur.execute(create_sql)