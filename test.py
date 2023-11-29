from file_conversion import Docx2PdfConverter, Pdf2DocxConverter

# Convert DOCX to PDF
docx_path = "D:\\file_conversion\\igs-file-conversion\\input_folder\\sample2.docx" #input_pdffile_path
pdf_path = "D:\\file_conversion\\igs-file-conversion\\output_folder\\output_docxtopdf_file.pdf" #output_docxfile_path 

# Creating an instance of Docx2PdfConverter
converter = Docx2PdfConverter(docx_path, pdf_path)

# Performing the conversion from DOCX to PDF
converter.convert_docx_to_pdf()

# Convert PDF to DOCX
pdf_path = "D:\\file_conversion\\igs-file-conversion\\input_folder\\input_file.pdf" #input_ocxfile_path
docx_path = "D:\\file_conversion\\igs-file-conversion\\output_folder\\output_pdftodocx_file.docx" #output_pdffile_path 

# Creating an instance of Pdf2DocxConverter
converter = Pdf2DocxConverter(pdf_path, docx_path)

# Performing the conversion from PDF to DOCX
converter.convert_pdf_to_docx()
