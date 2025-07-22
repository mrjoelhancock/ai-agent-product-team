# core/action_manager.py

from actions import send_message

# Map action names to handler functions
ACTION_HANDLERS = {
    "send_message": send_message.send_message,
    # Later: "deploy": deploy.deploy_to_platform,
    # Later: "open_pr": pull_requests.open_pull_request,
}

def perform_action(action_name, config, **kwargs):
    """
    Perform an action using project-specific configuration.
    kwargs are passed to the action handler (e.g. tool_name, message).
    """
    if action_name not in ACTION_HANDLERS:
        raise ValueError(f"Unsupported action: {action_name}")

    handler = ACTION_HANDLERS[action_name]
    return handler(config, **kwargs)