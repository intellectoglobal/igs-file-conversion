import os
import fitz

def merge_pdfs(input_files, output_folder, output_file):
    pdf_merger = fitz.open()

    for input_file in input_files:
        pdf = fitz.open(input_file)
        pdf_merger.insert_pdf(pdf)

    output_path = os.path.join(output_folder, output_file)
    
    output_pdf = fitz.open()  # Create a new PDF document for the merged result
    output_pdf.insert_pdf(pdf_merger)  # Insert the merged content into the new document
    
    output_pdf.save(output_path)
    output_pdf.close()

# Get user input for PDF files to merge
input_files = []
while True:
    file_path = input("Enter the path of a PDF file to merge (or 'done' to finish): ").strip()
    if file_path.lower() == 'done':
        break
    input_files.append(file_path)

# Get user input for the output folder
output_folder = 'D:\\file_conversion\\igs-file-conversion\\output_folder'

# Get user input for the output file
output_file = input("Enter name for the output PDF file: ").strip()
if not output_file.endswith(".pdf") or output_file == '':
    output_file += '.pdf'  # Ensure the output file has a '.pdf' extension

# Call the function to merge PDFs
merge_pdfs(input_files, output_folder, output_file)