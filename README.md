# ai-agent-product-team

Prototype for an agent which can carry out software development tasks with some level of autonomy.

Works against "Jobs" to achieve outcomes.

Carries out "Actions" using "Tools" that help it do things via the Internet.

Tools are configured for use in Projects via "Adapters". Adapters are the configurations that allow use in a project context.

```
Job = Write Python script to print a random number. Commit the script to code repo X. Email Y when done.
```

Agent uses LLM to determine tasks required to achieve Job. Create a plan for working on the job.

```
Job Tasks
- Write Python script which prints a random number.
- Create new branch for script in code repo C.
- Commit the script to code repo C.
- Componse subject and body for email to send to Y.
- Send email to Y with content from previous task.
```

Job Tasks
```
Job Task => (performed by) Action => (with) Tool => (configured for use in Project via) Adapter
```

Agent planning

```
1. To carry out this task, what is the best Action?
2. To perform this Action, what is the best Tool?
3. Ensure the tool is correctly configured for the Project.
``

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
