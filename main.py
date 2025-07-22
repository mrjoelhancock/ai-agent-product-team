# main.py

import argparse
import os
import json
import yaml

from roles.clarify import clarify_project
from roles.planner import plan_tasks
from utils.files import save_to_memory, list_projects, load_session, save_session, clear_session
from core.action_manager import perform_action

SESSION_FILE = ".session.json"

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
    parser.add_argument('--project-config', help='Path to project config file')
    parser.add_argument('--list-projects', action='store_true', help='List known project configs')
    parser.add_argument('--use-project', help='Use a named project from project_configs/')
    parser.add_argument('--exit-project', action='store_true', help='Clear the current project session')
    args = parser.parse_args()

    # --exit-project: clear session and exit
    if args.exit_project:
        clear_session()
        print("🧹 Project session cleared.")
        return

    # --list-projects: show known configs and exit
    if args.list_projects:
        projects = list_projects()
        print("\n📁 Available Projects:")
        for name, path in projects:
            print(f"• {name} → {path}")
        return

    # --use-project: resolve and save to session
    if args.use_project:
        projects = list_projects()
        match = next((p for p in projects if p[0] == args.use_project), None)
        if not match:
            print(f"❌ Project '{args.use_project}' not found.")
            return
        args.project_config = match[1]
        save_session(args.project_config)

    # No config explicitly passed: try to load from session
    if not args.project_config:
        session = load_session()
        if session:
            args.project_config = session.get("project_config")

    # Final fallback: if still no project config, fail
    if not args.project_config:
        print("❌ No project selected. Use --use-project <name> or --project-config <path>.")
        return

    # Load selected project config
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

        # Clarify project requirements
        clarified = clarify_project(user_input, config)
        print("\n📝 Clarified Requirements:\n")
        print(clarified)
        print("\n---\n")
        
        # Save it
        save_to_memory(config["project_name"], "clarified_project.md", clarified)
        
        # Plan work from clarified text
        work_plan = plan_tasks(clarified, config)
        print("\n📋 Work Plan:\n")
        print(work_plan)
        
        # Save it too
        save_to_memory(config["project_name"], "work_plan.md", work_plan)

        # Perform a Slack notification action (if configured)
        try:
            perform_action(
                "send_message",
                config,
                tool_name="slack",
                message=f"📣 Project '{config['project_name']}' clarified and planned."
            )
        except Exception as e:
            print(f"⚠️ Slack message failed: {e}")

if __name__ == '__main__':
    main()