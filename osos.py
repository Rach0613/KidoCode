# importing necessary libraries
import img2pdf
from PIL import Image
import os #interacting with the file system (creating directories, navigating the file system, checking if a file exists)

def convert_image_to_pdf(img_path, pdf_path):
    # Check if the PDF file already exists
    if os.path.exists(pdf_path):
        print("File already exists. Conversion skipped.")
        return
    
    # Opening the image
    try:
        image = Image.open(img_path)
    except Exception as e:
        print(f"Failed to open image: {e}")
        return

    # Converting image to PDF bytes
    try:
        pdf_bytes = img2pdf.convert(image.filename)
    except Exception as e:
        print(f"Failed to convert image to PDF: {e}")
        return

    # Opening or creating the PDF file
    try:
        with open(pdf_path, "wb") as file:
            # Writing PDF bytes to the file
            file.write(pdf_bytes)
        print("Successfully made PDF file")
    except Exception as e:
        print(f"Failed to write PDF file: {e}")
    
    # Closing the image file
    finally:
        image.close()

# Storing image path
img_path = r"C:\\Users\Ashley Law\Downloads\\picture test.jpg"
# Storing pdf path
pdf_path = r"C:\\Users\Ashley Law\Downloads\\test1_pdf.pdf"

# Call the function to convert the image to PDF
convert_image_to_pdf(img_path, pdf_path)
