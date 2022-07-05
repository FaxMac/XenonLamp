# XenonLamp
Python Discord Bot to see the status of Valve Games (Source Query/A2S)

Fetures
------
- Constant update of playercount in status
- Slash command to see players online in the server

Requirements
------
[python-a2s](https://github.com/Yepoleb/python-a2s) `pip3 install python-a2s`

[py-cord >=2.0.0-rc.1](https://docs.pycord.dev/en/master/installing.html#installing)`pip3 install -U py-cord --pre`

Usage
------
inside of the main.py file you'll find `bot.run()` and direction = `("X.X.X.X", 27015)`, in the first one you put your discord bot token and in the second you put your IP + Port. Pretty self-explanitory.

TO-DO
------
- [ ] Make a slash command that edits the IP and port, that is only usable for admins
- [ ] When using `/list` when a server timeout occurs (like when the game server is offline), it raises a 404 error, figure out what is going on with that
