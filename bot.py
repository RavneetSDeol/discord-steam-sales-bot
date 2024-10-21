import discord
from discord import app_commands
import requests
from dotenv import load_dotenv
import os

# Set up the bot and commands
class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Bot logged in as {self.user}")
        self.tree.sync()