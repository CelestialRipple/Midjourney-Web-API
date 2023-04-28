import requests
import json
import time
import re
import argparse
import sys

class Sender:

    def __init__(self, 
                 params):
        
        self.params = params
        self.sender_initializer()

    def sender_initializer(self):

        with open(self.params, "r") as json_file:
            params = json.load(json_file)

        self.channelid=params['channelid']
        self.authorization=params['authorization']
        self.application_id = params['application_id']
        self.guild_id = params['guild_id']
        self.session_id = params['session_id']
        self.version = params['version']
        self.id = params['id']
        self.flags = params['flags']
        
        
    def send(self, prompt):
        header = {
            'authorization': self.authorization
        }

        payload = {'type': 2, 
        'application_id': self.application_id,
        'guild_id': self.guild_id,
        'channel_id': self.channelid,
        'session_id': self.session_id,
        'data': {
            'version': self.version,
            'id': self.id,
            'name': 'imagine',
            'type': 1,
            'options': [{'type': 3, 'name': 'prompt', 'value': str(prompt) + ' ' + self.flags}],
            'attachments': []}
            }
        
        r = requests.post('https://discord.com/api/v9/interactions', json = payload , headers = header)
        while r.status_code != 204:
            r = requests.post('https://discord.com/api/v9/interactions', json = payload , headers = header)

        print('prompt [{}] successfully sent!'.format(prompt))
