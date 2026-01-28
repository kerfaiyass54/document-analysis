import pdfplumber
from transformers import pipeline
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

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

summarizer = pipeline("text-generation", model="t5-small")

summary = summarizer(
    "summarize: " + document_text[:1000],
    max_length=150,
    min_length=30,
    do_sample=False
)

print("Summary:", summary[0]["generated_text"])
sentences = sent_tokenize(document_text)
passages = []
current_passage = ""
for sentence in sentences:
    if len(current_passage.split()) + len(sentence.split()) < 200:  # adjust the word limit as needed
        current_passage += " " + sentence
    else:
        passages.append(current_passage.strip())
        current_passage = sentence
if current_passage:
    passages.append(current_passage.strip())

