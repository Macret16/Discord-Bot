import discord
from discord import Game
import json
import aiohttp
import asyncio
import random
import discord.voice_client
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import requests
from config import prefix, token, ownerid, link
import time
import parse
import urllib


client = Bot(prefix)
status = [
    "Matchmaking...",
    "Doing Fun!",
    "PUBG Mobile!",
    "Valorant!",
    "Bathing!",
    "Watching Movie!",
    "Raising Puppies!",
    "Feeding Animals!",
]


@client.event
async def on_ready():
    await client.change_presence(activity=Game(name=random.choice(status)))
    print("----------------------")
    print("Logged In As")
    print("Username: %s" % client.user.name)
    print("ID: %s" % client.user.id)
    print("----------------------")


@client.command(name='ping', description='Shows current ping of Jodd')
async def ping(ctx):
    ping = round(client.latency * 1000)
    await ctx.send(f"My ping is {ping}ms.")


@client.command(name='botinvite', description='For inviting Jodd in your server.')
async def botinvite(ctx):
    '''A Link To Invite This Bot To Your Server!'''
    await ctx.send("Check Your Dm's :wink:")
    await ctx.author.send(link)


@client.command(name='joke', description='Cracks some cool jokes.')
async def joke(ctx):
    r = requests.get(
        'https://sv443.net/jokeapi/v2/joke/Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,racist,sexist&type=single').json()
    joke = r['joke']
    await ctx.send(joke)


@client.command(name='bitcoin', description='Shows Current Bitcoin Price.')
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])


@client.command(name='ask', description='Replies to your questions.')
async def ask(ctx):
    possible_responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no.',
        'Outlook not so good.',
        'Very doubtful.'
    ]
    await ctx.send(ctx.author.mention + " " + random.choice(possible_responses) + ".")


@client.command(name='meme', description='Shows you amazing memes from Reddit.', category='Jodd Help')
async def meme(ctx):
    content = requests.get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color=discord.Color.random(
    )).set_image(url=f"{data['url']}")
    await ctx.send(embed=meme)


@client.command(name='clear', description='It deletes the number of messages you give with amount.')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify the amount of messages to be deleted.")


@client.command(name='server', description='Shows details of this server.')
async def server(ctx):
    owner = str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    embed = discord.Embed(
        title=ctx.guild.name,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=False)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)


@client.command(name='submit')
async def submit(ctx, *submit):
    a = submit
    an = ''
    for i in a:
        an += i+' '
    await ctx.send(f"{ctx.author.mention}'s Answers -\n{an}")


@client.command(name='test')
async def test1(ctx):
    button1 = Button(label="Click Here!", style=ButtonStyle.gray, emoji=None)
    # async def button_callback(interaction):
    #     await interaction.response.send_message("Hi")
    #button1.callback = button_callback
    await ctx.send(button1)


client.run(token, bot=True, reconnect=True)
