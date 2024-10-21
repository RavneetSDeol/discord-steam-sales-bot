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

# Create the slash command
@bot.tree.command(name="steamsales", description="View current Steam sales")
async def steamsales(interaction: discord.Interaction):
    # Fetch Steam sales
    sales = get_steam_sales()

    if not sales:
        await interaction.response.send_message("Sorry, I couldn't retrieve any sales at the moment.")
        return
    
    sale_list = "\n".join([f"**{sale['name']}** - {sale['discount_percent']}% off!" for sale in sales[:5]])
    await interaction.response.send_message(f"Here at the current Steam sales:\n{sale_list}")