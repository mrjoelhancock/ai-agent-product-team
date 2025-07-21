# utils/openai_wrapper.py

import os
import openai

# Use environment variable for your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

DEFAULT_MODEL = "gpt-4o"

def ask_gpt(prompt, system_prompt=None, model=DEFAULT_MODEL, temperature=0.4):
    messages = []

    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    messages.append({"role": "user", "content": prompt})

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()

    except openai.error.OpenAIError as e:
        print(f"❌ OpenAI API error: {e}")
        return None