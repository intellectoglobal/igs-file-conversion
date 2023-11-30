from pdf_merger import PdfMerger
# Get user input for PDF files to merge
input_files = []
while True:
    file_path = PdfMerger.get_user_input("Enter the path of a PDF file to merge (or 'done' to finish) ")
    if file_path.lower() == 'done':
        break
    input_files.append(file_path)

# Get user input for the output folder
output_folder = PdfMerger.get_user_input("Enter the path of the output folder", is_path=True, default='output_folder')

# Get user input for the output file
output_file = PdfMerger.get_user_input("Enter name for the output PDF file", default='output.pdf')
if not output_file.endswith(".pdf"):
    output_file += '.pdf'  # Ensure the output file has a '.pdf' extension

# Call the function to merge PDFs
PdfMerger.merge_pdfs(input_files, output_folder, output_file)