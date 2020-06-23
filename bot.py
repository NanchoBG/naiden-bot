import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'na4o ')

@client.event
async def on_ready(): 
    print ('zdr mangali, kak e havata')

@client.command(aliases=['zdrasti','zdravey', 'zdr kp','zdr ks'])
async def zdr(ctx):
    responses = ['zdr', 'zdrasti','zdravey',
                'zdr manqk', 'zdrasti manqk','zdravey manqk',
                'zdr bratle', 'zdrasti bratle','zdravey bratle',
                'zdr pi4', 'zdrasti pi4','zdravey pi4',
                'zdr kp', 'zdr kp', 'zdr ko staa', 'zdrasti ko staa', 'zdr kak e']
    await ctx.send(random.choice(responses))


client.run('NzI1MDI4NjAxNTQ3OTgwODMw.XvI8Qg.qetBA9rIVAscnmjIE_brrv1hNJk')