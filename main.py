from  pytube import Playlist
playlist =  Playlist("https://youtube.com/playlist?list=PLTV1jAY3nKHMotVkWRcqH4EGPOqliQZ23 ") # enter the url here 

for video in playlist.videos:
    print("Downloading:{} with url:{}".format(video.title, video.watch_url))
    video.streams. \
        filter(type='video' , progressive=True , file_extension='mp4').\
            order_by('resolution').\
            desc().\
            first().\
                download()
