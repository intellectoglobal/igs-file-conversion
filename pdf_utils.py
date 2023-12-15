import fitz  # PyMuPDF module
import os

# The PdfSplitter class is used to split a PDF file into multiple smaller files.
class PdfSplitter:
    def __init__(self, input_path, output_folder):
        self.pdf_document = fitz.open(input_path)
        self.total_pages = self.pdf_document.page_count
        self.output_folder = output_folder

    def split_by_range(self, start_page, end_page, output_name="output"):
        writer = fitz.open()
        self._add_pages_to_writer(writer, start_page - 1, end_page)
        output_pdf_path = os.path.join(
            self.output_folder, f"{output_name}_pages_{start_page}-{end_page}.pdf"
        )
        self._write_part_to_pdf(writer, output_pdf_path)
        print(f"Pages {start_page}-{end_page} saved to {output_pdf_path}")

    def extract_specific_pages(self, page_numbers, output_name="output"):
        writer = fitz.open()
        for page_number in page_numbers:
            self._add_pages_to_writer(writer, page_number - 1, page_number)

        output_pdf_path = os.path.join(
            self.output_folder, f"{output_name}_pages_{'_'.join(map(str, page_numbers))}.pdf"
        )
        self._write_part_to_pdf(writer, output_pdf_path)
        print(f"Pages {', '.join(map(str, page_numbers))} saved to {output_pdf_path}")

    def split_and_write(self, pages_per_part):
        if pages_per_part <= 0 or pages_per_part >= self.total_pages:
            print(f"Error: The specified number of pages per part is invalid - your pdf file pages: {self.total_pages}.")
            pages_per_part = int(input("Enter a valid number of pages: "))
        
        num_parts = (self.total_pages + pages_per_part - 1) // pages_per_part
        os.makedirs(self.output_folder, exist_ok=True)

        for part_number in range(1, num_parts + 1):
            writer = fitz.open()

            start_page = (part_number - 1) * pages_per_part
            end_page = min(part_number * pages_per_part, self.total_pages)

            self._add_pages_to_writer(writer, start_page, end_page)

            output_pdf_path = os.path.join(
                self.output_folder, f"output_part_{part_number}_pages_{start_page + 1}-{end_page}.pdf"
            )

            self._write_part_to_pdf(writer, output_pdf_path)
            print(f"Part {part_number} saved to {output_pdf_path}")

    def _add_pages_to_writer(self, writer, start_page, end_page):
        for page_number in range(start_page, end_page):
            writer.insert_pdf(self.pdf_document, from_page=page_number, to_page=page_number)

    def _write_part_to_pdf(self, writer, output_pdf_path):
        writer.save(output_pdf_path)
        writer.close()


# The PdfMerger class is used to merge multiple PDF files into a single PDF file.
class PdfMerger:
    @staticmethod
    def merge_pdfs(input_files, output_folder, output_file):
        """
        Merge multiple PDF files into a single PDF.

        :param input_files: List of input PDF file paths to merge.
        :param output_folder: Path of the output folder for the merged PDF.
        :param output_file: Name of the output PDF file.
        """
        pdf_merger = fitz.open()

        for input_file in input_files:
            pdf = fitz.open(input_file)
            pdf_merger.insert_pdf(pdf)

        output_path = os.path.join(output_folder, output_file)
        
        output_pdf = fitz.open()  # Create a new PDF document for the merged result
        output_pdf.insert_pdf(pdf_merger)  # Insert the merged content into the new document
        
        output_pdf.save(output_path)
        output_pdf.close()

    @staticmethod
    def get_user_input(message, is_path=False, default=None):
        """
        Get user input with optional default value.

        :param message: Message to display to the user.
        :param is_path: True if the input should be treated as a file path.
        :param default: Default value for the input.
        :return: User input or the default value if provided.
        """
        while True:
            user_input = input(f"{message} ({default}): ").strip() if default else input(f"{message}: ").strip()

            # If a default value is provided and the user entered nothing, use the default
            if default and not user_input:
                return default

            # If the input should be treated as a path and it's not an absolute path, make it absolute
            if is_path and not os.path.isabs(user_input):
                user_input = os.path.abspath(user_input)

            return user_input