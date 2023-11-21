import datetime

class File:
    
    def __init__(self,name):
        self.name = name
    
    def writeLog(self,videosVisited,newEntries,time):
        f = open(self.name,'a')
    
        f.write(str(datetime.datetime.now()))
        f.write(f'\nVideos visited: {videosVisited}')
        f.write(f'\nNumber of new links: {newEntries}')
        f.write(f'\nTime Elapsed: {time:.3f} seconds.')
        f.write("\n------------------------------------\n")

        f.close()
        
    def eraseLog(self):
        # delete the data inside file
        # but not the file itself
  
        f = open(self.name, "r+")  
        f.seek(0)  
        f.truncate()  
        f.close()