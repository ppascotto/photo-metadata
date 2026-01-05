This is used to extract the Google Takeout metadata when exporting out of Google Photos.

## How to use

Assumptions:
- Data has been extracted from Google Photos

1. Copy the script into the folder where all media and JSON files are
2. Run the script:

```
./get_metadata.py
```
3. If any files are not found, a message will appear in the terminal. If this happens, delete the Output folder, fix the issue (see below) and try again
4. The output files will be created in the Output folder, with the name: YYYYMMDD_HHMMSS.extension

## Current Limitations:

- The EXIF data of the media files is unmodified, only the filename is updated.
- Some JSON files contain long names of the media files that are cut off, this needs to be fixed manually.
