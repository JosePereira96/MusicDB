import youtubeAPI
import FileClass
import TableClass
import re
import time

needledropChannelID = "UCt7fwAhXDy3oNFTAzF2o8Pw"
youtube = youtubeAPI.connect()
musicTable = TableClass.Table("links")
logFile = FileClass.File('logs.txt')

def extractURL(string): 
    # Creating an empty list 
    url_list = [] 
      
    # Regular Expression to extract URL from the string 
    regex = r'\b((?:https?|ftp|file):\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#\/%=~_|])'
      
    # Compile the Regular Expression 
    p = re.compile(regex, re.IGNORECASE) 
      
    # Find the match between string and the regular expression 
    m = p.finditer(string) 
      
    # Find the next subsequence of the input subsequence that find the pattern 
    for match in m: 
        mStart = match.start() 
        mEnd = match.end()
        # Find the substring from the first index of match result to the last index of match result and add in the list 
        url_list.append(string[mStart:mEnd]) 
    
    return url_list

def main():
    start = time.time()


    
    #get all playlist of a given channel 
    request = youtube.playlists().list(
        part="snippet",
        channelId=needledropChannelID,
        maxResults=50
    ) 

    response = request.execute()
    
    #get the playlist ID for the specific playlist
    for result in response['items']:
        if 'Weekly Track Roundup' in result['snippet']['title']:
            playlistID = result['id']
        
    #get all videos from that playlist
    request = youtube.playlistItems().list(
        part = "snippet,status",
        playlistId = playlistID,
        maxResults=25,
    )
    
    videosVisited = 0
    newEntries = 0
    
    #each response will contain 25 videos. 
    #therefore it is necessary to keep creating new requests with the nextPageToken
    while True:
        #for each video get description and store the videoID and descriptions in an array
        #for each description get links and store in array urlList
        
        response = request.execute()
    
        for i in response['items']:
            #the playlist has many types of videos
            #only need to get the videos that have "Weekly Track Roundup" in title
            #and are public.
            if i['status']['privacyStatus'] == 'public' and 'Weekly Track Roundup' in i['snippet']['title']:
                ownerVideoID = i['snippet']['resourceId']['videoId']
                videoDesc = i['snippet']['description']
            
                if musicTable.checkTable(ownerVideoID): #check if the video is already in DB
                    pass
                else:
                    #extract the urls in video description
                    #and store them in db
                    initialpos = videoDesc.find("!") #marks the beggining of tracks
                    finalpos = videoDesc.find("==") #marks the end
                    videoDesc = videoDesc[initialpos:finalpos]
                    
                    videoDescLinks = extractURL(videoDesc)
                    newEntries += len(videoDescLinks)
                    
                    for url in videoDescLinks:
                        musicTable.insert(ownerVideoID,url,"NO") #insert to DB            
        
                videosVisited += 1

        #sends a new request if nextPageToken is not null. otherwise break loop
        if 'nextPageToken' in response.keys():
            token = response['nextPageToken']
        
            request = youtube.playlistItems().list(
                part = "contentDetails,id,snippet,status",
                playlistId = playlistID,
                pageToken = token,
                maxResults=25,
            )
            response = request.execute()
        else:
            break
            
    end = time.time()
            
    #write to log file
    logFile.writeLog(videosVisited,newEntries,end-start)      

if __name__ == "__main__":
    main()