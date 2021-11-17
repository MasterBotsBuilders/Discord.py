import discord
import os
from discord.ext import commands


token = config.get('token')
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or",", strip_after_prefix = True, intents = intents)


@bot.event
async def on_ready():
  print("Bot is ready")
  
  
@bot.command()
@commands.is_owner()
async def unloadall(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            bot.unload_extension(f"cogs.{filename[:-3]}")
            await ctx.send(f"Unloaded `{filename[:-3]}` successfully!")    

@bot.command()
@commands.is_owner()
async def loadall(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            bot.load_extension(f"cogs.{filename[:-3]}")
            await ctx.send(f"Loaded `{filename[:-3]}` successfully!")
            
            
bot.load_extension("cogs.fun")
bot.load_extension("cogs.moderation")
bot.run(token)
