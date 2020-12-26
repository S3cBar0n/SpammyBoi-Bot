from discord.ext import commands
import discord
import os
import random

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
async def ping(ctx):
  await ctx.send("pong")


# Lucky command, it picks a number between 0-50 and spams your dm's with that number
@bot.command()
async def lucky(ctx):
  spamCount = random.randint(0, 50)
  for num in range(int(spamCount)):
    await ctx.message.author.send("ARE YOU FELLING LUCKY???")

# Basic spam command, you can provide a message and specify how many messages
@bot.command()
async def spam(ctx, spamCtx="spam", spamCount=1):
  for num in range(int(spamCount)):
    await ctx.send(str(spamCtx))

# Lets you mention a specific user who would like to spam in their DM's, you can specify a message
@bot.command()
async def attack(ctx, user: discord.User, *, message="GET SPAMMED NERD"):
  spamCount = 10
  for num in range(int(spamCount)):
    await user.send(message)

if __name__ == "__main__":
    bot.run(os.environ['TOKEN'])