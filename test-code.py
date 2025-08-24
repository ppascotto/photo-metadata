from exif import Image

# Open the image in binary read mode
with open("mvft.JPG", "rb") as image_file:
    my_image = Image(image_file)

# Check if the image has EXIF data
if my_image.has_exif:
    print("Has exif")
    # Access and modify tags using attribute notation
    print(f"Original model: {my_image.model}")
    my_image.model = "Modified Camera Model"
    print(f"New model: {my_image.model}")

    # Add a new tag (if it's a recognized EXIF tag)
    my_image.copyright = "Your Name © 2025"

    # Delete a tag
    # del my_image.software
else:
    print("Does not have exif")
# Save the modified image to a new file
with open("modified_image.jpg", "wb") as new_image_file:
    new_image_file.write(my_image.get_file())