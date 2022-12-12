from moviepy import editor
import os
import mimetypes

check_video_files = lambda path: [file for file in os.listdir(path) if mimetypes.guess_type(os.curdir + os.sep + path + os.sep + file)[0].startswith('video')]

def main() -> None:
    path_video = "video"
    path_audio = "audio"
    video_files = check_video_files(path_video)
    if len(video_files) == 0:
        print(f"Folder empty! Or not files video extensions in path: {path_video}")
        return
    for file in video_files:
        print(f"[+] Work with file: {file}")
        video = editor.VideoFileClip(os.curdir + os.sep + path_video + os.sep + file)
        audio = video.audio
        audio.write_audiofile(f"{os.curdir + os.sep + path_audio + os.sep + file}.mp3")
    print("Worked end! Good luck.")

if __name__ == "__main__":
    main()
    