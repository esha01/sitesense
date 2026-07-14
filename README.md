# 🔎 AI Website Summarizer

An AI-powered web application that summarizes the content of any website using **Groq's Llama 3.3 70B** model.

---

## Demo

![Demo](assets/demo.gif)

---

## Features

- 🌐 Summarize any website from its URL
- 🤖 AI-generated summaries using Groq LLM
- 📰 Removes navigation menus and unnecessary page content
- ⚡ Fast Gradio interface
- 📄 Markdown formatted summaries

---

## Tech Stack

- Python
- Gradio
- Groq API
- BeautifulSoup4
- Requests
- Python-dotenv

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Website-Summarizer.git

cd AI-Website-Summarizer
```

Create a virtual environment

```bash
python3.11 -m venv venv
```

Activate it

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

Run the app

```bash
python app.py
```

---

## Project Structure

```
AI-Website-Summarizer/
│
├── app.py
├── scraper.py
├── summarizer.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── assets/
```

---

## Future Improvements

- Multiple summary styles
- Bullet point summaries
- Download summary as PDF
- Multiple language support
- Browser extension
- Deploy on Hugging Face Spaces

---
