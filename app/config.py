# Configuration settings
APPLICATIONS = [
    {
        "name": "App1",
        "url": "https://yourapp1.com/health/",
        "webhook_url": "https://discord.com/api/webhooks/your-webhook-id-1"
    },
    {
        "name": "App2",
        "url": "https://yourapp2.com/health/",
        "webhook_url": "https://discord.com/api/webhooks/your-webhook-id-2"
    },
    # Add more applications as needed
]

# Default webhook URL if none is specified for an application
DEFAULT_WEBHOOK_URL = "https://discord.com/api/webhooks/default-webhook-id"

CHECK_INTERVAL = 300  # Check interval in seconds (e.g., 300 seconds = 5 minutes