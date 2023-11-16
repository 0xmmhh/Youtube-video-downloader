from sys import argv
from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        video = YouTube(url)

        video_stream = video.streams.get_highest_resolution()

        video_stream.download(output_path)

        print(f"Video has been successfully downloaded to {output_path}")

    except Exception as e:
        print(f"Error downloading video: {str(e)}")

if __name__ == "__main__":
    if len(argv) != 3:
        print("How to use: python download.py <video_url> <output_path>")
        print(r"Example output path: C:\Users\<your-name>\Downloads - It saves the file in the Downloads directory")
    else:
        video_url = argv[1]
        output_path = argv[2]

        download_video(video_url, output_path)
