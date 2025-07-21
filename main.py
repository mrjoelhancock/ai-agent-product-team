# main.py

import argparse
import os
import json
import yaml
from utils.openai_wrapper import ask_gpt
from roles.clarify import clarify_project
from roles.planner import plan_tasks
from utils.files import save_to_memory

def load_project_config(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    
    with open(path, 'r') as f:
        if path.endswith('.json'):
            return json.load(f)
        elif path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        else:
            raise ValueError("Unsupported config format. Use .json or .yaml")

def main():
    parser = argparse.ArgumentParser(description="AI Engineering Assistant")
    parser.add_argument('--project-config', required=True, help='Path to project config file')
    args = parser.parse_args()

    try:
        config = load_project_config(args.project_config)
    except Exception as e:
        print(f"Error loading project config: {e}")
        return

    print(f"\n🔧 Loaded project: {config.get('project_name', 'Unnamed')}")
    print(f"📄 Documentation: {config.get('documentation_path', 'N/A')}")
    print("🤖 Agent is ready. Type your project idea or 'exit' to quit.\n")

    while True:
        user_input = input("> ")
        if user_input.lower() in ['exit', 'quit']:
            break

        clarified = clarify_project(user_input, config)
        print("\n📝 Clarified Requirements:\n")
        print(clarified)
        print("\n---\n")
        
        save_to_memory(config["project_name"], "clarified_project.md", clarified)

if __name__ == '__main__':
    main()