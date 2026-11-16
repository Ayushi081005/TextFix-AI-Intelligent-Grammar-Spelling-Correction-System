# ✦ TextFix AI
### Intelligent Grammar, Spelling Correction & Text Summarization System

TextFix AI is a web-based NLP application designed to improve written content through grammar and spelling analysis, extractive text summarization, and writing-quality evaluation.

The application supports direct text input and document-based analysis through PDF and PPTX files. Users can analyze grammar and spelling, generate concise summaries, or perform both operations together.

It also provides writing analytics and quality indicators to help users understand their content.

## 🚀 Features

### ✍️ Grammar & Spelling Analysis
- Detects spelling errors.
- Identifies grammar issues.
- Provides suggested corrections.
- Displays detected issues clearly.
- Allows users to review individual corrections.
- Supports applying individual or all corrections.
- Allows manual editing of corrected text.

### 🧠 Extractive Text Summarization

TextFix AI includes an extractive summarization module that identifies important sentences from the original text and generates a shorter version.

**Available summary lengths:**
- **Short:** Selects approximately 20% of the original sentences.
- **Medium:** Selects approximately 35% of the original sentences.
- **Long:** Selects approximately 50% of the original sentences.

**How summarization works:**
- Splits the input into individual sentences.
- Processes words and removes common stop words.
- Calculates word importance using TF-IDF-like scoring.
- Assigns scores to sentences based on their important words.
- Selects the highest-ranking sentences.
- Arranges selected sentences in their original order.

The summarizer also provides:
- Original word count.
- Summary word count.
- Original sentence count.
- Selected sentence count.
- Compression percentage.

The approach is extractive, meaning it selects sentences from the original text rather than generating entirely new sentences.

### 📄 Document Support

TextFix AI supports:
- Plain text entered directly into the application.
- PDF documents.
- PowerPoint (`.pptx`) presentations.

The application extracts text from uploaded documents before processing.

### 📊 Writing Analytics

The application calculates:
- Word count.
- Sentence count.
- Character count.
- Characters excluding spaces.
- Average words per sentence.

### 📈 Writing Quality Analysis

TextFix AI evaluates writing using:
- Readability.
- Spelling accuracy.
- Grammar accuracy.
- Sentence clarity.

These indicators are combined into an overall writing-quality score out of 100, accompanied by a descriptive quality label.

### 📝 Editing & Correction Tools

Users can:
- Review original and corrected text.
- Compare detected errors.
- Apply individual corrections.
- Apply all available corrections.
- Manually edit corrected text.
- Copy the corrected text.

### 📱 Responsive Interface

The interface is designed to work across desktop, tablet, and mobile devices.

---

## 🧠 How It Works

TextFix AI provides three analysis modes:

| Mode | Functionality |
|---|---|
| Grammar & Spelling | Detects errors and provides corrections and writing analytics. |
| Summarization | Generates an extractive summary with summary statistics. |
| Both | Performs grammar and spelling analysis alongside summarization. |

### Application Workflow

1. **Input:** Enter text manually or upload a PDF/PPTX document.
2. **Document Extraction:** Extract text from uploaded documents.
3. **Text Processing:** Validate the input and calculate basic statistics.
4. **Analysis Selection:** Choose Grammar & Spelling, Summarization, or Both.
5. **Processing:** Run the selected NLP operations.
6. **Results:** Display corrections, writing analytics, and/or the generated summary.

## 🔍 Analysis Pipeline

### 1. Input Processing
Users can enter text directly or upload supported documents.

### 2. Document Extraction
PDF and PPTX files are processed to extract their textual content.

### 3. Text Statistics
The application calculates word count, sentence count, character count, and average words per sentence.

### 4. Grammar & Spelling Analysis
The text is passed through the LanguageTool-based analysis service. Detected issues are classified and correction suggestions are generated where available.

### 5. Extractive Summarization
When summarization is selected, the summarizer:
- Tokenizes sentences.
- Removes common stop words.
- Calculates word importance.
- Scores sentences.
- Selects important sentences according to the requested summary length.
- Reconstructs the summary while maintaining the original sentence order.

### 6. Writing Quality Evaluation
The application calculates readability, spelling accuracy, grammar accuracy, and sentence clarity.

### 7. Interactive Results
The results dashboard displays the relevant outputs based on the selected analysis mode.

---

## 📐 Writing Quality Metrics

### Readability
Uses a Flesch Reading Ease-based calculation to estimate how easy the text is to read. The score is normalized to a 0–100 range.

### Spelling Accuracy
Estimated using detected spelling errors relative to the total number of words.

### Grammar Accuracy
Estimated using detected grammar issues relative to the total number of words.

### Sentence Clarity
Estimated using sentence length and average words per sentence.

### Overall Score
Combines the individual indicators using weighted scoring.

| Score | Quality |
|---|---|
| 90–100 | Excellent |
| 80–89 | Very Good |
| 70–79 | Good |
| 60–69 | Needs Improvement |
| Below 60 | Poor |

These scores are application-level heuristic indicators, not formal linguistic assessments.

---

## 🛠️ Technology Stack

### Backend
- Python
- Flask

### NLP & Text Analysis
- LanguageTool
- `language_tool_python`
- Regular-expression-based text processing
- TF-IDF-like word scoring for extractive summarization

### Document Processing
- `pdfplumber`
- `python-pptx`

### Frontend
- HTML5
- CSS3
- JavaScript

### Development Tools
- Visual Studio Code
- Python Virtual Environment
- Git
- GitHub

---

## 📂 Project Structure

```text
textfix-ai/
│
├── app.py
│
├── services/
│   ├── spell_checker.py
│   ├── document_parser.py
│   └── summarizer.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── result.css
│   │
│   └── js/
│       └── script.js
│
├── .gitignore
├── requirements.txt
└── README.md
```

*The virtual environment (`venv/`) is created locally and should not be committed to GitHub.*

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ayushi081005/TextFix-AI-Intelligent-Grammar-Spelling-Correction-System.git
```

### 2. Move into the project directory

```bash
cd TextFix-AI-Intelligent-Grammar-Spelling-Correction-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

---

## 💡 Usage

### Option 1 — Grammar & Spelling Analysis

1. Open TextFix AI.
2. Enter or paste text into the input area.
3. Select **Grammar & Spelling**.
4. Submit the text for analysis.
5. Review detected errors and writing-quality metrics.
6. Apply individual or all corrections.
7. Copy the corrected text.

### Option 2 — Text Summarization

1. Enter or paste the text.
2. Select **Summarization**.
3. Choose Short, Medium, or Long summary length.
4. Submit the text.
5. Review the generated summary and compression statistics.

### Option 3 — Combined Analysis

1. Enter text or upload a supported document.
2. Select **Both**.
3. Choose the desired summary length.
4. Submit the input.
5. Review the generated summary alongside grammar, spelling, and writing-quality results.

### Option 4 — Upload a Document

1. Select a PDF or PPTX file.
2. Upload the document.
3. Choose the desired analysis mode.
4. Submit the file.
5. Review the results.

---

## 📄 Supported Input

| Input | Supported |
|---|---|
| Direct text | ✅ |
| PDF | ✅ |
| PPTX | ✅ |
| Website URL summarization | Planned |

The application currently limits uploaded files to 2 MB.

---

## 🔐 Limitations

- Writing-quality scores are heuristic estimates.
- Readability depends on approximate syllable estimation.
- Grammar suggestions depend on the underlying LanguageTool analysis.
- Complex contextual or domain-specific language may require manual review.
- Extractive summarization selects existing sentences and does not generate new ones.
- Summary quality depends on the input text and sentence-scoring approach.
- Very short texts may be returned unchanged.
- Uploaded files are currently limited to 2 MB.
- The application is primarily designed for English text analysis.

---

## 🔮 Future Improvements

Possible future enhancements include:

- Website URL summarization.
- User accounts and analysis history.
- Support for more document formats.
- Advanced contextual grammar correction.
- Improved readability analysis.
- Vocabulary enhancement suggestions.
- Sentence restructuring suggestions.
- Plagiarism detection.
- Multilingual support.
- Exportable analysis reports.
- Cloud deployment.
- Advanced NLP models for contextual analysis.
- Automated testing and CI/CD.

---

## 🌐 Deployment

TextFix AI is designed as a Flask web application and can be deployed using a cloud hosting platform that supports Python applications.

Deployment configuration and the live application URL will be added once the project is deployed.

---

## 🎯 Project Goals

The main goals of TextFix AI are to:

- Provide an accessible grammar and spelling correction tool.
- Combine error correction with useful writing analytics.
- Generate concise summaries from longer text.
- Support analysis of common document formats.
- Help users understand the quality and readability of their writing.
- Provide an interactive interface for reviewing and applying corrections.

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Flask web application development.
- NLP-based text analysis.
- Text preprocessing and tokenization.
- Grammar and spelling detection.
- Extractive text summarization.
- Sentence scoring and ranking.
- Document text extraction.
- File upload handling.
- Writing-quality metrics.
- Frontend and backend integration.
- Git and GitHub workflow.
- Deployment preparation.

---

## 👩‍💻 Author

**Ayushi Shrivastava**

---

## ⭐ Acknowledgements

TextFix AI uses open-source Python libraries and language-processing tools for its grammar analysis, document processing, and text summarization functionality.

## 📜 License

This project is available for educational and portfolio purposes.
