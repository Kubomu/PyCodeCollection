# Importing the yt-dlp library, which is a fork of youtube-dl with additional features and fixes
import yt_dlp

# Prompting the user to enter the URL of the video to be downloaded
url = input('Enter video url(Its free and in HD):')

# Creating an empty dictionary to store options for the YoutubeDL object
ydl_opts = {}

# Creating a YoutubeDL object with the options dictionary as an argument
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # Initiating the download process with the user-provided URL
    ydl.download([url])

# Printing a success message to the console once the download is completed
print("Download completed......... Asante!")

