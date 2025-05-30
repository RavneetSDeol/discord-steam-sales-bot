import discord
from discord import app_commands
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set up the bot and commands
class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default()) # Set up the basic bot functionality
        self.tree = app_commands.CommandTree(self) # Create a command tree to register slash commands

    async def on_ready(self):
        print(f"Bot logged in as {self.user}") # Print when the bot is logged in
        await self.tree.sync() # Sync the commands with Discord

# Function to fetch Steam sales data
def get_steam_sales():
    url = "https://store.steampowered.com/api/featuredcategories"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("specials", {}).get("items", [])
    else:
        return []
    
if __name__ == "__main__":
    bot = MyBot()

    # Create the slash command
    @bot.tree.command(name="steamsales", description="View current Steam sales")
    async def steamsales(interaction: discord.Interaction):
        # Fetch Steam sales
        sales = get_steam_sales()

        if not sales:
            await interaction.response.send_message("Sorry, I couldn't retrieve any sales at the moment.")
            return
    
        # Format the response
        sale_list = "\n".join([
            f"**{sale['name']}** - {sale['discount_percent']}% off! "
            f"Now: ${(sale['final_price'] / 100):.2f} (was ${(sale['original_price'] / 100):.2f})"
            for sale in sales[:100]
        ])  # Limit to 100 sales
        
        await interaction.response.send_message(f"Here are the current Steam sales:\n{sale_list}")

    
    TOKEN = os.getenv("DISCORD_TOKEN") # Load token from environment variables
    bot.run(TOKEN)