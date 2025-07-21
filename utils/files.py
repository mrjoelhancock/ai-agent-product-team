# utils/files.py

import os

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