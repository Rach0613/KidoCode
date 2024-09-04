# using img2pdf library
# importing necessary libraries
import img2pdf
from PIL import Image
import os

# storing image path
img_path = "C:\\Users\\user\\Downloads\\quokka.jpeg"

# storing pdf path
pdf_path = "C:\\Users\\user\\Downloads\\quokka_pdf.pdf"

# opening image
image = Image.open(img_path)

# setting A4 page dimensions in points (1 point = 1/72 inch)
a4_width = img2pdf.mm_to_pt(210)  # A4 width in points
a4_height = img2pdf.mm_to_pt(297)  # A4 height in points
a4inpt = (a4_width, a4_height)

# converting image to PDF with A4 layout, resizing image to A4 dimensions
pdf_bytes = img2pdf.convert(image.filename, 
                            layout_fun=img2pdf.get_layout_fun(a4inpt))

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file........")
