# 🔎 SiteSense

An AI-powered web application that summarizes the content of any website using Groq's Llama 3.3 70B model.

---

## Demo

![SiteSense Demo](assets/demo.gif)

---

## Features

- Summarize any public website using its URL
- AI-powered summaries using **Groq's Llama 3.3 70B** model
- Multiple summary styles:
  - 😊 Friendly
  - 💼 Professional
  - 📋 Bullet Points
  - 🧒 Explain Like I'm 5
- Extracts only the meaningful content from webpages
- Removes advertisements, navigation menus, scripts, headers, and footers
- Markdown-formatted summaries
- Interactive web interface built with Gradio

---

# How It Works

```text
        User
          │
          ▼
 Enter Website URL
          │
          ▼
  Fetch Website HTML
          │
          ▼
 BeautifulSoup Parser
(Removes scripts, ads & menus)
          │
          ▼
    Prompt Engineering
(Style selected by user)
          │
          ▼
 Groq API (Llama 3.3 70B)
          │
          ▼
 AI Generated Summary
          │
          ▼
     Display in UI
```

---

# Tech Stack

- Python
- Groq API
- Gradio
- BeautifulSoup4
- Requests

---

# Project Structure

```text
sitesense/
│
├── app.py                 # Gradio UI
├── scraper.py             # Website scraping
├── summarizer.py          # AI summarization
├── requirements.txt
├── README.md
├── .gitignore
├── .env                   # API Key (not committed)
│
├── assets/
│   ├── demo.gif
│   └── screenshot.png
│
└── venv/
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/esha01/sitesense.git

cd sitesense
```

---

## 2. Create a virtual environment

### macOS / Linux

```bash
python3.11 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure your API Key

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 5. Launch the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:7860
```

---

# Future Improvements

- Summary Length (Short / Medium / Detailed)
- Multi-language summaries
- Export summary as PDF
- Copy Summary button
- Shareable summary links
- Browser extension

---
