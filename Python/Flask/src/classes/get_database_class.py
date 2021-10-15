
class DatabaseManagement():
    """Manager mock database connection"""

    def __init__(self,db_endpoint):
        self.db_endpoint = db_endpoint
        try:
            print("Connected to database: {}".format(self.db_endpoint))
        except Exception as error:
            print(error)
    
    def get_data(self, config):
        """
        Get the message from config file

        :param config: json with the application configuration
        :return: dict with the info to response the user
        """
        return config.get("message")
