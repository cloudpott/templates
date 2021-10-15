from datetime import datetime

def main(config):
    """
    Principal function to get health.

    :param config: json with the application configuration
    :return: dict with status
    """
    app_name = config.get("app_name")
    return {
        "app_name": app_name,
        "statusCode": 200,
        "message": "ALIVE",
        "timestamp": str(datetime.now())
    }
