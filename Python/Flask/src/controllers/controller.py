import requests
import json
import boto3
import time
from datetime import datetime

class AdapterController:
    def __init__ (self,config):
        self.config = config
        self.bot_engine_config = self.config.get("bot_engine")

    def send_message(self,incoming_message):
        try:
            bot_message_request = incoming_message
            print(bot_message_request)
            if bot_message_request is not None:
                response = requests.post(
                    self.bot_engine_config["endpoint"] +
                    self.bot_engine_config["paths"]["messages"],
                    json=bot_message_request,
                    timeout=self.config.get("requests_timeout"))
                status_code = response.status_code
            if status_code != 200:
                return response.text,status_code
            return bot_message_request['chatter'],bot_message_request['message_id'],response.text,status_code

        except Exception as msg:            
            return msg

    def decode_engine_message(self,message):
        chatter = message['chatter']
        message_id = message['message_id']
        message = message['messages'][0]['message']

        return chatter,message_id,message

    def put_log(self,chatter, message_id, message, dynamodb = None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb',region_name = 'us-east-1')
        table = dynamodb.Table('aw000-TabotXVoz-dev-dynamo')
        response = table.put_item(
            Item={
                'chatter':chatter,
                'message_id': message_id,
                'message': message,
                'timestamp' : str(datetime.now().time())
            }
        )
        return response

    def get_log(self,chatter, message_id, dynamodb = None):
        if not dynamodb:
            dynamodb = boto3.resource('dynamodb',region_name = 'us-east-1')
        table = dynamodb.Table('aw000-TabotXVoz-dev-dynamo')
        attempts  = 0
        while attempts < 5:
            try:
                response = table.get_item(
                    Key={
                        'chatter':chatter,
                        'message_id': message_id
                    }
                )
                return {'body' : response['Item']['message']}
            except:
                attempts += 1
                time.sleep(2)
        return {'body' : "No tengo una respuesta para ti"}
