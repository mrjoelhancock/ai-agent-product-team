# roles/planner.py

from utils.openai_wrapper import ask_gpt

def plan_tasks(clarified_project_text, config):
    """
    Takes clarified project description and returns a structured work plan in Markdown.
    """
    system_prompt = (
        "You are a technical planner working on a new software project. Based on the clarified project description, "
        "break down the work into actionable tasks grouped by logical phases and components. Each task should be short, concrete, and buildable. "
        "Use Markdown checkboxes. Group by phase (e.g., MVP, v1.1, Future) and optionally by area (e.g., Backend, Frontend)."
    )

    prompt = f"""Clarified Project Description:

\"\"\"{clarified_project_text}\"\"\"

Tech stack includes: {', '.join(config.get("frameworks", []))}.
Language: {config.get("language", 'unspecified')}.

Generate a clean work plan that could be pasted into a `todo.md` or task board.
"""

    return ask_gpt(prompt, system_prompt=system_prompt)