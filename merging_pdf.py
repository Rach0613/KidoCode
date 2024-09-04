import PyPDF2
import tkinter as tk
# messagebox - display message to the users
# filedialog - file selection
from tkinter import filedialog, messagebox

def merge_pdfs(input_pdfs, output_pdf):
    merger = PyPDF2.PdfMerger()

    # try-except error handling to deal with the errors
    try:
        for pdf in input_pdfs:
            merger.append(pdf)

        with open(output_pdf, "wb") as merged_pdf:
            merger.write(merged_pdf)
        
        messagebox.showinfo("Success", f"PDFs has merged successfully!\nOutput saved to: {output_pdf}")
    except Exception as e:
        messagebox.showerror("Error", f" There is an error in merging the PDFs: {e}")

# file browsing
def browse_files():
    filenames = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF Files", "*.pdf")])
    for file in filenames:
        if file not in pdf_files:  # Avoid duplicates
            pdf_files.append(file)
            listbox.insert(tk.END, file)  # Insert selected files into the listbox

# remove selected files
def remove_selected():
    selected_items = listbox.curselection()
    for index in selected_items[::-1]:  # Reverse to avoid issues while removing items
        listbox.delete(index)
        del pdf_files[index]

# save the files to be merged
def save_as():
    output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if output_pdf:
        if pdf_files:
            merge_pdfs(pdf_files, output_pdf)
        else:
            messagebox.showwarning("Warning", "No PDF files are selected for merging.")

# Initialize the main window
root = tk.Tk()
root.title("PDF Merger")

pdf_files = []  # List to store paths of the selected PDF files

# Add widgets to the window
tk.Label(root, text="Selected PDF Files:").pack(pady=5)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
listbox.pack(pady=5)

# buttons
# browse, remove and merge
tk.Button(root, text="Browse PDF Files", command=browse_files).pack(pady=5)
tk.Button(root, text="Remove Selected Files", command=remove_selected).pack(pady=5)
tk.Button(root, text="Merge & Save As", command=save_as).pack(pady=5)

# call the main window of the tkinter
root.mainloop()









