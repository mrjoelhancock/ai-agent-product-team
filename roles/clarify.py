# roles/clarify.py

import os
from utils.openai_wrapper import ask_gpt

def load_documentation(doc_path):
    if not os.path.exists(doc_path):
        return None
    try:
        with open(doc_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading documentation: {e}")
        return None

def clarify_requirements(user_input, config):
    doc_path = os.path.join(config.get("code_path", "."), config.get("documentation_path", "README.md"))
    documentation = load_documentation(doc_path)

    system_prompt = (
        "You are a software business analyst helping an engineer clarify and structure a new software feature or project. "
        "Given the user's idea and any available documentation, ask smart questions to resolve ambiguity, identify missing pieces, "
        "and return a structured, clarified requirements list in plain text or markdown format."
    )

    prompt = f"""The user has submitted the following idea for a feature or project:

\"\"\"{user_input}\"\"\"

{"Here is some existing project documentation:\n\n" + documentation if documentation else "No documentation is available."}

Please help clarify and structure the requirements. If anything is vague or incomplete, flag it and suggest questions to ask.
"""

    return ask_gpt(prompt, system_prompt=system_prompt)