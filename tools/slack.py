# tools/slack.py
# Supports "send_message" actions.

import requests

def send_message(adapter_config, message):
    """
    Sends a message to Slack using an incoming webhook.
    adapter_config must include 'webhook_url'.
    """
    webhook_url = adapter_config.get("webhook_url")
    if not webhook_url:
        raise ValueError("Slack adapter missing 'webhook_url'")
    
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)

    if response.status_code != 200:
        raise Exception(f"Slack message failed: {response.status_code} {response.text}")
    
    return True