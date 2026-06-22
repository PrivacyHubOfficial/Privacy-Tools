from PIL import Image
from PIL.ExifTags import TAGS

def decode_metadata(image_path):
    image = Image.open(image_path)
    metadata = image.getexif()

    decoded = {}

    for key, value in metadata.items():
        tag = TAGS.get(key, key)
        decoded[tag] = value

    return decoded


result = decode_metadata("sample.jpg")

for k, v in result.items():
    print(f"{k}: {v}")