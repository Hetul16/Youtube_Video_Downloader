from pytube import YouTube
link = input("Paste here link")
yt1=YouTube(link)
print(yt1.title)
print(yt1.thumbnail_url)
#below line show all format video
videos=yt1.streams.all()
#for only mp3
#videos=yt1.streams.filter(only_audio=True)
#videos=yt1.streams.filter(only_audio=True)

vid=list(enumerate(videos))
for i in vid:
    print(i)
strm=int(input("Enter quality index number : "))
videos[strm].download()
print("done!!!")


# ______________forplaylist___________________
from pytube import Playlist
py=Playlist("link")
print(f'Downloading : {py.title}')
for video in py.videos:
    video.streams.first().download()