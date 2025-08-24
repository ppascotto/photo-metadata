from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif_data(image_path):
    """Extract EXIF data from an image"""
    image = Image.open(image_path)
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            exif_data[tag_name] = value
    return exif_data

def get_gps_info(exif_data):
    """Extract GPS coordinates if available"""
    gps_info = {}
    if "GPSInfo" in exif_data:
        for key in exif_data["GPSInfo"].keys():
            decode = GPSTAGS.get(key, key)
            gps_info[decode] = exif_data["GPSInfo"][key]
    return gps_info

if __name__ == "__main__":
    file_path = "mvft.jpg"  # change this to your jpeg
    exif = get_exif_data(file_path)

    # Print DateTime
    datetime = exif.get("DateTime", "No DateTime found")
    print("Date/Time:", datetime)

    # Print GPS (if available)
    gps = get_gps_info(exif)
    if gps:
        print("GPS Info:", gps)
    else:
        print("No GPS info found")
