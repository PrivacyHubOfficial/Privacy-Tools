from PIL import Image
from PIL.ExifTags import TAGS

# Open image
image = Image.open("sample.jpg")

# Extract metadata
raw_metadata = image.getexif()

# Convert to readable format
for key, value in raw_metadata.items():
    tag = TAGS.get(key, key)
    print(f"{tag}: {value}")