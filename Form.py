import PyPDF2
import json

file.pdf=st.file_uploader("upload your file",type[pdf])
# Open the PDF file
with open('file.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    # Loop through all pages
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extractText()

# Convert the text to JSON format
json_data = json.loads(text)

# Access the data in the JSON format
print(json_data['key'])

