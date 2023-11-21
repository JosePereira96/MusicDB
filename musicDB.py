import mysql.connector
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
loginData = config['database']

def connect():
    db = mysql.connector.connect(
        host=loginData['host'],
        user=loginData['user'],
        password=loginData['password'],
        database = loginData['dbName']
    )

    myCursor = db.cursor()

    #Table Creation
    myCursor.execute("""
    CREATE TABLE IF NOT EXISTS links (
        linkID int NOT NULL AUTO_INCREMENT,
        ownerVideoID varchar(255) NOT NULL,
        URL varchar(512) NOT NULL,
        watched ENUM("YES","NO") NOT NULL,
        PRIMARY KEY (linkID)
    ); 
    """)

    #Creating Views based on the origin website
    myCursor.execute("""CREATE OR REPLACE VIEW youtube AS
                    SELECT *
                    FROM links
                    WHERE URL LIKE "%youtube%" OR URL LIKE "%youtu.be%";
                """)

    myCursor.execute("""CREATE OR REPLACE VIEW spotify AS
                    SELECT *
                    FROM links
                    WHERE URL LIKE "%spotify.com%";
                """)

    myCursor.execute("""CREATE OR REPLACE VIEW bandcamp AS
                    SELECT *
                    FROM links
                    WHERE URL LIKE "%bandcamp.com%";
                """)

    myCursor.execute("""CREATE OR REPLACE VIEW soundcloud AS
                    SELECT *
                    FROM links
                    WHERE URL LIKE "%soundcloud.com%";
                """)

    myCursor.execute("""CREATE OR REPLACE VIEW itunes AS
                    SELECT *
                    FROM links
                    WHERE URL LIKE "%itunes.apple%";
                """)

    #includes all the websites that dont belong to the previous views
    myCursor.execute("""CREATE OR REPLACE VIEW other AS
                    SELECT * FROM links WHERE linkID NOT IN 
                    (
                    SELECT linkID FROM youtube
                    UNION
                    SELECT linkID FROM spotify
                    UNION
                    SELECT linkID FROM bandcamp
                    UNION
                    SELECT linkID FROM itunes
                    UNION
                    SELECT linkID FROM soundcloud 
                    );
                """)

    return (db,myCursor)

def disconnect():
    db.close()