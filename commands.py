#!/usr/bin/python3

import discord
import json
from urllib import request
from replacements import replacements
import os

client = discord.Client()
other_commands = json.loads(open('othercommands.json', 'r'))
info = json.loads(open('info.json', 'r'))
perms = json.loads(open('perms.json', 'r'))

def bazaar_load(key):
    output = json.loads(request.urlopen("https://api.hypixel.net/skyblock/bazaar?key={apikey}".format(apikey=key)).read())
    return output

def get_key(val): 
    for key, value in replacements.items(): 
         if val == value.lower(): 
             return key 
    return

class Bot(object):
    global client, other_commands, info, perms

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
        args = get_key(message.content[8:].lower())
        try:
            product = bazaar["products"][args]["quick_status"]
            await message.channel.send('__{item}__\nBuy price: {buy} coins\nSell price: {sell} coins\nMargin: {margin} coins'.format(item=replacements[args], buy=round(product["buyPrice"], 2), sell=round(product["sellPrice"], 2), margin=round(product["buyPrice"]-product["sellPrice"], 2)))
        except KeyError:
            await message.channel.send('Invalid item.')

    async def isplayer(self, message):
        try:
            username = json.loads(request.urlopen('https://api.mojang.com/users/profiles/minecraft/{username}'.format(username=message.content[10:])).read())
            await message.channel.send('{username} is a player.\nhttps://crafatar.com/renders/body/{uuid}?scale=5'.format(username=username['name'],uuid=username['id']))
        except:
            await message.channel.send('{username} is not a player.'.format(username=message.content[9:]))

    async def close(self, message):
        if message.author.name in perms["close"]:
            await client.close()
    
    async def echo(self, message):
        await message.channel.send(message.content[5:])
    
    async def swear(self, message):
        await message.channel.send('>:(')

    #main
    @client.event
    async def on_message(self, message):
        if message.author == client.user:
            return
        
        self.run(message.content)