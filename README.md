# ai-agent-product-team

## 🧠 Project Configs

This AI agent uses JSON-based project config files stored in the `project_configs/` folder.

A project config tells the agent where to find your project documentation and codebase.

Example config (see `project_configs/example_project.json`):

```json
{
  "project_name": "example-project",
  "description": "An example configuration for a Python web project.",
  "documentation_path": "README.md",
  "code_path": ".",
  "language": "python",
  "frameworks": ["flask", "sqlite", "chart.js"]
}
```

### Usage

```bash
python main.py --project-config project_configs/example_project.json
```
## How to run as a cli tool

### Option 1: Install as a Local CLI Tool (Editable Mode)

#### Step 1: Add setup.py to the root of your project
#### File: setup.py

from setuptools import setup

```
setup(
    name='mydevagent',
    version='0.1',
    py_modules=['main'],
    install_requires=['openai', 'pyyaml'],
    entry_points={
        'console_scripts': [
            'mydevagent = main:main',
        ],
    },
)
```

#### Step 2: Install it as an editable local package

```
pip install --editable .
```

#### Step 3: Now use it like a normal CLI tool

```
mydevagent --list-projects
mydevagent --use-project caffeine-tracker
```

### Option 2: : Create a Shell Wrapper Script (Quick & Dirty)

#### Step 1: Create a shell script somewhere on your PATH
#### File: ~/bin/mydevagent (or wherever you like)

```
#!/bin/bash
python /full/path/to/ai-engineering-agent/main.py "$@"
```

#### Step 2: Make it executable

```
chmod +x ~/bin/mydevagent
```

#### Step 3: Run it like a CLI tool

```
mydevagent --list-projects
```
