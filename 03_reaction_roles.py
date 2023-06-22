import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1121329384918372403

    async def on_ready(self):
        print('Ready')

    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        if payload.emoji.name == '🤟':
            role = discord.utils.get(guild.roles, name='love')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🤑':
            role = discord.utils.get(guild.roles, name='money')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, name='enjoy')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != self.target_message_id:
            return
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        if payload.emoji.name == '🤟':
            role = discord.utils.get(guild.roles, name='love')
            await member.remove_roles(role)
        elif payload.emoji.name == '🤑':
            role = discord.utils.get(guild.roles, name='money')
            await member.remove_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, name='enjoy')
            await member.remove_roles(role)


client = MyClient(intents=intents)

client.run('MTEyMTExNjIzODI3ODU3NDE4MQ.GgxA_o.MZv9cldFVa7uRVHSnNOE-nTFDud_VL4-o1rghg')
