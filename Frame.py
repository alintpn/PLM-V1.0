import cv2
import os

def extract_frames(video_path, output_dir, frame_rate=10):
    """
    Extract frames from a video at a specified frame rate.

    :param video_path: Path to the input video file.
    :param output_dir: Directory to save the extracted frames.
    :param frame_rate: Number of frames to extract per second.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error opening video file {video_path}")
        return

    fps = video.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 25  # Default to 25 if FPS is not available

    interval = int(fps / frame_rate)
    count = 0
    saved_count = 0

    while True:
        ret, frame = video.read()
        if not ret:
            break

        if count % interval == 0:
            frame_filename = os.path.join(output_dir, f"frame_{saved_count:04d}.png")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        count += 1

    video.release()
    print(f"Extracted {saved_count} frames to {output_dir}")

# Usage
video_path = r'C:\Users\alint\Desktop\OCR\Source\source.mov'  # Corrected with raw string
output_dir = 'extracted_frames'
extract_frames(video_path, output_dir, frame_rate=1)  # Extract 5 frame per second
