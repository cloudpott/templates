from src.classes import get_database_class
import random

def get_response(config, username):
    """
    Here you must get all the needed data to response the user

    :param config: json with the application configuration
    :param username: username given by the user at request
    :return: dict with the info to response the user
    """

    #Simulate getting data from a database
    response = []
    db_endpoint = config.get("db_endpoint")
    db_connection = get_database_class.DatabaseManagement(db_endpoint)
    r_choice = random.choice([True,False])
    response.append(r_choice)
    
    message = db_connection.get_data(config)
    message["method"] = "get"
    message["username"] = username
    response.append(message)
    
    return response
    
