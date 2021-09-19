import requests
import discord
import discord,json,os,random
from discord import Embed, File
from discord.ext import commands
import discord, datetime, time
import time
import asyncio
import smtplib
import datetime
from configparser import ConfigParser
import os
import sys
import json

token = "YOURBOTTOKEN"

client = commands.Bot(command_prefix='+')
client.remove_command('help')
help_command=None
        
@client.command()
async def help(ctx):
    embed = Embed(title="All Commands", description=None)
    embed.add_field(name="+help", value="Displays all available commands", inline=False)
    embed.add_field(name="+http", value="Sends a fresh http proxy list", inline=False)
    embed.add_field(name="+https", value="Sends a fresh https proxy list", inline=False)
    embed.add_field(name="+socks4", value="Sends a fresh socks4 proxy list", inline=False)
    embed.add_field(name="+socks5", value="Sends a fresh socsk5 proxy list", inline=False)
    embed.add_field(name="+all", value="Sends a fresh http, https, socks4 and socks5 proxy list", inline=False)
    embed.add_field(name="+email", value="Format - +email [count] [email] [message] - e.g +email 10 email@email.com lol!", inline=False)
    embed.add_field(name="+socials", value="Sends all of the creators socials", inline=False)  
    embed.add_field(name="+bypass", value="You can bypasss adlinks like linkvertise with this cmd", inline=False)
    embed.add_field(name="+lookup", value="Looks through over 9 milion dbs to search for a usernames data", inline=False)
    embed.add_field(name="+whois", value="Sends a discord accounts info [+whois @user]", inline=False)
    embed.add_field(name="+dm", value="Sends a dm to a certain user [+dm @user]", inline=False)
    embed.add_field(name="+ban", value="Bans a certain user out of the server [admin only]", inline=False)
    embed.add_field(name="+kick", value="Kicks a certain user out of the server [admin only]", inline=False) 
    embed.add_field(name="+unban", value="Unbans a certain user that has been banned [admin only]", inline=False)  
    embed.add_field(name="+addrole", value="Adds a specefied role to a certain user [admin only]", inline=False)
    embed.add_field(name="+remrole", value="Removes a specefied role from a certain user [admin only]", inline=False)     
    embed.add_field(name="+ping", value="Sends the ping of the bot", inline=False)   
    embed.add_field(name="+question", value="Answers a question [+question yourquestion]", inline=False)                           
    embed.add_field(name="+info", value="Sends info about the bot", inline=False) 
    await ctx.send(embed=embed)

@client.command()
async def http(ctx):
    f = open("Data/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/http-proxies.txt"))

@client.command()
async def https(ctx):
    f = open("Data/https-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/https-proxies.txt"))

@client.command()
async def socks4(ctx):
    f = open("Data/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/socks4-proxies.txt"))

@client.command()
async def socks5(ctx):
    f = open("Data/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/socks5-proxies.txt"))

@client.command()
async def all(ctx):
    f = open("Data/all-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/all-proxies.txt"))

    
init(convert=True)
os.system("title EmailSpammer!")
config = ConfigParser()

config.read('cfg.ini')

emale = config.get('SETTINGS', 'email')
pas = config.get('SETTINGS', 'password')

def type(words):
    words
    for char in words:
        time.sleep(0.001)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

@client.event
async def on_ready(): 
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} Servers / Add me to your server: criminals.life/bots / +help / Developed By rookie?#1337"))
count = 10
@client.command()
async def email(ctx,count=None,bomb_email=None,*,message=None):
    if count == None or bomb_email == None or message == None:
        await ctx.send("Format - +email [count] [email] [message] - e.g +email 10 email@email.com lol!")
    else:
        x = int(count)
    if x > 50:
        await ctx.send("`That's a lot. Do 50 or less!`")
    else:
        currentDT = datetime.datetime.now()
        hour = str(currentDT.hour)
        minute = str(currentDT.minute)
        second = str(currentDT.second)
        print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} [Command used] - {ctx.author.name}#{ctx.author.discriminator}:{Fore.RESET} !email {count} {bomb_email} {message}")
        counting = int(0)
        embed=discord.Embed(title=f"{counting}/{count}", url="https://github.com/9xc", color=0xff0000)
        embed.set_author(name="Email sent!", url="https://github.com/9xc")
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
        embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        msg = await ctx.send(embed=embed)
        for i in range(x):
            mail = smtplib.SMTP('smtp-relay.sendinblue.com',587,)
            mail.ehlo()
            mail.starttls()
            mail.login(emale,pas)
            mail.sendmail(emale,bomb_email,message)
            mail.close() 
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Message Sent:{Fore.RESET} {message} {Fore.GREEN}To {Fore.RESET}{bomb_email}")
            counting = counting + 1
            embed=discord.Embed(title=f"{counting}/{count}", url="https://github.com/9xc", color=0xff0000)
            embed.set_author(name="Email sent!", url="https://github.com/9xc")
            embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
            embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
            await msg.edit(embed=embed)
        embed=discord.Embed(title="Please consider following!", url="https://github.com/9xc", color=0xff0000)
        embed.set_author(name="Done spamming!", url="https://github.com/9xc")
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
        await msg.edit(embed=embed)
        
@client.command()
async def info(ctx):
    aboutem = discord.Embed(
        title="Some Info About ILLUMINATI :)",
        description="Languages: Python\nVersion: 1.0 \nChangelog: Added Addrole/Remrole Command\nDeveloper: rookie?1337",
        color=discord.Colour.dark_purple()
    )
    await ctx.send(embed = aboutem)
    
@client.command()
async def socials(ctx):
    aboutem = discord.Embed(
        title="Rookies Socials :)",
        description="Twitter: @rookiethagawd\nTikTok: @rookiethegod\nGithub: @9xc\nDiscord: rookie?1337",
        color=discord.Colour.dark_purple()
    )
    await ctx.send(embed = aboutem)
    
@client.command()
async def bypass(ctx, arg):
  r=requests.get('https://bypass.bot.nu/bypass2?url='+arg)
  a = ('%'+r.text)
  chunks = a.split(',')
  dest = chunks[1]
  stripped = dest.split('"')
  #await ctx.send(chunks[1])
  embed = discord.Embed()
  embed.set_thumbnail(url="https://thumbs.gfycat.com/PlainHonestAzurevase-size_restricted.gif")
  embed.add_field(name="Bypassed Link:", value=stripped[3], inline=False)
  await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

@client.command()
async def lookup(ctx, username = None):
    waitem = discord.Embed(
        title="Searching info...",
        description=f"PS, If i dont reply it means that the user has over 6000 Words As A response",
        color=discord.Colour.dark_purple()
    )
    msg = await ctx.reply(embed = waitem)
    if username == None:
        ws = discord.Embed(
            title="Error!",
            description=f"Please Enter A Valid Alias. Dont Leave Blank",
            color=discord.Colour.dark_purple()
        )
        await msg.edit(embed = ws)
    else:
        apireq = requests.get(f"https://api.weleakinfo.to/api?value={username}&type=email&key=YOURAPIKEY")
        status = apireq.json()['success']
        
        if status == False:
            ws = discord.Embed(
                title="Error!",
                description=f"Couldnt Find Anything, Sorry...",
                color=discord.Colour.dark_purple()
            )
            await msg.edit(embed = ws)
        else:
            infoamount = apireq.json()['found']
            resultap = apireq.json()['result']
            complete = discord.Embed(
                title = "Complete, Read Below...",
                description=f"Found {infoamount} Things About **{username}**\n\n```{resultap}```",
                color=discord.Colour.dark_purple()
            )
            await msg.edit(embed = complete)

@client.command(name="whois")
async def whois(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"Info on - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Highest Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)
    
@commands.has_permissions(administrator=True)   
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member.mention} has been banned for the Reason: **{reason}**.')
    
@commands.has_permissions(administrator=True)       
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)   
    
@commands.has_permissions(administrator=True)     
@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} Has been unbanned.')
            return
                  
@client.command()
async def purge(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)

@client.command()
async def cls(ctx, amount=35):
    await ctx.channel.purge(limit=amount)
        
@client.command()
async def dm(ctx, user: discord.User, *, msg):
    await ctx.send('Sent DM successfully')
    await user.send(f'{msg}')

@client.command()
async def addrole(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)
        await ctx.send(f"{user.mention} Has recieved the role {role.mention}.")
        
@client.command()
async def remrole(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.remove_roles(role)
        await ctx.send(f"{user.mention} Has had the role {role.mention} taken from him.")

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')
    
@client.command()
async def question(ctx, *, question):
    responses = ['Yes.',
                 'No.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')            
                          
client.run(token)
