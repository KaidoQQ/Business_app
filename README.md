# Business AI Assistant

**Business AI Assistant** is a desktop application designed to analyze and develop startup business plans using **Google Gemini AI**. It automates strategic analysis and prototyping based on business descriptions.

## 🚀 Key Features

### 1. Rating & Strategic Advice
* Acts as a Senior Venture Capital Analyst to "stress-test" the business plan.
* Identifies vulnerabilities and tags them with `[RISK]` followed by a brief explanation.
* Suggests specific improvements using `[IMPROVEMENT]` and `[REVISED TEXT]` tags.
* Highlights missing critical information (e.g., financial projections) with the `[GAP]` tag.

### 2. Mini-Site (MVP) Generation
* Transforms a business plan into a professional landing page using **React (Vite)**, **Tailwind CSS**, and **Lucide Icons**.
* Implements "Security by Design," including input sanitization to prevent XSS.
* Provides a clear modular folder structure and a deployment guide for Vercel or Netlify.

### 3. PESTEL & SWOT Analysis
* Conducts a deep macro-environmental analysis updated for 2026 market trends.
* Generates a detailed SWOT matrix in Markdown table format.
* Provides a strategic synthesis (TOWS) and 5 critical recommendations for the startup.

## 🛠️ Tech Stack

* **Language**: Python 3.x.
* **GUI Framework**: Tkinter.
* **AI Model**: Gemini 2.5 Flash Lite.
* **Supported Formats**: Word (.docx), PDF (.pdf), and Text (.txt).

## ⚙️ Setup & Installation

1. **API Key**: Create a file at `settings/tokens.env` and add your key: `GEMINI=your_api_key_here`.
2. **Dependencies**:
  ```bash
  pip install google-genai python-dotenv pypdf python-docx
  ```

3. **Run Application**:
  ```bash
  python GUI.py
  ```

*Note: This is a practice project intended to explore AI integration in business workflows.*

*Created by [KaidoQQ](https://github.com/KaidoQQ)*