from concurrent.futures import ThreadPoolExecutor
from moviepy import VideoFileClip
from pathlib import Path
import os
import subprocess
import time

directory =  Path(r"YOUR DIRECTORY HERE")
new_dir = Path(r"OUTPUT DIRECTORY HERE")

def getFrame(full_file):
        clip = VideoFileClip(full_file)
        half_duration = str(clip.duration // 2)
        output = Path(full_file).stem

        command = [

            "ffmpeg",
            "-ss", half_duration,
            "-i", full_file,
            "-frames:v", "1",

            os.path.join(new_dir,output + ".png")
        ]

        try: 
            subprocess.run(command)
            clip.close()

        except Exception as e:
            print(e)
            clip.close()

def getAudio(full_file):
        output = Path(full_file).stem

        command = [
            "ffmpeg",
            "-i", full_file,
            "-vn",
            '-c:a', 'copy',
            
            os.path.join(new_dir,output + '.m4a')
            ]

        try: 
            subprocess.run(command)

        except Exception as e:
            print(e)

def processVideo(file):
        full_file = os.path.join(directory,file)
        if full_file.lower().endswith(".mp4"):
            getFrame(full_file)
            getAudio(full_file)

def main():
    files = os.listdir(directory)

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(processVideo, files)
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print(f"Total runtime: {end-start}")
