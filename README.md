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