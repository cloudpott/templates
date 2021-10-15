from src.models import get_sample_model

def main(config, username):
    """
    Principal function to copntroller get_sample.

    :param config: json with the application configuration
    :param username: username given by the user at request
    :return: dict with the info to response the user
    """

    result = get_sample_model.get_response(config,username)
    if result[0]:
        return result[1]
    else:
        return {
            "statusCode": 200,
            "detail": "Sorry, I can`t give you more information. Try again later"
            }