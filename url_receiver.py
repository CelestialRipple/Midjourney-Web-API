import requests
import json
import time
import pandas as pd
import os
import re
from datetime import datetime

class Receiver:

    def __init__(self, params, index):
        
        self.params = params
        self.index = index
        self.sender_initializer()

        self.df = pd.DataFrame(columns = ['prompt', 'url', 'filename', 'is_downloaded'])

    
    def sender_initializer(self):

        with open(self.params, "r") as json_file:
            params = json.load(json_file)

        self.channelid=params['channelid'][self.index]
        self.authorization=params['authorization']
        self.headers = {'authorization' : self.authorization}

    def retrieve_messages(self):
        r = requests.get(
            f'https://discord.com/api/v10/channels/{self.channelid}/messages?limit={100}', headers=self.headers)
        jsonn = json.loads(r.text)
        return jsonn


    def collecting_results(self):
        message_list  = self.retrieve_messages()
        self.awaiting_list = pd.DataFrame(columns = ['prompt', 'status'])
        for message in message_list:

            if (message['author']['username'] == 'Midjourney Bot') and ('**' in message['content']):
                
                if len(message['attachments']) > 0:

                    if (message['attachments'][0]['filename'][-4:] == '.png') or ('(Open on website for full quality)' in message['content']):
                        id = message['id']
                        prompt = message['content'].split('**')[1].split(' --')[0]
                        url = message['attachments'][0]['url']
                        filename = message['attachments'][0]['filename']
                        if id not in self.df.index:
                            self.df.loc[id] = [prompt, url, filename, 0]

                    else:
                        id = message['id']
                        prompt = message['content'].split('**')[1].split(' --')[0]
                        if ('(fast)' in message['content']) or ('(relaxed)' in message['content']):
                            try:
                                status = re.findall("(\w*%)", message['content'])[0]
                            except:
                                status = 'unknown status'
                        self.awaiting_list.loc[id] = [prompt, status]

                else:
                    id = message['id']
                    prompt = message['content'].split('**')[1].split(' --')[0]
                    if '(Waiting to start)' in message['content']:
                        status = 'Waiting to start'
                    self.awaiting_list.loc[id] = [prompt, status]
                   
