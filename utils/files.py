# utils/files.py

import os
import json

def save_to_memory(project_name, filename, content, memory_root="project_memory"):
    """
    Saves content to a file inside project_memory/<project_name>/<filename>
    """
    dir_path = os.path.join(memory_root, project_name)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, filename)

    try:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"💾 Saved to {file_path}")
    except Exception as e:
        print(f"❌ Error saving to memory: {e}")
        
def list_projects(config_root="project_configs"):
    """
    Returns a list of project names and their config paths.
    """
    projects = []
    for root, dirs, files in os.walk(config_root):
        for file in files:
            if file == "project_config.json":
                path = os.path.join(root, file)
                try:
                    with open(path, 'r') as f:
                        config = json.load(f)
                        name = config.get("project_name") or os.path.basename(root)
                        projects.append((name, path))
                except Exception:
                    continue
    return projects