import pdfplumber

pdf_path = "D:/projects/document-analysis/content/google_terms_of_service_en_in.pdf"

output_text_file = "extracted_text.txt"

with pdfplumber.open(pdf_path) as pdf:
    extracted_text = ""
    for page in pdf.pages:
        extracted_text += page.extract_text()

with open(output_text_file, "w") as text_file:
    text_file.write(extracted_text)

print(f"Text extracted and saved to {output_text_file}")

# reading pdf content
with open("D:/projects/document-analysis/extracted_text.txt", "r") as file:
    document_text = file.read()

# preview the document content
print(document_text[:500])