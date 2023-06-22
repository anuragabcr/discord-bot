import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot is now online and ready to work')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content=='hello':
        await message.channel.send('Welcome to Bot learning')


client.run('MTEyMTExNjIzODI3ODU3NDE4MQ.GgxA_o.MZv9cldFVa7uRVHSnNOE-nTFDud_VL4-o1rghg')
