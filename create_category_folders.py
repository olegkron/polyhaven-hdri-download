
from os import link, makedirs, path

from colors import bcolors as c


def create_category_folders(file_info, save_to_dir , file_path, file_name):
    for category in file_info["categories"]:  # Create the category folder if it doesn't exist.
        category_folder = path.join(save_to_dir, category)
        makedirs(category_folder, exist_ok=True)
        return category_folder
