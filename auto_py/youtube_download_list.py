import pytube

link = "https://www.youtube.com/playlist?list=PLZOm4uzWk9WPwJybXDR6WJzj9VWyflmyt"
p = pytube.Playlist(link)
for video in p.videos:
    video = video.streams.get_highest_resolution()
    video.download()
