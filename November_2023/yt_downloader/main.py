from pytube import YouTube

def Download(link):
    youtube_obj = YouTube(link)
    # youtube_obj = youtube_obj.streams.get_highest_resolution()
    youtube_obj = youtube_obj.streams.filter(res="1080p").first()
    try:
        youtube_obj.download()
    except:
        print("An error has occurred.")
    print("Download is completed successfully.")

link = input("Enter the YouTube video URL: ")
Download(link)