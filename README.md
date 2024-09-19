
# Pynitor

Pynitor is a simple Python application to monitor the health of multiple applications and send notifications to a Discord channel if any of them become unhealthy. It supports specifying individual webhooks for each application to allow for targeted notifications.

## Installation

First, clone the repository and navigate into the directory:

```bash
git clone https://github.com/na0495/pynitor.git
cd pynitor
```

Then, install the package:

```bash
pip install .
```

## Usage

After installation, you can run the monitor using the command:

```bash
pynitor
```

## Configuration

The configuration is defined in `app/config.py`. This file contains a list of applications to monitor, along with their health check URLs and optional webhook URLs for notifications. Here's a breakdown of the configuration options:

- **`APPLICATIONS`**: A list of dictionaries where each dictionary represents an application to monitor. Each dictionary can have:
  - `name`: A name for the application (used in notifications).
  - `url`: The health check URL for the application.
  - `webhook_url` (optional): The Discord webhook URL for notifications specific to this application.

- **`DEFAULT_WEBHOOK_URL`**: The default webhook URL to use if an application doesn't specify its own webhook.

- **`CHECK_INTERVAL`**: How often (in seconds) to check the health of the applications.

### Example Configuration

In `app/config.py`, you can define your applications like this:

```python
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

CHECK_INTERVAL = 300  # Check interval in seconds (e.g., 300 seconds = 5 minutes)
```

## Adding Applications

To monitor more applications, simply add them to the `APPLICATIONS` list in `app/config.py`. Each application can have its own `webhook_url`. If no `webhook_url` is provided, the `DEFAULT_WEBHOOK_URL` will be used.

## Deployment

- **Running Periodically**: To run `pynitor` periodically, you can set up a cron job (Linux/macOS) or use Task Scheduler (Windows). For example, to run the script every 5 minutes, add this to your crontab:
    ```bash
    */5 * * * * /path/to/python /path/to/pynitor
    ```
    Replace `/path/to/python` with the path to the Python executable and `/path/to/pynitor` with the path to the `pynitor` command.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

If you want to contribute to this project, feel free to create a pull request or open an issue in the GitHub repository.

## Author

Saad Mrabet  
Email: saad.mrabet@kubicbits.com
