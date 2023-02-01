# Polyhaven HDRIs Downloader

A Python script for downloading High Dynamic Range Images (HDRIs) from [Polyhaven](https://polyhaven.com/). This script utilizes the [Pillar](https://github.com/pillar-framework/pillar) library for compressing thumbnails.

## Features

- Downloads all HDRIs by category
- Links one file to multiple categories via hard-linking for easy navigation and saving space
- Adds metadata, tags & thumbnails for each shot
- Compresses and resizes thumbnails
- Checks MD5 hash of each file
- Includes a progress bar
- Compatible with the [ZooTools](https://github.com/mwq/zootools) plugin for Autodesk Maya

## Requirements

- Python 3.6 or higher
- Pillar library

## Usage

1.  Clone the repository

bashCopy code

`git clone https://github.com/olegkron/polyhaven-hdri-download.git`

2.  Install the required packages

Copy code

`pip install -r requirements.txt`

3.  Set up variables in main.py

`save_to_dir = 'YOUR DIRECTORY'
asset_size = '4k'` 3. Run the script`

Copy code

`python hdri_downloader.py`

## Contributing

Contributions are welcome! Please open an issue or create a pull request for any bugs or feature requests.

## License

This project is licensed under the [MIT License](https://github.com/olegkron/polyhaven-hdri-download/LICENSE).
