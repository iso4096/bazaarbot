#!/usr/bin/python3.6 version 3.6

import discord
import json
from urllib import request
import os

client = discord.Client()
key = '00000000-0000-0000-0000-000000000000' #your api key here

#https://hypixel.net/threads/api-bazaar-item-names-to-in-game-bazaar-item-json.2845357/
replacements = {"BROWN_MUSHROOM": "Brown Mushroom","INK_SACK:3": "Cocoa Beans","INK_SACK:4": "Lapis Lazuli","TARANTULA_WEB": "Tarantula Web","CARROT_ITEM": "Carrot","ENCHANTED_POTATO": "Enchanted Potato","ENCHANTED_SLIME_BALL": "Enchanted Slimeball","ENCHANTED_RED_MUSHROOM": "Enchanted Red Mushroom","ENCHANTED_GOLDEN_CARROT": "Enchanted Golden Carrot","ENCHANTED_RABBIT_HIDE": "Enchanted Rabbit Hide","ENCHANTED_BIRCH_LOG": "Enchanted Birch Wood","ENCHANTED_GUNPOWDER": "Enchanted Gunpowder","ENCHANTED_MELON": "Enchanted Melon","ENCHANTED_SUGAR": "Enchanted Sugar","CACTUS": "Cactus","ENCHANTED_BLAZE_ROD": "Enchanted Blaze Rod","ENCHANTED_CAKE": "Enchanted Cake","PUMPKIN": "Pumpkin","ENCHANTED_BROWN_MUSHROOM": "Enchanted Brown Mushroom","WHEAT": "Wheat","ENCHANTED_RAW_SALMON": "Enchanted Raw Salmon","ENCHANTED_GLISTERING_MELON": "Enchanted Glistering Melon","PRISMARINE_SHARD": "Prismarine Shard","PROTECTOR_FRAGMENT": "Protector Dragon Fragment","ENCHANTED_EMERALD": "Enchanted Emerald","ENCHANTED_SPIDER_EYE": "Enchanted Spider Eye","RED_MUSHROOM": "Red Mushroom","MUTTON": "Mutton","ENCHANTED_MELON_BLOCK": "Enchanted Melon Block","DIAMOND": "Diamond","WISE_FRAGMENT": "Wise Dragon Fragment","COBBLESTONE": "Cobblestone","SPIDER_EYE": "Spider Eye","RAW_FISH": "Raw Fish","ENCHANTED_PUFFERFISH": "Enchanted Pufferfish","POTATO_ITEM": "Potato","ENCHANTED_HUGE_MUSHROOM_1": "Enchanted Brown Mushroom Block","ENCHANTED_COBBLESTONE": "Enchanted Cobblestone","ENCHANTED_HUGE_MUSHROOM_2": "Enchanted Red Mushroom Block","ICE_BAIT": "Ice Bait","PORK": "Raw Porkchop","PRISMARINE_CRYSTALS": "Prismarine Crystals","ICE": "Ice","HUGE_MUSHROOM_1": "Brown Mushroom Block","HUGE_MUSHROOM_2": "Red Mushroom Block","LOG_2:1": "Dark Oak Wood","ENCHANTED_SNOW_BLOCK": "Enchanted Snow Block","GOLDEN_TOOTH": "Golden Tooth","STRING": "String","RABBIT_FOOT": "Rabbit's Foot","REDSTONE": "Redstone","ENCHANTED_CACTUS_GREEN": "Enchanted Cactus Green","ENCHANTED_CARROT_ON_A_STICK": "Was Temporarily: Enchanted Carrot on a Stick","ENCHANTED_LAPIS_LAZULI_BLOCK": "Enchanted Lapis Block","ENCHANTED_ENDSTONE": "Enchanted End Stone","ENCHANTED_COOKIE": "Enchanted Cookie","ENCHANTED_SAND": "Enchanted Sand","ENCHANTED_STRING": "Enchanted String","STRONG_FRAGMENT": "Strong Dragon Fragment","SLIME_BALL": "Slimeball","SNOW_BALL": "Snowball","HOLY_FRAGMENT": "Holy Dragon Fragment","ENCHANTED_ACACIA_LOG": "Enchanted Acacia Wood","ENCHANTED_EGG": "Enchanted Egg","SAND": "Sand","RAW_CHICKEN": "Raw Chicken","ENCHANTED_LAPIS_LAZULI": "Enchanted Lapis Lazuli","ENCHANTED_GHAST_TEAR": "Enchanted Ghast Tear","ENCHANTED_COCOA": "Enchanted Cocoa Bean","CARROT_BAIT": "Carrot Bait","SEEDS": "Seeds","ENCHANTED_LEATHER": "Enchanted Leather","ENCHANTED_SPONGE": "Enchanted Sponge","HAY_BLOCK": "Hay Bale","FLINT": "Flint","INK_SACK": "Ink Sack","ENCHANTED_ROTTEN_FLESH": "Enchanted Rotten Flesh","WOLF_TOOTH": "Wolf Tooth","ENCHANTED_SPRUCE_LOG": "Enchanted Spruce Wood","ENCHANTED_GRILLED_PORK": "Enchanted Grilled Pork","ENCHANTED_NETHER_STALK": "Enchanted Nether Wart","ENCHANTED_REDSTONE_BLOCK": "Enchanted Redstone Block","ENCHANTED_QUARTZ_BLOCK": "Enchanted Quartz Block","GREEN_CANDY": "Green Candy","ENCHANTED_REDSTONE": "Enchanted Redstone","ENCHANTED_REDSTONE_LAMP": "Enchanted Redstone Lamp","GRAVEL": "Gravel","MELON": "Melon","ENCHANTED_LAVA_BUCKET": "Enchanted Lava Bucket","ENCHANTED_PACKED_ICE": "Enchanted Packed Ice","RAW_FISH:3": "Pufferfish","ENCHANTED_PRISMARINE_SHARD": "Enchanted Prismarine Shard","ENCHANTED_IRON_BLOCK": "Enchanted Iron Block","BONE": "Bone","RAW_FISH:2": "Clownfish","RAW_FISH:1": "Raw Salmon","REVENANT_FLESH": "Revenant Flesh","ENCHANTED_GLOWSTONE": "Enchanted Glowstone","ENCHANTED_PORK": "Enchanted Pork","FEATHER": "Feather","NETHERRACK": "Netherrack","WHALE_BAIT": "Whale Bait","SPONGE": "Sponge","BLAZE_ROD": "Blaze Rod","ENCHANTED_DARK_OAK_LOG": "Enchanted Dark Oak Wood","YOUNG_FRAGMENT": "Young Dragon Fragment","ENCHANTED_CLOWNFISH": "Enchanted Clownfish","ENCHANTED_GOLD": "Enchanted Gold","ENCHANTED_RAW_CHICKEN": "Enchanted Raw Chicken","ENCHANTED_WATER_LILY": "Enchanted Lily Pad","LOG:1": "Spruce Wood","CATALYST": "Catalyst","LOG:3": "Jungle Wood","LOG:2": "Birch Wood","BLESSED_BAIT": "Blessed Bait","ENCHANTED_GLOWSTONE_DUST": "Enchanted Glowstone Dust","ENCHANTED_INK_SACK": "Enchanted Ink Sack","ENCHANTED_CACTUS": "Enchanted Cactus","ENCHANTED_SUGAR_CANE": "Enchanted Sugar Cane","ENCHANTED_COOKED_SALMON": "Enchanted Cooked Salmon","ENCHANTED_SEEDS": "Enchanted Seeds","LOG": "Oak Wood","GHAST_TEAR": "Ghast Tear","UNSTABLE_FRAGMENT": "Unstable Dragon Fragment","ENCHANTED_ENDER_PEARL": "Enchanted Ender Pearl","PURPLE_CANDY": "Purple Candy","ENCHANTED_FERMENTED_SPIDER_EYE": "Enchanted Fermented Spider Eye","SPIKED_BAIT": "Spiked Bait","ENCHANTED_GOLD_BLOCK": "Enchanted Gold Block","ENCHANTED_JUNGLE_LOG": "Enchanted Jungle Wood","ENCHANTED_FLINT": "Enchanted Flint","IRON_INGOT": "Iron Ingot","ENCHANTED_EMERALD_BLOCK": "Enchanted Emerald Block","ENCHANTED_CLAY_BALL": "Enchanted Clay","GLOWSTONE_DUST": "Glowstone Dust","GOLD_INGOT": "Gold Ingot","REVENANT_VISCERA": "Revenant Viscera","TARANTULA_SILK": "Tarantula Silk","ENCHANTED_MUTTON": "Enchanted Mutton","SUPER_COMPACTOR_3000": "Super Compactor 3000","SUPER_EGG": "Super Enchanted Egg","ENCHANTED_IRON": "Enchanted Iron","STOCK_OF_STONKS": "Stock of Stonks","ENCHANTED_HAY_BLOCK": "Enchanted Hay Bale","ENCHANTED_PAPER": "Enchanted Paper","ENCHANTED_BONE": "Enchanted Bone","ENCHANTED_DIAMOND_BLOCK": "Enchanted Diamond Block","SPOOKY_BAIT": "Spooky Bait","SUPERIOR_FRAGMENT": "Superior Dragon Fragment","EMERALD": "Emerald","ENCHANTED_RABBIT_FOOT": "Enchanted Rabbit Foot","LIGHT_BAIT": "Light Bait","HOT_POTATO_BOOK": "Hot Potato Book","ENCHANTED_ICE": "Enchanted Ice","CLAY_BALL": "Clay","OLD_FRAGMENT": "Old Dragon Fragment","GREEN_GIFT": "Green Gift","PACKED_ICE": "Packed Ice","WATER_LILY": "Lily Pad","LOG_2": "Acacia Wood","HAMSTER_WHEEL": "Hamster Wheel","ENCHANTED_OBSIDIAN": "Enchanted Obsidian","ENCHANTED_COAL": "Enchanted Coal","ENCHANTED_QUARTZ": "Enchanted Quartz","COAL": "Coal","ENDER_PEARL": "Ender Pearl","ENCHANTED_COAL_BLOCK": "Enchanted Block of Coal","ENCHANTED_PRISMARINE_CRYSTALS": "Enchanted Prismarine Crystals","ENCHANTED_WET_SPONGE": "Enchanted Wet Sponge","ENCHANTED_RAW_FISH": "Enchanted Raw Fish","ENDER_STONE": "End Stone","QUARTZ": "Nether Quartz","FOUL_FLESH": "Foul Flesh","RAW_BEEF": "Raw Beef","ENCHANTED_EYE_OF_ENDER": "Enchanted Eye of Ender","ENCHANTED_CARROT_STICK": "Enchanted Carrot on a Stick","RECOMBOBULATOR_3000": "Recombobulator 3000","SUGAR_CANE": "Sugar Cane","MAGMA_CREAM": "Magma Cream","RED_GIFT": "Red Gift","ENCHANTED_RAW_BEEF": "Enchanted Raw Beef","ENCHANTED_FEATHER": "Enchanted Feather","ENCHANTED_SLIME_BLOCK": "Enchanted Slime Block","ENCHANTED_OAK_LOG": "Enchanted Oak Wood","RABBIT_HIDE": "Rabbit Hide","WHITE_GIFT": "White Gift","RABBIT": "Raw Rabbit","SULPHUR": "Gunpowder","NETHER_STALK": "Nether Wart","DARK_BAIT": "Dark Bait","ENCHANTED_CARROT": "Enchanted Carrot","ENCHANTED_PUMPKIN": "Enchanted Pumpkin","ROTTEN_FLESH": "Rotten Flesh","ENCHANTED_COOKED_FISH": "Enchanted Cooked Fish","OBSIDIAN": "Obsidian","MINNOW_BAIT": "Minnow Bait","ENCHANTED_MAGMA_CREAM": "Enchanted Magma Cream","ENCHANTED_FIREWORK_ROCKET": "Enchanted Firework Rocket","LEATHER": "Leather","ENCHANTED_COOKED_MUTTON": "Enchanted Cooked Mutton","ENCHANTED_RABBIT": "Enchanted Raw Rabbit","ENCHANTED_BREAD": "Enchanted Bread","FUMING_POTATO_BOOK": "Fuming Potato Book","ENCHANTED_CHARCOAL": "Enchanted Charcoal","ENCHANTED_BLAZE_POWDER": "Enchanted Blaze Powder","SUMMONING_EYE": "Summoning Eye","FISH_BAIT": "Fish Bait","SNOW_BLOCK": "Snow Block","ENCHANTED_BAKED_POTATO": "Enchanted Baked Potato","COMPACTOR": "Compactor","ENCHANTED_DIAMOND": "Enchanted Diamond"}

def bazaar_load():
    output = json.loads(request.urlopen("https://api.hypixel.net/skyblock/bazaar?key={apikey}".format(apikey=key)).read())
    return output

def get_key(val): 
    for key, value in replacements.items(): 
         if val == value.lower(): 
             return key 
    return 0

def list_in_str(a, b):
    for entry in a:
        if entry in b:
            return True
    return False

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    game = discord.Game("being developed")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if list_in_str(["fuck", "shit", "faggot", "gay", "bitch", "dick", "ass", "cock"], message.content): #primitive swear filter, might need to change in the future
        await message.channel.send('>:(')
    elif message.content.startswith('$help'):
        await message.channel.send('*-- not implemented --*')
    elif message.content.startswith('$bazaar'):
        args = get_key(message.content[8:].lower())
#        print(args)
#        print(key)
        bazaar = bazaar_load()
        try:
            product = bazaar["products"][args]["quick_status"]
            await message.channel.send('__{item}__\nBuy price: {buy} coins\nSell price: {sell} coins\nMargin: {margin} coins'.format(item=replacements[args], buy=round(product["buyPrice"], 2), sell=round(product["sellPrice"], 2), margin=round(product["buyPrice"]-product["sellPrice"], 2)))
        except KeyError:
            await message.channel.send('Invalid item.')
    elif message.content.startswith('$isplayer'):
        try:
            username = json.loads(request.urlopen('https://api.mojang.com/users/profiles/minecraft/{username}'.format(username=message.content[10:])).read())
            await message.channel.send('{username} is a player.\nhttps://crafatar.com/renders/body/{uuid}?scale=5'.format(username=username['name'],uuid=username['id']))
        except:
            await message.channel.send('{username} is not a player.'.format(username=message.content[9:]))
    elif message.content.lower().startswith('bad bot'):
        await message.channel.send(':(')
    elif message.content.lower().startswith('good bot'):
        await message.channel.send(':)')
    elif message.content == 'ping':
        await message.channel.send('pong')
    elif message.content.startswith('$refresh'):
        if message.author.name == "0x3b":
            await message.channel.send('Refreshing...')
            await client.close()
            os.system("python3 bot.py")
    elif message.content.startswith('$close'):
        if message.author.name == "0x3b":
            await client.close()
    elif message.content.startswith('$echo'):
        await message.channel.send(message.content[5:])
    elif message.content.startswith('$stats'):
        player = message.content[7:]
        await message.channel.send('https://sky.lea.moe/stats/%s' %player)
    elif message.content.startswith('$whte_rbt.obj'):
        await message.channel.send('https://vignette.wikia.nocookie.net/jurassicpark/images/b/b3/Ahahahreal.gif')
    elif message.content.startswith('$'):
        await message.channel.send('c\'mon mate this isn\'t a command')

client.run('client-token')