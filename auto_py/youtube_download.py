from pytube import YouTube
#한영상만 다운
link = "https://www.youtube.com/watch?v=bKPIcoou9N8&t=1118s"
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
ys.download()
