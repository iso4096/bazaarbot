#!/usr/bin/python3

import discord
import json
from urllib import request
import os

client = discord.Client()

class Bot(object):
    global client

    def __init__(self, apikey):
        self.prefix = '$'
        self.apikey = apikey
    
    def list_in_str(self, a, b):
        for entry in a:
            if entry in b:
                return True
        return False

    async def cmd(self, message):
        args = message.content

        #https://data-flair.training/blogs/python-switch-case/

        if not (args.startswith('$')) and self.list_in_str(open('swearfilter.txt', 'r').split('\n'), args):
            return
        elif self.list_in_str(open('swearfilter.txt', 'r').split('\n'), args):
            return self.swear(message)
        else:
            method_name = args.split(' ')[0]
            method = getattr(self, method_name, lambda:'c\'mon mate this isn\'t a command')
            return method(message)

    def help(self, message):
        pass

    async def swear(self, message):
        await message.channel.send('>:(')

    #main
    @client.event
    async def on_message(self, message):
        if message.author == client.user:
            return
        
        self.cmd(message)