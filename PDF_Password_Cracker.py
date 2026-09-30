import PyPDF2
import itertools

def crack_pdf_password(file_path, min_digits=5, max_digits=5):
    """Crack a PDF password by brute force"""
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        if not pdf_reader.is_encrypted:
            print("The PDF file is not encrypted.")
            return

        for digits in range(min_digits, max_digits + 1):
            for attempt in itertools.product('0123456789', repeat=digits):
                password = ''.join(attempt)
                if pdf_reader.decrypt(password) == 1:
                    print(f"Password found: {password}")
                    return
                else:
                    print(f"Failed Attempt: {password}", end='\r')

    print("\nPassword not found.")

# Example usage
file_path = input("Enter the path to the PDF file: ")
crack_pdf_password(file_path, min_digits=3, max_digits=5)