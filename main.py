import logging
import os
import time

from settings import MAIN_DIRS, WAIT_TIME
from telegram import send_message


def configure_logging():
    logging.basicConfig(
        filename='logs/main.log',
        filemode='w',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def check_dirs():
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
        time.sleep(WAIT_TIME)
        for position in range(len(dirs)):
            # get number of files from the directory
            number_of_files = len(os.listdir(dirs[position]))

            # If we don't have more files than previously, them notify
            if (number_of_files != 0) and (
                files_by_dir[position] == number_of_files
            ):
                logging.warning("Sending message")
                send_message(dirs[position])

            # update the number of files in the directory
            files_by_dir[position] = number_of_files


if __name__ == '__main__':
    configure_logging()
    check_dirs()
