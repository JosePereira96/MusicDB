import musicDB

db, myCursor = musicDB.connect()

class Table:
    def __init__(self,name):
        self.name = name

    def clear(self):
        myCursor.execute("DELETE FROM {}".format(self.name))
        db.commit()    
    
    def insert(self,ownerVideoID,URL,watched):
        myCursor.execute("""
                INSERT INTO {}(ownerVideoID,URL,watched)
                VALUES ("{}","{}","{}");
            """.format(self.name,
                       ownerVideoID,
                       URL,
                       watched)
                )
        db.commit() 
        
    def checkTable(self,videoID):
        myCursor.execute("""
            SELECT * FROM {} WHERE ownerVideoID = "{}"
            """.format(self.name,videoID))
        
        return bool(myCursor.fetchall())
        
    def printContents(self):
        myCursor.execute("SELECT * FROM {}".format(self.name))
        results = myCursor.fetchall()
        
        for i in results:
            print(i)
            
    def updateWatched(self,linkID):
        myCursor.execute("""
            UPDATE {}
            SET watched = "YES"
            WHERE linkID = "{}";
        """.format(self.name,linkID))
        db.commit() 
        
    def updateURL(self,linkID,URL):
        myCursor.execute("""
            UPDATE {}
            SET URL = "{}"
            WHERE linkID = "{}"
        """.format(self.name,URL,linkID))


    def createPlaylist(self,origin,size):
        myCursor.execute("""
            SELECT linkID,URL FROM {} 
            WHERE watched = "NO"
            LIMIT {};
        """.format(origin, size))
        
        result = myCursor.fetchall()
        return result