import random
import discord
from discord.ext import commands
import os, sys

bot = commands.Bot(command_prefix="q!", case_insensitive=True, self_bot=True)

def stop_bot():
  """Stops The Bot"""
  os.execv(sys.executable, ['python'] + sys.argv)

class Giveaway:
    @staticmethod
    def rand_double():
        return random.random()

    @staticmethod
    def select_winners(participants, winners):
        winlist = []
        pullist = list(participants)
        for _ in range(winners):
            if pullist:
                winner_index = int(Giveaway.rand_double() * len(pullist))
                winner = pullist.pop(winner_index)
                winlist.append(winner)
        return winlist

@bot.command()
async def ping(ctx: commands.Context):
    """responds with pong"""
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def predict(ctx: commands.Context, num_of_winners: int, msg_id: int, emoji: str):
    """Predicts the winner of a giveaway."""
    await ctx.send("Checking...")

    try:
        getmsg = await ctx.channel.fetch_message(msg_id)
        reactions = None
        for reaction in getmsg.reactions:
            if str(reaction) == emoji:
                reactions = reaction
                break
        
        if reactions is None:
            await ctx.reply("Emoji not found on the message.")
            return
        
        participants = []
        async for user in reactions.users():
            if not user.bot:
                participants.append(user)
        
        if not participants:
            await ctx.reply("No valid participants found.")
            return
        
        number_of_winners = num_of_winners  # You can change this number as needed
        winners = Giveaway.select_winners(participants, number_of_winners)
        winner_names = ", ".join([winner.name for winner in winners])
        
        await ctx.reply(f"The predicted winner(s) are: **{winner_names}**")
    
    except discord.NotFound:
        await ctx.reply("Giveaway Message not found.")

@bot.command()
async def hide(ctx: commands.Context):
    """hides a message (dk why i added this)"""
    await ctx.send("E\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\nE\n")

@bot.command()
async def stop(ctx: commands.Context):
    """stops the bot"""
    await ctx.send('Stopping...')
    stop_bot()

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!!!")

bot.run("TOKEN")