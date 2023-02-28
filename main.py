import os
import time

from settings import MAIN_DIRS
from telegram import send_message

dirs = []

# Extract all the dirs
for main_dir in MAIN_DIRS:
    for walked_dir, walked_dirs, files in os.walk(main_dir):
        if walked_dirs:
            for dir_to_apped in walked_dirs:
                dirs.append(f"{walked_dir}/{dir_to_apped}")

# Create a list with the number of files by dir
files_by_dir = [len(os.listdir(dir)) for dir in dirs]

while True:
    # Check every 10 minutes
    print("sleeping")
    print(dirs)
    time.sleep(60)
    for position in range(len(dirs)):
        # get number of files from the directory
        number_of_files = len(os.listdir(dirs[position]))

        # If we don't have more files than previously, them notify
        if (number_of_files != 0) and (
            files_by_dir[position] == number_of_files
        ):
            send_message(dirs[position])

        # update the number of files in the directory
        files_by_dir[position] = number_of_files
