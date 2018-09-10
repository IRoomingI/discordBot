## Discord Bot

This is a bot written in Python with help of the [discord.py API](https://github.com/Rapptz/discord.py "discord.py Github Page").

_Important! You should know how to create and set up a Discord bot_

Packages you need to run the bot:

*   Python 3.5 or 3.6 (3.7 or newer may not work) [[Download](https://python.org/downloads/ "Python Download")]
*   discord.py package for Python (look at [discord.py](https://github.com/Rapptz/discord.py "discord.py Github Page") GitHub for installation info)
*   asyncio package for Python
    `python3 -m pip install -U asyncio`
*   colorama package for Python (colored commandline output)
    `python3 -m pip install -U colorama`


## Please Read:

Please don't think that this project will reach huge scales, like other bots coded by people much more talented than I am.
This is project was started for fun and I can't promise frequent updates.

## Installation

*   Clone or Download this repository to any place (I recommend a place you'll remember ;D)
*   Enter the folder and configure the _CONFIG.json_ <br>
    ```
    "TOKEN" : "0123456789abcdefg"   (example Token)
    "PREFIX" : "COMMAND_PREFIX"     (default is "+")
    "OWNER_ID" : "22234234354326"   (your discord user id)
    "GAME" : "a game"               (game that the bot plays) 
    ``` 
*   Execute the _main.py_ 
    `python3 main.py`
*   **or** use the _start.sh_ if you are on Linux `sh start.sh` (make sure you are in the same folder and have _screen_ installed)
*   That's all, now the bot should be running

## Commands

Note: replace [PREFIX] with the prefix you chose in the CONFIG.json **or** use the new _prefix_ command (default is: +)

*   _[PREFIX]help_ - shows the help text (there may be more information than here)
*   _[PREFIX]clear 4_  - deletes 4 messages from the channel including the command message (max number is 99)
*   _[PREFIX]ping_  - the bot sends you a private message "Pong!" (not your ping in milliseconds)
*   _[PREFIX]say Hello World_  - the bot sends this message and deletes your message
*   _[PREFIX]game Half Life 3_  - changes the game the bot is playing
*   _[PREFIX]prefix :_ - changes the preferred command prefix (max length is 8)
