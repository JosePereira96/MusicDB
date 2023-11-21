import TableClass 
import webbrowser 

musicTable = TableClass.Table("links")

def getYTVideoID(url):
    initialPos = url.find("watch?v=")
    initialPos += len("watch?v=")
    idLength = 11
    videoID = url[initialPos:initialPos+idLength]
    
    return videoID

def createYoutubePlayList(size):
    playList = musicTable.createPlaylist("youtube",size)
    
    playListURL = "http://www.youtube.com/watch_videos?video_ids="
    
    for i in playList:
        videoID = getYTVideoID(i[1])
        playListURL += videoID
        playListURL += ','
        
        musicTable.updateWatched(i[0])
        
    playListURL[:-1]
    webbrowser.open(playListURL)

if __name__ == "__main__":
    createYoutubePlayList(10)