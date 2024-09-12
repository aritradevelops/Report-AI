# Run this first if you are using unix  => docker run --rm -p 3000:3000 gotenberg/gotenberg:8

import os
import platform
import requests
from colorama import init, Fore
from docx2pdf import convert as docx_to_pdf

# Initialize colorama for colored logs
init(autoreset=True)

# Gotenberg URL for Unix-based systems
url = "http://localhost:3000/forms/libreoffice/convert"

def convert_to_pdf_unix(doc_path, output_path):
    """Convert a .docx file to PDF using Gotenberg (Unix)."""
    print(f"{Fore.YELLOW}Converting {doc_path} to PDF using Gotenberg...")

    # Make the POST request
    with open(doc_path, 'rb') as file:
        response = requests.post(url, files={'files': file})

    # Save the response as a .pdf file
    with open(output_path, 'wb') as pdf_file:
        pdf_file.write(response.content)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"{Fore.GREEN}File converted and saved as {output_path}")
    else:
        print(f"{Fore.RED}Failed to convert the file. Status code: {response.status_code}")

def convert_docs_to_pdfs(doc_dir='./docs', pdf_dir='./pdfs'):
    """Convert all .docx files in the doc_dir to .pdf in the pdf_dir, based on the OS."""
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    doc_files = [f for f in os.listdir(doc_dir) if f.endswith('.docx')]

    if not doc_files:
        print(f"{Fore.RED}No .docx files found in {doc_dir}")
        return

    print(f"{Fore.CYAN}Found {len(doc_files)} .docx files. Starting conversion to PDF...")

    for doc_file in doc_files:
        doc_path = os.path.join(doc_dir, doc_file)
        pdf_file = os.path.splitext(doc_file)[0] + ".pdf"
        pdf_path = os.path.join(pdf_dir, pdf_file)

        # Determine the platform and choose the conversion method
        current_os = platform.system()
        if current_os == "Linux" or current_os == "Darwin":  # Unix or macOS
            convert_to_pdf_unix(doc_path, pdf_path)
        else:  # Windows or non-Unix systems
            print(f"{Fore.YELLOW}Converting {doc_file} to PDF using docx2pdf...")
            docx_to_pdf(doc_path, pdf_path)
            print(f"{Fore.GREEN}Successfully converted {doc_file} to {pdf_file}\n")

if __name__ == '__main__':
    convert_docs_to_pdfs()
