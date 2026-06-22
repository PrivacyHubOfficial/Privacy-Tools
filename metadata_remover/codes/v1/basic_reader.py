from PIL import Image

# Open image file
image = Image.open("sample.jpg")

# Extract raw metadata
metadata = image.getexif()

# Print raw output
print(metadata)