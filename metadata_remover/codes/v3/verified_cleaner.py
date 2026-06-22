from PIL import Image

def remove_and_verify(input_path, output_path):
    image = Image.open(input_path)

    # Strip metadata by reconstructing image
    clean_image = Image.new(image.mode, image.size)
    clean_image.paste(image)

    clean_image.save(output_path)

    # Verification step
    test = Image.open(output_path).getexif()

    if len(test) == 0:
        print("Clean removal confirmed: No metadata found.")
    else:
        print("Warning: Some metadata still exists.")


remove_and_verify("sample.jpg", "clean_sample.jpg")