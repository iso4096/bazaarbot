#!/usr/bin/python3

import discord
import json
from urllib import request
from replacements import replacements
import os
import matplotlib.pyplot as plt
import numpy as np

client = discord.Client()
other_commands = json.loads(open('othercommands.json', 'r').read())
info = json.loads(open('info.json', 'r').read())
perms = json.loads(open('perms.json', 'r').read())

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

    def __init__(self):
        self.prefix = '$'
        #until i set up the prefix system, i'm not gonna revise this
    
    def list_in_str(self, a, b):
        for entry in a:
            if entry in b:
                return True
        return False

    async def run(self, message):
        args = message.content

        #https://data-flair.training/blogs/python-switch-case/
        if not (args.startswith(self.prefix)) and self.list_in_str(open('swearfilter.txt', 'r').read().split('\n'), args) and self.list_in_str(other_commands["matches_exactly"].keys(), args):
            await None
        elif self.list_in_str(open('swearfilter.txt', 'r').read().split('\n'), args):
            await self.swear(message)
        elif self.list_in_str(other_commands["matches_exactly"].keys(), args):
            await message.channel.send(other_commands["matches_exactly"][args])
        elif args.startswith(self.prefix):
            method_name = args.split(' ')[0][len(self.prefix):]
            await getattr(self, method_name, lambda _: message.channel.send('c\'mon mate this isn\'t a command'))(message)

    async def help(self, message):
        await message.channel.send("not implemented because i'm too lazy")
    
    async def bazaar(self, message):
        args = get_key(message.content[len(self.prefix)+7:].lower())
#        print(args)
#        print(key)
        bazaar = bazaar_load(info["hypixel_api_key"])
        try:
            product = bazaar["products"][args]
            buyprices = [product["buy_summary"][0]["pricePerUnit"], product["buy_summary"][-1]["pricePerUnit"]]
            sellprices = [product["sell_summary"][0]["pricePerUnit"], product["sell_summary"][-1]["pricePerUnit"]]
            buytext = ""
            selltext = ""
            buypercentage = (buyprices[1]-buyprices[0])/buyprices[1]
            sellpercentage = (sellprices[1]-sellprices[0])/sellprices[1]
            if buypercentage >= 0:
                buytext = "+ Buy price: {buyprice} coins (+{buypercentage}%)".format(buyprice=buyprices[0], buypercentage=round(buypercentage*100, 2))
            else:
                buytext = "- Buy price: {buyprice} coins ({buypercentage}%)".format(buyprice=buyprices[0], buypercentage=round(buypercentage*100, 2))
            if sellpercentage >= 0:
                selltext = "+ Sell price: {sellprice} coins (+{sellpercentage}%)".format(sellprice=sellprices[0], sellpercentage=round(sellpercentage*100, 2))
            else:
                selltext = "- Sell price: {sellprice} coins ({sellpercentage}%)".format(sellprice=sellprices[0], sellpercentage=round(sellpercentage*100, 2))
            await message.channel.send('```diff\n{item}\n{buytext}\n{selltext}\nMargin: {margin} coins```'.format(item=replacements[args], buytext=buytext, selltext=selltext, margin=round(buyprices[0]-sellprices[0], 1)))
        except KeyError:
            await message.channel.send('Invalid item.')

    async def isplayer(self, message):
        try:
            username = json.loads(request.urlopen('https://api.mojang.com/users/profiles/minecraft/{username}'.format(username=message.content[10:])).read())
            await message.channel.send('{username} is a player.\nhttps://crafatar.com/renders/body/{uuid}?scale=5'.format(username=username['name'],uuid=username['id']))
        except:
            await message.channel.send('{username} is not a player.'.format(username=message.content[9:]))

    async def close(self, message):
        if message.author.name in perms["$close"]:
            await client.close()
    
    async def echo(self, message):
        await message.channel.send(message.content[len(self.prefix)+5:])
    
    async def swear(self, message):
        await message.channel.send('>:(')
    
    async def trend(self, message):
        args = get_key(message.content[len(self.prefix)+6:].lower())
        bazaar = bazaar_load(info["hypixel_api_key"])
        try:
            product = bazaar["products"][args]
            buyprices = [product["buy_summary"][i]["pricePerUnit"] for i in range(len(product["buy_summary"]))]
            sellprices = [product["sell_summary"][i]["pricePerUnit"] for i in range(len(product["sell_summary"]))]
            plt.title("Buy prices")
            plt.xlabel("Order no.")
            plt.ylabel("Buy price")
            plt.plot(range(len(product["buy_summary"])), buyprices, "b-")
            plt.savefig("figure.png")
            f = discord.File("./figure.png", filename="figure.png")
            embed = discord.Embed()
            embed.set_image(url="attachment://figure.png")
            await message.channel.send(file=f, embed=embed)
            plt.clf()
            plt.title("Sell prices")
            plt.xlabel("Order no.")
            plt.ylabel("Sell price")
            plt.plot(range(len(product["sell_summary"])), sellprices, "b-")
            plt.savefig("figure.png")
            f = discord.File("./figure.png", filename="figure.png")
            embed = discord.Embed()
            embed.set_image(url="attachment://figure.png")
            plt.clf()
            await message.channel.send(file=f, embed=embed)
        except KeyError:
            await message.channel.send('Invalid item.')

    #main
    async def handle(self, message):
        if message.author == client.user:
            return
        
        await self.run(message)