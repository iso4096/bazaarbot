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
    game = discord.Game("version 1.0.1")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    await bot.handle(message)

if __name__ == "__main__":
    assert info["discord_token"] != "00000000000000000000000000000000000000000000000000000000000"
    assert info["hypixel_api_key"] != "00000000-0000-0000-0000-000000000000"
    client.run(info["discord_token"])