import piexif
from PIL import Image

file_path = "mvft.jpg"  # change this to your JPEG

# Load existing EXIF data
exif_dict = piexif.load(file_path)

# Overwrite DateTime fields
new_datetime = "2025:01:01 12:00:00"
exif_dict["0th"][piexif.ImageIFD.DateTime] = new_datetime.encode("utf-8")
exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = new_datetime.encode("utf-8")
exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = new_datetime.encode("utf-8")

# Dump back into the same file
exif_bytes = piexif.dump(exif_dict)
image = Image.open(file_path)
image.save(file_path, "jpeg", exif=exif_bytes)

print(f"Updated {file_path} with DateTime {new_datetime}")
