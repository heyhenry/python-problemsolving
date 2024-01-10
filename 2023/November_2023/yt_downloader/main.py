import os
import re
from pytube import YouTube
import subprocess

def sanitize_filename(filename):
    # Remove invalid characters from the filename
    return re.sub(r'[\/:*?"<>|]', '', filename)

def download_and_process(link, resolution="3840x2160", bitrate="3072k"):
    try:
        # Get the current working directory
        script_dir = os.getcwd()

        # Create a YouTube object
        youtube_obj = YouTube(link)

        # Get the highest resolution stream available
        video_stream = youtube_obj.streams.get_highest_resolution()

        # Sanitize the video title for use in the filename
        video_title = sanitize_filename(youtube_obj.title)

        # Set the filename to the sanitized video title with a .mp4 extension
        video_file = os.path.join(script_dir, f"{video_title}.mp4")

        # Download the video to the current working directory
        video_stream.download(output_path=script_dir, filename=video_title)

        # Explicitly append the .mp4 extension to the video file
        video_file_with_extension = video_file + ".mp4"
        os.replace(video_file, video_file_with_extension)

        # Check if the downloaded video file exists
        if os.path.exists(video_file_with_extension):
            # Process the video with the desired resolution and bitrate using FFmpeg
            subprocess.run(["ffmpeg", "-i", video_file_with_extension, "-s", resolution, "-b:v", bitrate, video_file_with_extension])
            print("Download and processing completed successfully.")
        # else:
        #     print(f"Error: The downloaded video file '{video_file_with_extension}' does not exist.")

    except Exception as e:
        print(f"An error has occurred: {e}")

if __name__ == "__main__":
    # Get the YouTube video URL from user input
    link = input("Enter the YouTube video URL: ")

    # Call the download_and_process function with the option to specify resolution and bitrate
    download_and_process(link, resolution="3840x2160", bitrate="3072k")











