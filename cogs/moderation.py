import discord
from discord.ext import commands
bot_embed_color = 0x4548a8


class Moderation(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
 
  @commands.command()
  async def kick(self, ctx, target: discord.Member = None, *,reason: str = None):
      if ctx.author.guild_permissions.kick_members:
          if target is None:
              embed = discord.Embed(description="Cannot kick cause member is not mentioned. ", color=bot_embed_color)
              await ctx.reply(embed=embed)
              return
          if target == ctx.author:
              embed = discord.Embed(description="You cannot kick yourself. ", color=bot_embed_color)
              await ctx.reply(embed=embed)
              return
          if target == ctx.guild.owner:
              embed = discord.Embed(description="You cannot kick the guild owner.", color=bot_embed_color)
              await ctx.reply(embed=embed)
              return
            
              await target.kick(reason=str(reason))

              if reason is None:
                  embed = discord.Embed(description=f"{target.mention} has been kicked successfully by {ctx.author.mention} "
                                              f"without any given reason. ", color=bot_embed_color)
              else:
                  embed = discord.Embed(description=f"{target.mention} has been kicked successfully by {ctx.author.mention}. "
                                              f"\nReason given: {reason}", color=bot_embed_color)
                  await ctx.reply(embed=embed)
              else:
                  embed = discord.Embed(description=f"Cannot kick {target.mention} cause {ctx.author.mention} "
                                          f"do not have the permissions to kick members. ", color=bot_embed_color)
        await ctx.reply(embed=embed)
    
def setup(bot):
  bot.add_cog(Moderation(bot))
