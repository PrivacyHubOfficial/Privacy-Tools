from PIL import Image

# Open the image
image = Image.open("my_photo.jpg")

# Read metadata
metadata = image.getexif()

# Print metadata
print(metadata)