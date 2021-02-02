import discord
from discord.ext import commands
from discord import *


TOKEN = 'include your token here'
   
 
def main():
    global bot
    print ("Starting...")
    run_commands()


def run_commands():
    bot = commands.Bot(command_prefix='^')
      
      
    @bot.command(pass_context=True)
    async def clear(ctx, amount=10):
        await ctx.channel.purge(limit=amount)  

                
    @bot.command(pass_context=True)         
    async def banall(ctx):
        for m in ctx.guild.members:
            try:
                await m.ban(reason="По просьбе")
            except:
                pass


    @bot.command(pass_context=True)             
    async def delrole(ctx):
        for m in ctx.guild.roles:
            try:
                await m.delete(reason="По просьбе")
            except:
                pass


    @bot.command(pass_context=True)             
    async def delchannel(ctx):
        failed = []
        counter = 0
        for channel in ctx.guild.channels:
            try:
                await channel.delete(reason="По просьбе")
            except: failed.append(channel.name)
            else: counter += 1
        fmt = ", ".join(failed)
        await ctx.send(f" {counter} channels deleted. {f' {fmt} was not deleted' if len(failed) > 0 else ''}")
        

        
    bot.run(TOKEN)



if __name__=="__main__":
    main()
