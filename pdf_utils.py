import fitz  # PyMuPDF module
import os

class PdfSplitter:
    def __init__(self, input_path, output_folder):
        """
        Initializes the PdfSplitter class.

        Parameters:
        - input_path (str): Path to the input PDF file.
        - output_folder (str): Path to the folder where the output PDF files will be saved.
        """
        self.pdf_document = fitz.open(input_path)
        self.total_pages = self.pdf_document.page_count
        self.output_folder = output_folder

    def split_and_write(self, pages_per_part):
        """
        Splits the input PDF file into parts of specified pages and writes them to separate PDF files.

        Parameters:
        - pages_per_part (int): Number of pages per part.

        Note: If pages_per_part is less than or equal to 0 or greater than or equal to the total pages,
        it prompts the user to enter a valid number.
        """
        if pages_per_part <= 0 or pages_per_part >= self.total_pages:
            print(f"Error: The specified number of pages per part is invalid - your pdf file pages: {self.total_pages}.")
            pages_per_part = int(input("Enter a valid number of pages: "))
        
        num_parts = (self.total_pages + pages_per_part - 1) // pages_per_part

        # Create the output folder if it doesn't exist
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
        """
        Adds pages to the PDF writer.

        Parameters:
        - writer: PDF writer object.
        - start_page (int): Starting page number.
        - end_page (int): Ending page number (exclusive).
        """
        for page_number in range(start_page, end_page):
            writer.insert_pdf(self.pdf_document, from_page=page_number, to_page=page_number)

    def _write_part_to_pdf(self, writer, output_pdf_path):
        """
        Writes the PDF writer to a PDF file.

        Parameters:
        - writer: PDF writer object.
        - output_pdf_path (str): Path to the output PDF file.
        """
        writer.save(output_pdf_path)
        writer.close()
