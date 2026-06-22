from PIL import Image

def remove_metadata(input_path, output_path):
    image = Image.open(input_path)

    # Rebuild image data (safer export)
    clean_image = Image.new(image.mode, image.size)
    clean_image.paste(image)

    clean_image.save(output_path)

    print("Clean image exported successfully.")


remove_metadata("sample.jpg", "clean_sample.jpg")