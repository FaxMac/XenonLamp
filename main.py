import socket

import a2s
import discord
from discord.ext import tasks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Sourcespagetthi part (aka, get our Player Names and put it on a list)

    def player_names(address):
        InfoOfPlayers = []
        try:
            currentDataOfPlayers = a2s.players(address)
            for x in currentDataOfPlayers:
                InfoOfPlayers.append([x.name, x.score])
        except socket.timeout:
            InfoOfPlayers.append(["Error:", "Server Time out"])
        return InfoOfPlayers

########################################### Put your ip here
    direction = ("192.168.1.10", 27015)
###########################################


    # ended a2s madness, now discord bot madness

    bot = discord.Bot()


    @bot.event
    async def on_ready():
        print(f"We have logged in as {bot.user}")
        updatestatus.start()


    @tasks.loop(seconds=2)
    async def updatestatus():
        try:
            activity = discord.Activity(
                name=f"Jugadores: {a2s.info(direction).player_count}/{a2s.info(direction).max_players}| Mapa: {a2s.info(direction).map_name}",
                type=0)
        except socket.timeout:
            activity = discord.Activity(
                name="Error: Server timed out",
                type=0)
        except OSError:
            activity = discord.Activity(
                name="Error: Routing error",
                type=0)
        except ConnectionRefusedError:
            activity = discord.Activity(
                name="Error: Target port closed",
                type=0)
        await bot.change_presence(status=discord.Status.online, activity=activity)


    @bot.slash_command(name="list", description="Returns the list of players",
                       guild_ids=[208800527084027916]) ###########################################Put your guild id here
    async def playerlistcom(ctx):
        embed = discord.Embed(title="User List:")
        user_data = player_names(direction)
        print(len(user_data))
        if len(user_data) == 0:
            embed.add_field(name="No players online", value="Try Later", inline=False)
        else:
            for x in user_data:
                embed.add_field(name=f"**{x[0]}**", value=f"Score: {x[1]}", inline=False)
        await ctx.respond(embed=embed)

#################### Put your bot token here
    bot.run('your bot token')
####################
