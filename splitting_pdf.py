# PdfReader class - read PDFs
# PdfWriter class - write in PDFs
from PyPDF2 import PdfReader, PdfWriter

# creating a function to split the pdf
# 2 param (input path & folder)
def split_pdf(input_pdf_path, output_folder):
    # Create a PDF reader object
    pdf_reader = PdfReader(input_pdf_path)

    # Loop through each page and create a separate PDF for each page
    for page_number in range(len(pdf_reader.pages)):
        # Create a PDF writer object
        pdf_writer = PdfWriter()

        # Add the current page to the writer
        pdf_writer.add_page(pdf_reader.pages[page_number])

        # Define the output path for each page
        output_pdf_path = f"{output_folder}/page_{page_number + 1}.pdf"

        # Write the single-page PDF to the output path
        # open the pdf file in binary write mode
        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdf_writer.write(output_pdf_file)

        print(f"Created: {output_pdf_path}")

# Path to the input PDF
# define a path
input_pdf_path = "C:\\Users\\user\\Downloads\\C++ Programming From Problem Analysis to Program Design [5th Edition] book.pdf"

# Folder where the output PDFs will be saved
output_folder = "C:\\Users\\user\\Downloads\\demo_split"

# call the function
split_pdf(input_pdf_path, output_folder)
