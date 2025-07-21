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

def clarify_project(user_input, config):
    """
    Clarifies the high-level project goal, purpose, and outcomes.
    Suitable for the start of a project.
    """
    doc_path = os.path.join(config.get("code_path", "."), config.get("documentation_path", "README.md"))
    documentation = load_documentation(doc_path)

    system_prompt = (
        "You are a product strategist and service designer. Your job is to help clarify a new software project idea. "
        "You analyze the user's idea and produce a structured breakdown including:\n\n"
        "- Problem being solved\n"
        "- Who the users are (personas)\n"
        "- Goals or outcomes the users want\n"
        "- Potential features (even rough or speculative)\n"
        "- Any open questions or assumptions to clarify\n"
    )

    prompt = f"""The user has submitted the following idea for a software project:

\"\"\"{user_input}\"\"\"

{"Here is some existing project documentation:\n\n" + documentation if documentation else "No documentation is available."}

Please analyze and clarify this project idea in a structured format.
"""

    return ask_gpt(prompt, system_prompt=system_prompt)

def clarify_feature(feature_text, config):
    """
    (Stub) Will later clarify the structure, flow, and boundaries of a specific feature.
    """
    system_prompt = (
        "You are a software business analyst. Given a specific feature, clarify its scope, inputs, user flow, "
        "and any data or system interactions involved. Identify edge cases or questions."
    )

    prompt = f"""Clarify the following feature for implementation planning:

\"\"\"{feature_text}\"\"\"

Assume the stack includes: {', '.join(config.get('frameworks', []))}.
"""

    return ask_gpt(prompt, system_prompt=system_prompt)

def clarify_task(task_description, config):
    """
    (Stub) Will later clarify a specific technical task to define expected logic, files, and tests.
    """
    system_prompt = (
        "You are a software engineer preparing to implement a specific technical task. "
        "Given the task description, break down what should be done, what files or modules are involved, "
        "and what tests should be included."
    )

    prompt = f"""Clarify the implementation of this task:

\"\"\"{task_description}\"\"\"

Base language: {config.get('language', 'unspecified')}. Frameworks: {', '.join(config.get('frameworks', []))}.
"""

    return ask_gpt(prompt, system_prompt=system_prompt)