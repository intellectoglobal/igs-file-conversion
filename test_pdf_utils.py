from pdf_utils import PdfSplitter

# Provide the path to the input PDF file
input_pdf_path = 'D:\\file_conversion\\igs-file-conversion\\input_folder\\output_docxtopdf_file.pdf'

# Specify the folder where the output PDF files will be saved
output_folder = 'D:\\file_conversion\\igs-file-conversion\\output_folder'

# Get the number of pages per part from user input
pages_per_part = int(input("Enter the number of pages per part: "))

# Create an instance of the PdfSplitter class
pdf_splitter = PdfSplitter(input_pdf_path, output_folder)

# Split the PDF and write the output files with the specified number of pages per part
pdf_splitter.split_and_write(pages_per_part)
