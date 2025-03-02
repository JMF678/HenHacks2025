import fitz


def pdf_to_text(pdf_file_path):
    # Open the PDF file
    doc = fitz.open(pdf_file_path)
       
    # Extract text from each page
    text = ''
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text("text")


    return text


# Input the PDF file path from the user
pdf_file_path = input("Enter the path to the PDF file: ")


# Call the function and print the extracted text
text = pdf_to_text(pdf_file_path)
print("Extracted Text:")
print(text)
import HenHack_2025_PDF
import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text = HenHack_2025_PDF.text
    text_to_speech(text)


