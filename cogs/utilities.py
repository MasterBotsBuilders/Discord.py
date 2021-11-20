import discord
from discord.ext import commands
import random
import LyricsScraper
import requests
import aiohttp


class utilities(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    
    
    @commands.command(pass_context=True)
    async def lyrics(self, ctx, *args):
        track = " ".join(args)
        user = ctx.author
        for activity in user.activities:
            if isinstance(activity, Spotify):
                track = activity.title + " by " + str(activity.artist).split(";")[0]
        if track == "" or track == " " or track.isspace():
            await ctx.reply(":question: What track to search? Correct format: `~lyrics [Query]`", delete_after=10)
            return
        else:
            wait = await ctx.reply(f":mag: Please hold on, searching for `{track}`")
            try:
                search_lyrics = LyricsScraper()
                try:
                    search_lyrics.musixmatch_lyrics(query=track)
                except TimeoutError:
                    search_lyrics.google_lyrics(query=track)
                except:
                    search_lyrics.genius_lyrics(query=track,
                                            api_key="API Key")
                embed = discord.Embed(title=search_lyrics.title, description="**" + search_lyrics.artist + "**",
                                  colour=0xffae00)
                lyric = str(str(search_lyrics.lyrics).strip()).split("\n\n")
                for i in lyric:
                    embed.add_field(name="​", value=i, inline=False)
                embed.set_footer(text="Source: " + search_lyrics.source)
                try:
                    await wait.edit(embed=embed, content="")
                except:
                    embed = discord.Embed(title=":x: Something went wrong, can't show lyrics. Click here. ",
                                          url=search_lyrics.url, colour=0xffae00)
                    await wait.edit(embed=embed, content="")
            except:
                await wait.edit(content=":x: Something went wrong, can't show lyrics ")
                
    @commands.command(aliases=['ethereum'])
    async def eth(self, ctx):
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
        em.set_author(name='Ethereum', icon_url='https://cdn.disnakeapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
        await ctx.reply(embed=em)

    @commands.command(aliases=['bitcoin'])
    async def btc(self, ctx):
        r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
        r = r.json()
        usd = r['USD']
        eur = r['EUR']
        em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
        em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
        await ctx.reply(embed=em)
     
    
    
def setup(bot):
  bot.add_cog(utilities(bot))
