# Importing necessary modules
from docx2pdf import convert
from pdf2docx import Converter

class Docx2PdfConverter:
    """
    A class for converting DOCX files to PDF format.

    Attributes:
    - docx_path (str): The path to the input DOCX file.
    - pdf_path (str): The path to save the output PDF file.

    Methods:
    - convert_docx_to_pdf(): Converts the input DOCX file to a PDF file.
    """
    def __init__(self, docx_path, pdf_path):
        """
        Initializes a Docx2PdfConverter object.

        Parameters:
        - docx_path (str): The path to the input DOCX file.
        - pdf_path (str): The path to save the output PDF file.
        """
        self.docx_path = docx_path
        self.pdf_path = pdf_path

    def convert_docx_to_pdf(self):
        """
        Converts the input DOCX file to a PDF file.

        Returns:
        - bool: True if the conversion is successful, False otherwise.
        """
        return convert(self.docx_path, self.pdf_path)


class Pdf2DocxConverter:
    """
    A class for converting PDF files to DOCX format.

    Attributes:
    - input_path (str): The path to the input PDF file.
    - output_path (str): The path to save the output DOCX file.

    Methods:
    - convert_pdf_to_docx(): Converts the input PDF file to a DOCX file.
    """
    def __init__(self, input_path, output_path):
        """
        Initializes a Pdf2DocxConverter object.

        Parameters:
        - input_path (str): The path to the input PDF file.
        - output_path (str): The path to save the output DOCX file.
        """
        self.input_path = input_path
        self.output_path = output_path

    def convert_pdf_to_docx(self):
        """
        Converts the input PDF file to a DOCX file.
        Returns:
        - None
        """
        cv = Converter(self.input_path)
        cv.convert(self.output_path)
        cv.close()