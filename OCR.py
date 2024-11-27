import pytesseract
from PIL import Image
import os

# If you're on Windows and Tesseract is not in your PATH, specify the path
# Uncomment and modify the following line if necessary:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_image(image_path):
    """
    Apply OCR to a preprocessed image.

    :param image_path: Path to the preprocessed image.
    :return: Extracted text as a string.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='eng')  # Specify language as needed
        return text.strip()
    except Exception as e:
        return f"Error processing {image_path}: {e}"

def perform_ocr_on_directory(input_dir, output_file):
    """
    Perform OCR on all images in a directory and save the extracted text to a file.

    :param input_dir: Directory containing preprocessed images.
    :param output_file: Path to the output text file.
    """
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for filename in sorted(os.listdir(input_dir)):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                image_path = os.path.join(input_dir, filename)
                text = ocr_image(image_path)
                f_out.write(f"--- {filename} ---\n")
                f_out.write(text + "\n\n")
                print(f"OCR completed for: {filename}")

    print(f"OCR extraction completed. Extracted text saved to {output_file}")

if __name__ == "__main__":
    input_directory = 'extracted_frames'
    output_text_file = 'extracted_text.txt'
    perform_ocr_on_directory(input_directory, output_text_file)
