from groq import Groq
from dotenv import load_dotenv
import os

from scraper import fetch_website_contents

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_prompt = """
You analyze the contents of websites.

Write a concise summary.

Ignore advertisements, menus, navigation bars and repeated content.

Respond in Markdown.
"""

def summarize(url):
    website = fetch_website_contents(url)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Summarize this website:\n\n{website}"}
        ],
    )

    return response.choices[0].message.content