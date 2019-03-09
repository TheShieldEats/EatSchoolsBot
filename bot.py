 #EAT By TheShield

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='.')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Fired up and ready to serve!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ffff)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ffff)
    embed.set_author(name="TheShield @ 2019 All Rights Reserved")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("MiniEATers")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Goodbye!, {}.".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="my name jeff", color=0x00ffff)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def minieaters(ctx):
    embed=discord.Embed(title="Education And Technology", url="https://eatschools.com/", description="Command List", color=0x80ffff)
    embed.set_author(name="MiniEATers", icon_url="https://www.eatschools.com/pluginfile.php/7/core_admin/logo/0x150/1551379216/Eat%20logo%20png.png")
    embed.set_thumbnail(url="https://www.eatschools.com/pluginfile.php/7/core_admin/logo/0x150/1551379216/Eat%20logo%20png.png")
    embed.add_field(name="Information about EAT, EATCOIN And MiniEATers", value="Please hurry up and create your account on the World Wide Web EOS Blockchain And eatschools.com By sending your grade to the WhatsApp on one of the representative numbers of eatschools.com, The cost of a working account is $ 10 will be deducted from the currencies acquired at no cost to the student and paid by the site ... The goal of the EOS account is to receive the EATCOIN currency that the student will receive for each mark they receive in the online exams ... The site eatschools.com will provide teachers in all subjects Arabic and other languages ​​... For more information watch this video. #learn_earn #teacholgy #eatschools", inline=False)
    embed.add_field(name="Nour eldin amr", value="01001150752", inline=True)
    embed.add_field(name="Nagham wael", value="01023846886", inline=True)
    embed.add_field(name="Nader Fawzy", value="01211793334", inline=True)
    embed.add_field(name="Kirollos Elia", value="01210678769", inline=True)
    embed.add_field(name="Joe Khaled", value="01203676177", inline=True)
    embed.add_field(name="Ahmed Gemy", value="01114673062", inline=True)
    embed.add_field(name="Moussa Tawfik", value="01223390222", inline=True)
    embed.add_field(name="Mario saad", value="01096883843", inline=True)
    embed.add_field(name="Maria Nader", value="01271337569", inline=True)
    embed.add_field(name="Logy Mohamed", value="01010586647", inline=True)
    embed.add_field(name="Mrawan Mostafa", value="01091620859", inline=True)
    embed.add_field(name="Ahmed Sherif", value="01013775801", inline=True)
    await bot.whisper(embed=embed)

@bot.command(pass_context=True)
async def minieater(ctx):
    embed=discord.Embed(title="Education And Technology", url="https://eatschools.com/", description="Command List", color=0x80ffff)
    embed.set_author(name="MiniEATers", icon_url="https://www.eatschools.com/pluginfile.php/7/core_admin/logo/0x150/1551379216/Eat%20logo%20png.png")
    embed.set_thumbnail(url="https://www.eatschools.com/pluginfile.php/7/core_admin/logo/0x150/1551379216/Eat%20logo%20png.png")
    embed.add_field(name="Information about EAT, EATCOIN And MiniEATers", value="Please hurry up and create your account on the World Wide Web EOS Blockchain And eatschools.com By sending your grade to the WhatsApp on one of the representative numbers of eatschools.com, The cost of a working account is $ 10 will be deducted from the currencies acquired at no cost to the student and paid by the site ... The goal of the EOS account is to receive the EATCOIN currency that the student will receive for each mark they receive in the online exams ... The site eatschools.com will provide teachers in all subjects Arabic and other languages ​​... For more information watch this video. #learn_earn #teacholgy #eatschools", inline=False)
    embed.add_field(name="Nour eldin amr", value="01001150752", inline=True)
    embed.add_field(name="Nagham wael", value="01023846886", inline=True)
    embed.add_field(name="Nader Fawzy", value="01211793334", inline=True)
    embed.add_field(name="Kirollos Elia", value="01210678769", inline=True)
    embed.add_field(name="Joe Khaled", value="01203676177", inline=True)
    embed.add_field(name="Ahmed Gemy", value="01114673062", inline=True)
    embed.add_field(name="Moussa Tawfik", value="01223390222", inline=True)
    embed.add_field(name="Mario saad", value="01096883843", inline=True)
    embed.add_field(name="Maria Nader", value="01271337569", inline=True)
    embed.add_field(name="Logy Mohamed", value="01010586647", inline=True)
    embed.add_field(name="Mrawan Mostafa", value="01091620859", inline=True)
    embed.add_field(name="Ahmed Sherif", value="01013775801", inline=True)
    await bot.whisper(embed=embed)

client.run(str(os.environ.get("BOT_TOKEN")))
