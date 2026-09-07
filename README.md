# ✦ TextFix AI

### Intelligent Grammar & Spelling Correction System

TextFix AI is a web-based NLP application designed to analyze written content, detect spelling and grammar issues, suggest corrections, and provide meaningful insights into writing quality.

The application supports both direct text input and document-based analysis through PDF and PPTX files. Along with correcting errors, TextFix AI provides writing analytics such as word count, sentence count, character count, readability, spelling accuracy, grammar accuracy, and sentence clarity.

---

## 🚀 Features

### ✍️ Grammar & Spelling Analysis

- Detects spelling errors
- Detects grammar issues
- Provides suggested corrections
- Displays detected issues clearly
- Allows users to review individual corrections
- Supports applying corrections to the text

### 📄 Document Support

TextFix AI can analyze:

- Plain text entered directly into the application
- PDF documents
- PowerPoint (`.pptx`) presentations

The application extracts the text from uploaded documents before sending it through the analysis pipeline.

### 📊 Writing Analytics

The application provides:

- Word count
- Sentence count
- Character count
- Characters excluding spaces
- Average words per sentence

### 📈 Writing Quality Analysis

TextFix AI calculates an overall writing-quality score using multiple indicators:

- Readability
- Spelling accuracy
- Grammar accuracy
- Sentence clarity

The result is presented as an overall score out of 100 along with a descriptive quality label.

### 📝 Editing & Correction Tools

Users can:

- Review the original text
- Compare it with corrected text
- Review detected errors
- Apply individual corrections
- Apply all available corrections
- Manually edit the corrected text
- Copy the corrected text

### 📱 Responsive Interface

The interface is designed to work across:

- Desktop
- Tablet
- Mobile devices

---

## 🧠 How It Works

TextFix AI follows a simple NLP-based processing pipeline:

```text
                ┌─────────────────────┐
                │      User Input     │
                └──────────┬──────────┘
                           │
                ┌──────────▼──────────┐
                │ Text / PDF / PPTX   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Document Extraction │
                │   (PDF / PPTX)      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Text Validation &   │
                │    Statistics       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Grammar & Spelling  │
                │      Analysis       │
                └──────────┬──────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
   ┌──────────────────┐       ┌──────────────────┐
   │ Error Detection  │       │ Corrected Text   │
   └────────┬─────────┘       └────────┬─────────┘
            │                          │
            └────────────┬─────────────┘
                         ▼
                ┌─────────────────────┐
                │ Writing Quality &   │
                │     Analytics       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Result Dashboard │
                └─────────────────────┘
                
🔍 Analysis Pipeline
1. Input

Users can either:

Enter text manually
Upload a PDF
Upload a PPTX presentation
2. Document Processing

For uploaded documents, TextFix AI extracts the textual content before analysis.

3. Text Statistics

The extracted text is processed to calculate basic writing statistics including:

Number of words
Number of sentences
Number of characters
Average words per sentence

4. Grammar & Spelling Analysis

The text is passed through the application's grammar and spelling analysis service.

Detected issues are classified into spelling and grammar errors and suggestions are generated where available.

5. Writing Quality Evaluation

The application evaluates the text using:

Readability score
Spelling accuracy
Grammar accuracy
Sentence clarity

These metrics are combined into an overall writing-quality score.

6. Interactive Results

The user receives an analysis dashboard containing:

Total detected issues
Spelling errors
Grammar errors
Writing quality score
Detailed writing metrics
Original text
Corrected text
Correction actions

📐 Writing Quality Metrics
Readability

TextFix AI uses a Flesch Reading Ease-based calculation to estimate how easy the text is to read.

The score is normalized to a 0–100 range in the application.

Spelling Accuracy

Spelling accuracy is estimated based on the number of detected spelling errors relative to the total number of words.

Grammar Accuracy

Grammar accuracy is estimated using detected grammar issues relative to the total number of words.

Sentence Clarity

Sentence clarity is estimated using sentence length and the average number of words per sentence.

Overall Score

The overall writing-quality score combines the individual metrics using weighted scoring.

The application categorizes the resulting score as:

Score	Quality
90–100	Excellent
80–89	Very Good
70–79	Good
60–69	Needs Improvement
Below 60	Poor

These scores are application-level heuristic indicators intended to provide useful writing feedback rather than a formal linguistic assessment.

🛠️ Technology Stack
Backend
Python
Flask
NLP / Text Analysis
LanguageTool
language_tool_python
Regular-expression based text processing
Document Processing
pdfplumber
python-pptx
Frontend
HTML5
CSS3
JavaScript
Development
Visual Studio Code
Python Virtual Environment
Git
GitHub


📂 Project Structure
textfix-ai/
│
├── app.py
│
├── services/
│   ├── spell_checker.py
│   └── document_parser.py
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
├── venv/
│
├── .gitignore
├── requirements.txt
└── README.md

⚙️ Installation
1. Clone the repository
git clone https://github.com/Ayushi081005/TextFix-AI-Intelligent-Grammar-Spelling-Correction-System.git
2. Move into the project directory
cd TextFix-AI-Intelligent-Grammar-Spelling-Correction-System
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment
Windows PowerShell
venv\Scripts\Activate.ps1
Windows Command Prompt
venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
▶️ Running the Application

Start the Flask application:

python app.py

The application will run locally at:

http://127.0.0.1:5000/

Open the address in your browser to use TextFix AI.

💡 Usage
Option 1 — Enter Text
Open TextFix AI.
Enter or paste text into the input area.
Submit the text for analysis.
Review detected spelling and grammar issues.
Review the writing-quality metrics.
Apply individual or all corrections.
Copy the corrected text.
Option 2 — Upload a Document
Select a supported PDF or PPTX file.
Upload the document.
TextFix AI extracts the document text.
The extracted text is analyzed.
Review the generated corrections and writing analytics.

📄 Supported Input
Input	Supported
Direct text	✅
PDF	✅
PPTX	✅

The application currently limits uploaded files to 2 MB.


🔐 Limitations

TextFix AI is intended as a practical writing-assistance application and should not be considered a replacement for professional editorial or linguistic review.

Some limitations include:

Writing-quality scores are heuristic estimates.
Readability depends on approximate syllable estimation.
Grammar suggestions depend on the underlying LanguageTool analysis.
Complex contextual or domain-specific language may require manual review.
Uploaded files are currently limited to 2 MB.
The application is primarily designed for English text analysis.


🔮 Future Improvements

Possible future enhancements include:

 User accounts and analysis history
 More document formats
 Advanced contextual grammar correction
 Improved readability analysis
 Vocabulary enhancement suggestions
 Sentence restructuring suggestions
 Plagiarism detection
 Multilingual support
 Exportable analysis reports
 Cloud deployment
 Advanced NLP models for contextual analysis
 Automated testing and CI/CD

🌐 Deployment

TextFix AI can be deployed as a Flask web application using a cloud hosting platform that supports Python applications.

Deployment configuration and the live application URL will be added here once the project is deployed.

🎯 Project Goals

The main goals of TextFix AI are to:

Provide an accessible grammar and spelling correction tool.
Combine error correction with useful writing analytics.
Support analysis of common document formats.
Help users understand the quality and readability of their writing.
Provide an interactive interface for reviewing and applying corrections.


📚 Learning Outcomes

This project demonstrates practical experience with:

Flask web application development
NLP-based text analysis
Text preprocessing
Grammar and spelling detection
Document text extraction
File upload handling
Writing-quality metrics
Frontend and backend integration
REST-style application routing
Git and GitHub workflow
Deployment preparation


👩‍💻 Author

Ayushi Shrivastava



⭐ Acknowledgements

TextFix AI uses open-source Python libraries and language-processing tools to provide its analysis and document-processing functionality.

📜 License

This project is available for educational and portfolio purposes.