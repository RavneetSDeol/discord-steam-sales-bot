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

Install dependencies with:

```bash
pip install -r requirements.txt
