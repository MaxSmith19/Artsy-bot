import discord
from discord.ext import commands
from discord.utils import get
from roles import ROLES
import asyncio  

bot = discord.Client()

botTesting=bot.get_channel(821435572891287603)
rules=bot.get_channel(821433342632788018)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

@bot.event
async def on_reaction_add(reaction, user):
    await rules.send()
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('?React'):
        await message.add_reaction("👍")

@bot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send('{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))
    print(user.name,reaction.emoji)
    if reaction.emoji == "👍":
        role = get(member.roles, name="Test")
        await bot.add_roles(user.name, role)


bot.run('')   
