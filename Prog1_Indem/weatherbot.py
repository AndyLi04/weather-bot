import discord
import os
 
client = discord.Client()
 
@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
   if message.author == client.user:
       return
 
   if message.content.startswith('Botar!'):
       await message.channel.send('Bib bop bop')
   elif 'Jag frågar' in message.content:
       await message.channel.send('Jag är inte människa 😞')

client.run('OTUwMzY0NjYxODkzNzIyMTcy.YiX2EA.1iAkA9mD04kBghnIAhsHU72lK7w')

