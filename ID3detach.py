import os
import glob
import shutil
from mutagen.id3 import ID3, ID3NoHeaderError

files_path = 'file-path-here'
destination_path = 'Destination-after-processing-path-here'
os.chdir(files_path)

audio_files = glob.glob('*.mp3')

for i, file in enumerate(audio_files, start=1):
    try:
        audio = ID3(file)
        audio.delete()
        print(f"Removed ID3 tags from: {file}")
    except ID3NoHeaderError:
        print(f"No ID3 tags found in: {file}")
    
    new_name = f"Unknown_file_{i}.mp3"
    new_path = os.path.join(destination_path, new_name)
    shutil.move(file, new_path)
    print(f"Renamed '{file}' to '{new_name}' and moved to '{destination_path}'")

print("Processing completed.")