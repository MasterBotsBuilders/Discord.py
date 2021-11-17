import discord
from discord.ext import commands
import random
import requests
import aiohttp


class Fun(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(help="Sends a meme.")
    async def meme(self, ctx):
        data = await req("https://meme-api.herokuapp.com/gimme")
        if data["nsfw"] is False:
            meme = discord.Embed(
                title=f"{data['title']}", Color=discord.Color.random()
            ).set_image(url=f"{data['url']}")
        else:
            await ctx.reply("Please run the command again.", delete_after=db["del"])
        await ctx.reply(embed=meme, delete_after=db["del"])

  @commands.command(aliases = ["8ball", "8b", "8"])
  async def _8ball(self, ctx, *, Question):
    responses = ["as I see it, yes", "yes!!!", "no!!!", "heck off, you know that's a no", "i can tell you certainly, no", " that would be a hell no", "ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again",
             "don’t count on it", "It is certain", "it is decidedly so", "most likely", "my reply is no", "my sources say no",
             "outlook not so good", "outlook good", "signs point to yes", "very doubtful", "without a doubt",
             "yes", "yes, definitely", "you may rely on it", "when you grow a braincell, yes",  "yes, idiot", "yes???",  "sure, why not"]
    response = random.choice(responses)
    em=discord.Embed(title=f'8ball Has Spoken', description=f'🎱 {response}', color=ctx.author.color)
    await ctx.send(embed=em)
    
    
  @commands.command()
  async def gayrate(self, ctx, *, name=None):
    rate = random.randrange(99)
    rate1 = rate + 1
    if name == None:
      user = ctx.author
      embed = discord.Embed(title = "Gayrate Machine", description = f"You are {rate1}% gay 🏳️‍🌈" , color = ctx.author.color)
      await ctx.send(embed = embed)
    else:
      em=discord.Embed(title = "Gayrate Machine", description = f"{name} is {rate1}% gay 🏳️‍🌈" , color = ctx.author.color)
      await ctx.send(embed=em)

    
  @commands.command()
  async def pp(self, ctx, *, name=None):
    random_number = random.randint(0, 30)
    alphabet = '='
    ppsize = alphabet * random_number
    if name ==None:
      user = ctx.author
      embed = discord.Embed(title='PP size machine', description=f"{user.name}'s pp \n 8{ppsize}D", color=ctx.author.color)
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(title='PP size machine', description=f"{name}'s pp \n 8{ppsize}D", color=ctx.author.color)
      await ctx.send(embed=embed)

  
  @commands.command()
  async def simprate(self, ctx, *, name=None):
    rate = random.randrange(99)
    rate1 = rate + 1
    if name == None:
      user = ctx.author
      embed = discord.Embed(title = "Simprate Machine", description = f"You are {rate1}% simp" , color = ctx.author.color)
      await ctx.send(embed = embed)
    else:
      em=discord.Embed(title = "Simprate Machine", description = f"{name} is {rate1}% simp" , color = ctx.author.color)
      await ctx.send(embed=em)


  @commands.command()
  async def emojify(self, ctx, *, text):
    emojis = []
    for s in text:
        if s.isdecimal():
            num2emo = {
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine'
            }

            emojis.append(f':{num2emo.get(s)}:')
        elif s.isalpha():
            emojis.append(f':regional_indicator_{s}: ')
        else:
            emojis.append(s)       
    await ctx.message.delete()
    await ctx.send(''.join(emojis))

  @commands.command()
  async def joke(self, ctx):
    response = requests.get("https://icanhazdadjoke.com", headers = {"Accept": "text/plain"})
    embed = discord.Embed(title = "Random Joke!", description = response.text, color = ctx.author.color)
    await ctx.send(embed = embed)


  @commands.command()
  async def insult(self, ctx, *, member: discord.Member = None):
    if member == None: member = ctx.author
    async with aiohttp.ClientSession() as session:
      async with session.get("https://insult.mattbas.org/api/insult") as response:
        insult = await response.text()
        await ctx.send(f"{member.mention} {insult}.")
  
def setup(bot):
  bot.add_cog(Fun(bot))
