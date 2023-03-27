from pytube import YouTube,Playlist
from pathlib import Path
from os import system,name



def convertor(duration: int) -> int: 
    seconds: int = duration % (24 * 3600)
    hour: int = seconds // 3600
    seconds %= 3600 # -> Int
    minutes: int = seconds // 60
    seconds %= 60
     
    return  f"{hour}:{minutes:02d}:{seconds:02d}"

def installer(URL: str) -> object:
    try:
        print(f"\nInstalling {Playlist(URL).title}\n{len(Playlist(URL).video_urls)} videos were found.\n")
        [video.streams.get_highest_resolution().download(str(Path.home() / "Downloads")) and print(f"Installing: {video.title} | {convertor(video.length)}") for video in Playlist(URL).videos]
    except Exception:
       print(f"\nInstalling: {YouTube(URL).title} | Duration: {convertor(YouTube(URL).length)}")
       YouTube(URL).streams.get_highest_resolution().download(str(Path.home() / "Downloads"))
       print(f"Downloaded Successfully: {str(Path.home() / 'Downloads')}!\n")
       
       
def vidInfo(URL: str) -> str:
        
                    print(
        f"""
        Title            : {YouTube(URL).title}      
        Views            : {YouTube(URL).views:,}      
        Author           : {YouTube(URL).author}      
        Publish Date     : {YouTube(URL).publish_date}      
        Duration         : {convertor(YouTube(URL).length)}      
        Age Restricted   : {YouTube(URL).age_restricted}      
        Video ID         : {YouTube(URL).video_id}      
        Channel URL      : {YouTube(URL).channel_url}
        Embed URL        : {YouTube(URL).embed_url}
        Description      : {YouTube(URL).description}      
                    
            """)
                        
def playListInfo(URL: str) -> str:

        if "radio=1" in URL[-7:]:
            print("Can't Proccess custom PlayLists created by youtube from your recommended videos!")
                    
        else:               
            totalDuration = int()
            for vid in Playlist(URL).videos:
                totalDuration += vid.length

                print(
            f"""
            Title       : {Playlist(URL).title}      
            Views       : {Playlist(URL).views:,}      
            Owner       : {Playlist(URL).owner}      
            OwnerID     : {Playlist(URL).owner_id}      
            Duration    : {str(convertor(totalDuration))}
            Last Updated: {Playlist(URL).last_updated}      
            PlayList ID : {Playlist(URL).playlist_id}      
            PlayList URL: {Playlist(URL).playlist_url}      
            Description : {Playlist(URL).description}      
                        
                        """)
                break

def info(URL: str) -> str:
        if  "&list=" not in URL:
            vidInfo(URL)
        else:
            playListInfo(URL)
    
    
def clear() -> None:
    system("cls" if name == "nt" else "clear" )
    
        
        
