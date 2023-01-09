from PyPDF2 import PdfReader, PdfWriter

uploaderpdf=st.file_uploader('Choose your pdf',accept_multiple_files=True)
reader = PdfReader(uploaderpdf)
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams() 
    writer.add_page(page)

with open(uploaderpdf, "wb") as f:
    writer.write(f)
