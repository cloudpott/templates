from src.controllers import health_controller, get_sample_controller
from flask import Flask,request
import logging
import json

def create_app(config):
    """
    Handle requests

    :param config: json with the application configuration
    :return: flask applicaion
    """
    with open(config) as json_file:
        config = json.load(json_file)
    
    flaskname = config.get("app_name")
    application = Flask(flaskname)

    @application.route('/',methods=['GET'])
    def health_check():
        return  {
                    "detail":"Working"
                }
    
    @application.route('/health',methods=['GET'])
    def health_status():
        return health_controller.main(config)

    @application.route('/get_sample', methods = ['GET'])
    def get_sample():
        username = request.args.get("username")
        if username == None:
            return{"detail":"username parameter missing"},400
        return get_sample_controller.main(config, username)

    return application
