
# 📄 Document Analysis Toolkit

**Extract, Analyze, and Understand Documents with AI**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com/)
[![GitHub Stars](https://img.shields.io/github/stars/kerfaiyass54/document-analysis?style=social)](https://github.com/kerfaiyass54/document-analysis/stargazers)

---

## 🚀 Overview

Tired of manually extracting insights from PDFs and other documents? **Document Analysis Toolkit** is your AI-powered solution for effortlessly extracting, summarizing, and analyzing text from documents. This project combines **NLP (Natural Language Processing)** with **PDF parsing** to help you:

✅ **Extract** clean text from PDFs
✅ **Summarize** documents with AI
✅ **Generate** insightful questions from content
✅ **Answer** questions using document context
✅ **Organize** content into manageable passages

Perfect for **legal professionals, researchers, students, and developers** who need to quickly understand and work with large documents.

---

## ✨ Features

📄 **PDF Text Extraction** – Extract raw text from PDFs using `pdfplumber`
🤖 **AI-Powered Summarization** – Summarize documents using Hugging Face's `T5` model
💬 **Question Generation** – Automatically generate questions from document content
🔍 **Contextual Q&A** – Answer questions using the document as context
📊 **Passage Segmentation** – Split documents into logical passages for better analysis
🐳 **Docker Support** – Run the tool in a container with minimal setup

---

## 🛠️ Tech Stack

| Category       | Tools/Libraries                          |
|----------------|------------------------------------------|
| **Language**   | Python 3.8+                              |
| **NLP**        | Hugging Face Transformers (`t5-small`, `valhalla/t5-base-qg-hl`, `deepset/roberta-base-squad2`) |
| **PDF Parsing**| `pdfplumber`                            |
| **Tokenization**| NLTK (`punkt`)                          |
| **Container**  | Docker                                  |
| **OS**         | Linux/macOS/Windows (with Docker)        |

---

## 📦 Installation

### Prerequisites

- **Python 3.8+** (tested with 3.8–3.11)
- **Docker** (optional, for containerized setup)
- **Git** (to clone the repository)

### Quick Start (Local Setup)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kerfaiyass54/document-analysis.git
   cd document-analysis
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: The `requirements.txt` will be auto-generated from `Dockerfile` in this template. For now, install manually:)*
   ```bash
   pip install transformers torch pdfplumber nltk
   ```

4. **Download NLTK data** (one-time setup):
   ```python
   python -c "import nltk; nltk.download('punkt')"
   ```

5. **Run the analyzer**:
   ```bash
   python pdf_analyser.py
   ```

---

### Quick Start (Docker Setup)

1. **Build and run the Docker container**:
   ```bash
   docker-compose up --build
   ```
   - The container will automatically install dependencies and run the analyzer.
   - Extracted text and results will be saved in the `./results` directory on your host machine.

---

## 🎯 Usage

### Basic Usage: Extract and Summarize a PDF

1. **Place your PDF** in the `content/` directory (e.g., `google_terms_of_service_en_in.pdf`).
2. **Run the script**:
   ```bash
   python pdf_analyser.py
   ```
3. **Output**:
   - Extracted text saved to `extracted_text.txt`.
   - Summary printed to the console.
   - Questions and answers generated for each passage.

---

### Advanced Usage: Customize the Analyzer

#### 1. **Modify the PDF Path**
   Change the `pdf_path` variable in `pdf_analyser.py` to point to your PDF:
   ```python
   pdf_path = "path/to/your/document.pdf"
   ```

#### 2. **Adjust Passage Length**
   Control how text is split into passages by changing the word limit in `sent_tokenize`:
   ```python
   if len(current_passage.split()) + len(sentence.split()) < 200:  # Adjust this value
   ```

#### 3. **Use Different Models**
   Replace the Hugging Face models in the pipelines:
   ```python
   summarizer = pipeline("text-generation", model="facebook/bart-large-cnn")  # Alternative model
   ```

#### 4. **Save Results to File**
   Redirect output to a file for later use:
   ```python
   with open("results.txt", "w") as f:
       f.write(summary[0]["generated_text"])
   ```

---



## 🔧 Configuration

### Environment Variables
No environment variables are required, but you can customize:
- `OUTPUT_DIR`: Change where results are saved by modifying `output_text_file` in `pdf_analyser.py`.

### Customization Options
1. **Passage Word Limit**: Adjust the `200` in `sent_tokenize` to control passage size.
2. **Model Selection**: Replace Hugging Face models in the pipelines for different behaviors.
3. **Output Format**: Modify how results are printed or saved (e.g., JSON, CSV).

---

## 🤝 Contributing

We welcome contributions from the community! Here’s how you can help:

### How to Contribute
1. **Fork the repository** and create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
2. **Make your changes** and test thoroughly.
3. **Submit a pull request** with a clear description of your changes.

### Development Setup
1. Clone the repo and install dependencies as described above.
2. Add tests (see the [Testing](#testing) section below).
3. Run the linter:
   ```bash
   pip install flake8
   flake8 pdf_analyser.py
   ```

### Code Style Guidelines
- Follow **PEP 8** conventions.
- Use **type hints** where applicable.
- Write **clear, concise comments**.

### Testing
Add tests using `pytest`:
```bash
pip install pytest
pytest tests/
```

---


## 🐛 Issues & Support

### How to Report Issues
1. Search existing issues to avoid duplicates.
2. Open a new issue with:
   - A clear title.
   - Steps to reproduce the problem.
   - Expected vs. actual behavior.
   - Screenshots or logs if applicable.

### Where to Get Help
- **Discussions**: [GitHub Discussions](https://github.com/kerfaiyass54/document-analysis/discussions)
- **Community**: Join our [Slack/Discord](link-to-community) for real-time help.

### FAQ
**Q: Why is my PDF not being extracted correctly?**
A: Ensure the PDF is not password-protected or corrupted. Try opening it manually to verify.

**Q: How can I use a different NLP model?**
A: Replace the model name in the `pipeline()` calls (e.g., `model="t5-small"`).

**Q: Can I run this on Windows?**
A: Yes! Use the local setup or Docker. Docker works seamlessly across platforms.


## 🚀 Get Started Today!

Ready to analyze your documents like never before? 🚀

1. **Star this repo** to show your support!
2. **Clone and run** the tool on your documents.
3. **Contribute** by improving features or fixing bugs.

Let’s make document analysis **fast, smart, and accessible** for everyone! 💡

