# 🎮 Steam Sales Discord Bot

A simple Discord bot that fetches and displays the latest Steam sales using a slash command. Built using `discord.py`, this bot interacts with the [Steam Store API](https://store.steampowered.com/api/featuredcategories) and shows users the top discounted games directly in your Discord server.

## ✨ Features

- Slash command `/steamsales` to display current Steam sales.
- Automatically formats and presents discounted titles, percentages, and prices.
- Clean and minimal code structure for easy customization.

## 📦 Requirements

- Python 3.8+
- `discord.py` (version supporting `app_commands`)
- `requests`
- `python-dotenv`

🔧 Setup
1. Clone the repository:
git clone https://github.com/yourusername/steam-sales-discord-bot.git
cd steam-sales-discord-bot

2. Create a .env file in the root directory and add your bot token:
DISCORD_TOKEN=your_discord_bot_token_here

3. Run the bot:
python main.py

Once the bot is online, use the /steamsales command in any server it's invited to.

📜 Example Output  
Here are the current Steam sales:  
**Half-Life: Alyx** - 60% off! Now: $23.99 (was $59.99)  
**Cyberpunk 2077** - 50% off! Now: $29.99 (was $59.99)  
...  

🧠 Notes
* The bot uses app_commands.CommandTree to register slash commands.
* The command output is limited to the first 100 sales for readability.
* Steam API responses may vary depending on region or availability.

🚀 Future Improvements
* Add filters for genre, price range, or publisher.
* Include embedded messages for a cleaner UI.
* Add a scheduled daily update to post top sales automatically.
