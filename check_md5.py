from hashlib import md5

from colors import bcolors as c


def check_md5(path, expected_md5, file_name):
    with open(path, "rb") as f: # Check the file hash
        md = md5()
        for chunk in iter(lambda: f.read(4096), b""):
            md.update(chunk)
    if md.hexdigest() != expected_md5:
        print(c.FAIL + f'Error downloading {file_name}: MD5 hash does not match source: ' + expected_md5 + c.ENDC)
        return False
    else:
        # print(c.OKGREEN + "MD5 hash OK: " + f'{file_name}' + c.ENDC)
        return True