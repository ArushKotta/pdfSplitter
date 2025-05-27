import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])

        output_path = os.path.join(output_folder, f'page_{i + 1}.pdf')
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        print(f'Saved: {output_path}')

if __name__ == "__main__":
    input_pdf = input("Enter the input PDF filename (e.g., document.pdf): ")
    output_dir = input("Enter the output folder name: ")
    split_pdf(input_pdf, output_dir)
