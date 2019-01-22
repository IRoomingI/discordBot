# Discord Bot

This is a bot written in Python with help of the [discord.py API](https://github.com/Rapptz/discord.py "discord.py Github Page").

**Important!** You should know how to create and set up a Discord bot

Packages you need to run the bot:

* Python 3.5 or higher [[Download](https://python.org/downloads/ "Python Download")]

* discord.py package for Python (look at [discord.py](https://github.com/Rapptz/discord.py "discord.py Github Page") GitHub for installation info)

* asyncio package for Python `python3 -m pip install -U asyncio`

* colorama package for Python (colored commandline output) `python3 -m pip install -U colorama`

## Please Read

Please don't think that this project will reach huge scales, like other bots coded by people much more talented than I am.
This is project was started for fun and I can't promise frequent updates.

## Installation

* Clone or Download this repository to any place (I recommend a place you'll remember ;D)

* Enter the folder and configure the _CONFIG.json_

    ```json
    "TOKEN" : "0123456789abcdefg"   (example Token)
    "PREFIX" : "COMMAND_PREFIX"     (default is "+")
    "OWNER_ID" : "22234234354326"   (your discord user id)
    "GAME" : "a game"               (game that the bot plays)
    ```

* Execute the _main.py_ `python3 main.py`

* **or** use the _start.sh_ if you are on Linux `sh start.sh` (make sure you are in the same folder and have _screen_ installed)

* That's all, now the bot should be running

## Commands

Note: You can change the command prefix in the CONFIG.json or with the _prefix_ command (default prefix is: +)

Arguments in these brackets <> mean they are neccessary. Arguments in \[ ] are optional

| Command | Arguments | Example | Explanation |
|---------|:------------------------------------:|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| help | - | `+help` | Sends a message with all commands their arguments and a short explanation. |
| clear | \<number> | `+clear 42` | Deletes messages from the channel including the command message (max number is 99) |
| ping | \[string] | `+ping` | Sends you a private message saying "Pong!" with your optionally attached arguments. |
| say | \<string> | `+say Hello World!` | The bot sends the text as a message and deletes your message. |
| game | \<string> | `+game Half Life 3?` | Changes the game the bot is playing to the text you enter. |
| prefix | \<string> | `+prefix ~` | Changes the preferred command prefix (max length is 8). _OWNER ONLY_ |
| nick | \<string> | `+nick A better name` | Changes your nickname on the server. |
| color | <add/remove/list/color_name> \[@role] | `+color add red @redrole` `+color remove green` `+color red` `+color list` | Add roles as colors your members can choose from.(Owner Only)  Remove a role from the 'color table'. (Owner Only) Change your color. List all colors. |
| poll | \<string> \<list> | `+poll "Some description for the poll" ["Option 1", "Option 2", "Option3"]` | Create a poll. You can vote by reacting to the message. The creator of the poll can close it by reacting with a :x:. |
| autrole | <add/remove> <@role> | `+autorole add @Member` `+autorole remove @cool` | Configure which roles should be automatically assigned to users joining the server. |
