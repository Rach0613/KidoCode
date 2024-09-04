# install pip install pypdfium2
import pypdfium2
# operating system of the files
import os

def pdf_to_images(pdf_path, output_folder, image_format='png'):
    # Ensures the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the PDF file
    pdf = pypdfium2.PdfDocument(pdf_path)
    
    # Iterate over each page in the PDF
    for page_number in range(len(pdf)):
        # Render the page to a bitmap
        page = pdf[page_number]
        bitmap = page.render()
        
        # Convert the bitmap to a PIL image
        image = bitmap.to_pil()
        
        # Save the image
        output_path = os.path.join(output_folder, f"page_{page_number + 1}.{image_format}")
        image.save(output_path)
        print(f"Saved page {page_number + 1} as {output_path}")

    pdf.close()

# select a pdf file path and output folder path
pdf_path = 'C:\\Users\\user\\Downloads\\21583473018.pdf ' # Corrected file path
output_folder = 'C:\\Users\\user\\Downloads\\demo_images'
pdf_to_images(pdf_path, output_folder)