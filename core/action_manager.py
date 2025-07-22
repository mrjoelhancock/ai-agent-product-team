# core/action_manager.py

from actions import send_message  # Import individual actions here
from tools import slack, telegram

ACTION_HANDLERS = {
    "send_message": send_message.send_message,
    # "deploy": deploy.run_deploy,
    # "open_pr": pr.open_pull_request,
}

def perform_action(action_name, config, **kwargs):
    """
    Perform a named action using the current project config.
    Validates tool, adapter, and dispatches to the correct action.
    """
    if action_name not in ACTION_HANDLERS:
        raise ValueError(f"Unsupported action: {action_name}")
    
    handler = ACTION_HANDLERS[action_name]
    return handler(config, **kwargs)