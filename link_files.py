from os import link, makedirs, path
from pathlib import Path

from colors import bcolors as c


def link_files(file_path, metadata_path, hdri_info_dir, file_name, file_info, asset_size, save_to_dir):
    linked_folders = []
    existing_links = []
    for category in file_info["categories"]: # Link the HDRI to its category folders.
        try:
            category_folder = path.join(save_to_dir, category)
            makedirs(category_folder, exist_ok=True)
            full_file_name = f'{file_name}_{asset_size}.hdr'
            category_path = path.join(save_to_dir, category, f'{full_file_name}')
            if not path.exists(category_path):
                link(file_path, category_path)
                linked_folders.append(category)
            # links the metadata file to the tag folder
            makedirs(path.join(save_to_dir, category, f'{file_name}_{asset_size}_fileDependencies'), exist_ok=True)
            link(metadata_path, path.join(save_to_dir, category, f'{file_name}_{asset_size}_fileDependencies', f'{file_name}_{asset_size}.zooInfo')) # links zooinfo file
            link(path.join(save_to_dir,"all" ,f'{file_name}_{asset_size}_hdr_fileDependencies', 'thumbnail.jpg'), path.join(save_to_dir, category, f'{file_name}_{asset_size}_fileDependencies', 'thumbnail.jpg'))# links thumbnail file 
        except FileExistsError as e:
            existing_links.append(category)

        except Exception as e:
            print(c.FAIL + f'Error linking {full_file_name} to {category} folder: {e}'+ c.ENDC)
    if linked_folders:
        print(c.OKGREEN + f'Linked file {full_file_name} to {linked_folders}.' + c.ENDC)
    if existing_links:
        print(c.FAIL + f'{full_file_name} already exists in {existing_links}.' + c.ENDC)
    if not linked_folders and not existing_links:
        print(c.FAIL + f'Error linking {full_file_name} to any category folders.' + c.ENDC)