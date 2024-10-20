from pytube import YouTube

def downloadLink(link):
    try:
        yt = YouTube(link)
        yt._js = None  # Clear any cached JS if needed

        # Use alternative stream selection
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if stream:
            print("Downloading...")
            stream.download()
            print("Download completed successfully!")
        else:
            print("No suitable stream found.")

    except Exception as e:
        print(f"An error occurred: {e}")

link = input("Enter the YouTube video URL: ")
downloadLink(link)
