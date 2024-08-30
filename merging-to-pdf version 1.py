# pip install PyPDF2
import PyPDF2

def merge_pdfs(input_pdfs, output_pdf):
    merger = PyPDF2.PdfMerger()

    #try-except 
    # wb-mode (write in binary format)
    try:
        for pdf in input_pdfs:
            merger.append(pdf)

        with open(output_pdf, "wb") as merged_pdf:
            merger.write(merged_pdf)
        
        print(f"PDFs have been merged successfully! Output saved to:{output_pdf}")

    except Exception as e:
        print(f"Error merging the PDFs: {e}")

input_pdfs = ["C:\\Users\\user\\Downloads\\Tahiti_pdf.pdf", "C:\\Users\\user\\Downloads\\skydiving_pdf.pdf", "C:\\Users\\user\\Downloads\\quokka_pdf.pdf"]
output_pdf = "C:\\Users\\user\\Downloads\\merged3_pdf.pdf"

merge_pdfs(input_pdfs, output_pdf)