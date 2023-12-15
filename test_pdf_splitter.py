from pdf_utils import PdfSplitter

input_path = "input_folder\\input_file.pdf" 
output_folder = "output_folder"

splitter = PdfSplitter(input_path, output_folder)

# # Split PDF by page range
splitter.split_by_range(start_page=3, end_page=6, output_name="range_output")

# Extract specific pages
splitter.extract_specific_pages(page_numbers=[2], output_name="specific_pages_output")

# Split and write by specified pages per part
splitter.split_and_write(pages_per_part=3)