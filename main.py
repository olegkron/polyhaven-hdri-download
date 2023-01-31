
import os

import requests

from check_md5 import check_md5
from colors import bcolors as c
from create_category_folders import create_category_folders
from create_metadata import create_metadata
from download_file import download_file
from link_files import link_files

save_to_dir = 'YOUR DIRECTORY'
asset_size = '4k'
headers = {'User-Agent': 'Mozilla/5.0'}
url_all_hdris = "https://api.polyhaven.com/assets?type=hdris"
url_categories = "https://api.polyhaven.com/categories/hdris"

try:
    categories = requests.get(url=url_categories, headers=headers).json()
    all_hdris = requests.get(url=url_all_hdris, headers=headers).json()
except requests.exceptions.RequestException as e:
    print(c.FAIL + f'Error fetching list of categories & HDRIs: {e}' + c.ENDC)
    all_hdris = {}
    categories = {}
os.makedirs(os.path.join(save_to_dir, 'all'), exist_ok=True) # Create the directory if it doesn't exist.

for file_name, file_info in all_hdris.items(): # Download each HDRI one by one.
    file_exists, file_path, expected_md5 = download_file(file_name, asset_size, save_to_dir, headers)
    if not file_exists : 
        check_md5(file_path, expected_md5, file_name)
        create_category_folders(file_info, save_to_dir, file_path, file_name)
        metadata_path = create_metadata(file_info, save_to_dir, file_name, asset_size, headers)
        link_files(file_path, metadata_path, save_to_dir, file_name, file_info, asset_size, save_to_dir)