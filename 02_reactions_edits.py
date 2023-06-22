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
    if message.content == 'cool':
        await message.add_reaction('\U0001F60E')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message \n'
        f'Before {before.content} \n'
        f'After {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


client.run('MTEyMTExNjIzODI3ODU3NDE4MQ.GgxA_o.MZv9cldFVa7uRVHSnNOE-nTFDud_VL4-o1rghg')
