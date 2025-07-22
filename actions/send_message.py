# actions/send_message.py

from tools import slack

TOOL_MAP = {
    "slack": slack.send_message,
}

def send_message(config, tool_name, message):
    """
    Performs a send_message action using the given tool.
    """
    tool_config = config.get("tools", {}).get(tool_name)
    if not tool_config or "adapter" not in tool_config:
        raise ValueError(f"Tool '{tool_name}' not properly configured in project config.")
    
    adapter_config = tool_config["adapter"]

    if tool_name not in TOOL_MAP:
        raise ValueError(f"Unsupported tool '{tool_name}'")

    # Call the tool's function
    return TOOL_MAP[tool_name](adapter_config, message)