import discord
import asyncio
import sys
import random
import re
import os
client=discord.Client()

@client.event
async def on_ready():
    print('Welcome message bot Logged in')
    print(client.user.name)
    print(client.user.id)
    print('-----')

newUserMessage = """your message
"""

@client.event

async def on_member_join(member):
    await client.send_message(member, newUserMessage)

client.run('your token') 
