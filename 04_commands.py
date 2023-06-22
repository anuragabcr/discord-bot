from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


@bot.command()
async def punched(ctx, arg):
    await ctx.send(f'{ctx.author} punched {arg}')


bot.run('MTEyMTExNjIzODI3ODU3NDE4MQ.GgxA_o.MZv9cldFVa7uRVHSnNOE-nTFDud_VL4-o1rghg')
