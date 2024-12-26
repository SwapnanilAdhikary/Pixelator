from PIL import Image
from moviepy import  *
import os
import numpy as np

def convert_frame_to_pixel_art(frame, pixel_size):
    # Convert the frame (numpy array) to an Image
    image = Image.fromarray(frame)
    image = image.convert("RGB")
    original_width, original_height = image.size
    new_width = original_width // pixel_size
    new_height = original_height // pixel_size

    # Apply pixelation
    small_image = image.resize((new_width, new_height), Image.Resampling.NEAREST)
    pixel_art = small_image.resize((original_width, original_height), Image.Resampling.NEAREST)

    # Convert back to a numpy array
    return np.array(pixel_art)


def video_to_pixel_art(input_path, output_path, pixel_size=16, frame_rate=12):
    # Create a temporary directory to store processed frames
    temp_dir = "temp_frames"
    os.makedirs(temp_dir, exist_ok=True)

    # Load the video
    video = VideoFileClip(input_path)

    # Process each frame
    frames = []
    for frame in video.iter_frames(fps=frame_rate, dtype="uint8"):
        pixel_art_frame = convert_frame_to_pixel_art(frame, pixel_size)
        frames.append(pixel_art_frame)

    # Create a new video from processed frames
    pixel_art_video = ImageSequenceClip(frames, fps=frame_rate)
    pixel_art_video.write_videofile(output_path, codec="libx264", audio=False)

    # Cleanup temporary files
    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))
    os.rmdir(temp_dir)

    print(f"Pixel art video saved to {output_path}")


# Example usage
video_to_pixel_art("videoplayback.mp4", "pixel_art_output.mp4", pixel_size=16, frame_rate=12)
