# bot.py
import os
import random
import requests
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
LEAGUE = "RGAPI-f4efad86-371d-4116-80c7-a627d0ab024d"

bot = commands.Bot(command_prefix='op.')

@bot.command(name='gg', help="returns user's rank")
async def searchup(ctx, username):
    response = ""
    summoner = requests.get(f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}?api_key={LEAGUE}")

    acc_info = json.loads(summoner.text)
    print("_______________Print Converted JSON_____________________")
    print(acc_info)
    
    acc_id = acc_info['id']

    rank = requests.get(f"https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{acc_id}?api_key={LEAGUE}")
    rank_info = json.loads(rank.text)

    print("_______________Print Converted JSON_____________________")
    print(rank_info)
    try:
        response = acc_info['name'] + " is " + str(rank_info[0]['tier']+ " " + rank_info[0]['rank'])
    except:
        response = "play more ranked games numbnut"
    await ctx.send(response)

bot.run(TOKEN)

