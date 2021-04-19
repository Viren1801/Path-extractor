import csv
import threading
import os

directory = r"E:\Imagesforscan"
subfolders, files = [], []


#  returning the folders and files found and returning them
def run_fast_scandir(dir, ext):
    global subfolders
    global files
    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)
    return subfolders, files


# recursively called the run_fast_scandir function to get .jpg files in subfolders also
def get_files(subfolders,ext):
    for dir in list(subfolders):
        sf, f = target=run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    

directory = r"E:\Imagesforscan"
#threading.Thread(target=run_fast_scandir(directory, [".jpg"])).start()
#threading.Thread(target=get_files(subfolders,[".jpg"])).start()
run_fast_scandir(directory, [".jpg"])
get_files(subfolders,[".jpg"])


#  appending the path data to the csv file
with open('paths_data.csv', "w") as outfile:
    writer = csv.writer(outfile, escapechar=' ', quoting=csv.QUOTE_NONE)
    writer.writerow(["folders", "files"])
    writer.writerow([subfolders,files])
