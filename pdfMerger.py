import PyPDF2
import sys
import os

# Specify the input and output folders
input_folder = "/Users/quanshuen/PycharmProjects/pythonProject/PDFMerger/Individual Files"  # Change to your specific folder path
output_folder = "/Users/quanshuen/PycharmProjects/pythonProject/PDFMerger/Merged File"  # Change to your specific folder path

# Initialize the PDF merger
merger = PyPDF2.PdfMerger()

# Iterate over PDF files in the specified input folder
for file in os.listdir(input_folder):
    if file.endswith(".pdf"):
        # Append each PDF file from the input folder to the merger
        merger.append(os.path.join(input_folder, file))
        # merger.append(file)

# Write the merged PDF to the specified output folder
output_path = os.path.join(output_folder, "combinedFiles.pdf")
merger.write(output_path)
merger.close()


