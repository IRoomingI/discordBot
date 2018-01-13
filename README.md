## Discord Bot

This is a bot written in Python with help of the [discord.py API](https://github.com/Rapptz/discord.py "discord.py Github Page").

_Important! You should know how to create and set up a Discord bot_

Packages you need to run the bot:

*   Python 3.5 or higher [[Download](https://python.org/downloads/ "Python Download")]
*   discord.py package for Python (look at [discord.py](https://github.com/Rapptz/discord.py "discord.py Github Page") GitHub for installation info)
*   asyncio package for Python
    `pip install asyncio`


## Please Read:

Please don't think that this project will reach huge scales, like other bots coded by people much more talented than I am.
This is project was started for fun and I can't promise frequent updates.

## Installation

*   Clone or Download this repository to any place (I recommend a place you'll remember ;D)
*   Enter the folder and execute the _main.py_
    `python main.py`
*   That's all, now the bot should be running

## Commands

Note: replace [PREFIX] with the prefix you chose in the CONFIG.py (default is: +)

*   _[PREFIX]clear 4_  - deletes 4 messages from the channel including the command message (max number is 99)
*   _[PREFIX]ping_  - the bot sends you a private message "Pong!" (not your ping in milliseconds)
*   _[PREFIX]say Hello World_  - the bot sends this message and deletes your message
*   _[PREFIX]type Hey guys!_  - the bot "types" the message letter by letter
