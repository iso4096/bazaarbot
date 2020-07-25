#!/usr/bin/python3

import discord
import json
from urllib import request
from replacements import replacements
import os

client = discord.Client()
other_commands = json.loads(open('othercommands.json', 'r'))
info = json.loads(open('info.json', 'r'))

def bazaar_load(key):
    output = json.loads(request.urlopen("https://api.hypixel.net/skyblock/bazaar?key={apikey}".format(apikey=key)).read())
    return output

class Bot(object):
    global client, other_commands, info

    def __init__(self, apikey):
        self.prefix = '$'
        self.apikey = apikey

    
    def list_in_str(self, a, b):
        for entry in a:
            if entry in b:
                return True
        return False

    async def run(self, message):
        args = message.content

        #https://data-flair.training/blogs/python-switch-case/

        if not (args.startswith('$')) and self.list_in_str(open('swearfilter.txt', 'r').split('\n'), args):
            return
        elif self.list_in_str(open('swearfilter.txt', 'r').split('\n'), args):
            return self.swear(message)
        else:
            method_name = args.split(' ')[0][1:]
            method = getattr(self, method_name, lambda:'c\'mon mate this isn\'t a command')
            return method(message)

    async def help(self, message):
        await message.channel.send("not implemented because i'm too lazy")
    
    async def bazaar(self, message):
        bazaar = bazaar_load(info["hypixel_api_key"])


    async def swear(self, message):
        await message.channel.send('>:(')

    #main
    @client.event
    async def on_message(self, message):
        if message.author == client.user:
            return
        
        self.run(cmd)