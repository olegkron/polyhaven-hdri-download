import json
from os import makedirs, path

import requests
from PIL import Image
from requests import exceptions, get

from colors import bcolors as c


def create_metadata(file_info, save_to_dir, file_name, asset_size, headers):
    try:
        file_info["tags"].append(asset_size) # add the asset size to the tags
        hdri_info_dir = path.join(save_to_dir, 'all',  f'{file_name}_{asset_size}_hdr_fileDependencies') # Creates Directory
        makedirs(hdri_info_dir, exist_ok=True)
        metadata_path = path.join(hdri_info_dir, f'{file_name}_{asset_size}.zooInfo') # Save the metadata as a zooInfo file.
        thumbnail = get(url= f'https://cdn.polyhaven.com/asset_img/thumbs/{file_name}.png' , headers=headers)
        with open(path.join(hdri_info_dir, 'thumbnail.jpg'), 'wb') as f:
            f.write(thumbnail.content)

        img = Image.open(path.join(hdri_info_dir, 'thumbnail.jpg'))
        width, height = img.size
        aspect_ratio = width/height
        new_width, new_height = 512, 512
        if width > height:
            new_height = int(new_width/aspect_ratio)
        else:
            new_width = int(new_height*aspect_ratio)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img = img.convert("RGB")
        img.save(path.join(hdri_info_dir, 'thumbnail.jpg'), "JPEG", optimize=True, quality=85)
        # print(f'Thumbnail saved to {path.join(hdri_info_dir, "thumbnail.jpg")}.')
        
        with open(metadata_path, 'w') as f:
            metadata = {"assetType": "IBL","creators": "","websites": "","tags": ', '.join(file_info["tags"]),"description": "","saved": "[]","animation": "None"}
            json.dump(metadata, f, indent=4)
        # print(f'Metadata saved to {metadata_path}.')
        return metadata_path

    except exceptions.RequestException as e:
        print(c.FAIL + f'Error downloading thumbnail: {e}'+ c.ENDC)
    except Exception as e:
        print(c.FAIL + f'Error saving thumbnail: {e}' + c.ENDC)
