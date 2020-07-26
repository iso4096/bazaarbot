#!/usr/bin/python3

import discord
import json
from urllib import request
from replacements import replacements
import os
import matplotlib.pyplot as plt
import numpy as np

from commands import Bot, info, client

bot = Bot()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    game = discord.Game("being developed")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    bot.handle(message)

client.run(info["discord_token"])