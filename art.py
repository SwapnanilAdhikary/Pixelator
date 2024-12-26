from PIL import Image

def convert_to_pixel_art(image_path, output_path, pixel_size=16):
    image = Image.open(image_path)
    image = image.convert("RGB")
    original_width, original_height = image.size
    new_width = original_width // pixel_size
    new_height = original_height // pixel_size

    small_image = image.resize((new_width, new_height), Image.Resampling.NEAREST)

    pixel_art = small_image.resize((original_width, original_height), Image.Resampling.NEAREST)

    pixel_art.save(output_path)

    print(f"Pixel art saved to {output_path}")

convert_to_pixel_art("1326332.jpeg", "pixel_art_output2.png", pixel_size=16)
