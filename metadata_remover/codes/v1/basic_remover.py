from PIL import Image

# Open image
image = Image.open("sample.jpg")

# Copy image (removes metadata in most cases)
clean_image = image.copy()

# Save new image
clean_image.save("clean_sample.jpg")

print("Image saved without metadata.")