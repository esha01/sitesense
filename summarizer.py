from groq import Groq
from dotenv import load_dotenv
import os

from scraper import fetch_website_contents

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

STYLE_PROMPTS = {
    "Friendly 😊": "Write a friendly, conversational summary in 5–7 sentences.",
    "Professional 💼": "Write a concise executive summary with a professional tone.",
    "Bullet Points 📋": "Summarize the content as clear, concise bullet points.",
    "Explain Like I'm 5 🧒": "Explain the content in very simple language that a 5-year-old can understand."
}


def summarize(url, style):

    website = fetch_website_contents(url)

    system_prompt = f"""
    You analyze the contents of websites.

    Ignore advertisements, navigation menus and repeated content.

    Generate the summary in this style:

    {STYLE_PROMPTS[style]}

    Respond in Markdown.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"Summarize this website:\n\n{website}"
            }
        ],
    )

    return response.choices[0].message.content