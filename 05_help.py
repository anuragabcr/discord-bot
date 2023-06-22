from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description='Welcome to help sections. here are all the Bot commands',
        color=discord.Color.random()
    )
    embed.add_field(
        name='!help',
        value='List all the commands',
        inline=False
    )
    embed.add_field(
        name='!info',
        value='Information of discord server',
        inline=False
    )
    embed.add_field(
        name='!punched',
        value='Give a name after punched.',
        inline=False
    )
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


@bot.command()
async def punched(ctx, arg):
    await ctx.send(f'{ctx.author} punched {arg}')


bot.run('MTEyMTExNjIzODI3ODU3NDE4MQ.GgxA_o.MZv9cldFVa7uRVHSnNOE-nTFDud_VL4-o1rghg')
