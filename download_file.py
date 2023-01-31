from os import makedirs, path

from requests import get

from colors import bcolors as c


def download_file(file_name, asset_size, save_to_dir, headers):
    file_path = path.join(save_to_dir, 'all', f'{file_name}_{asset_size}.hdr')
    file_exists = path.exists(file_path)

    if not file_exists:

        print(f'Downloading {file_name}...')
        response = get(url=f'https://api.polyhaven.com/files/{file_name}', headers=headers)
        asset = response.json()
        hdri_link = asset['hdri'][asset_size]['hdr']['url']
        expected_md5 = asset['hdri'][asset_size]['hdr']['md5']

        
        with open(file_path, 'wb') as f:
            response = get(hdri_link, stream=True)
            total = response.headers.get('content-length')
            if total is None:
                f.write(response.content)
            else:
                total = int(total)
                downloaded = 0
                for data in response.iter_content(chunk_size=max(int(total / 1000), 1024 * 1024)):
                    downloaded += len(data)
                    f.write(data)
                    done = int(50 * downloaded / total)
                    print(f'\r[{"=" * done}{" " * (50 - done)}] {downloaded / 1024 / 1024:.2f}/{total / 1024 / 1024:.2f} MB    ', end='')
        print(f'\n{file_name} saved to {file_path}.')     
    else:
        return file_exists, file_path, None
        
    return file_exists, file_path, expected_md5