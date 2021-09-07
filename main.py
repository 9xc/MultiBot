import requests
import discord
import discord,json,os,random
from discord import Embed, File
from discord.ext import commands
import time
import asyncio
import smtplib
import datetime
from configparser import ConfigParser
import os
import sys
from colorama import Fore, init

token = "YOUR BOT TOKEN"

client = commands.Bot(command_prefix='+')
client.remove_command('help')
            
@client.command()
async def help(ctx):
    embed = Embed(title="All Commands", description=None)
    embed.add_field(name="+help", value="Displays all available commands", inline=False)
    embed.add_field(name="+http", value="Sends fresh http proxy list", inline=False)
    embed.add_field(name="+https", value="Sends fresh https proxy list", inline=False)
    embed.add_field(name="+socks4", value="Sends fresh socks4 proxy list", inline=False)
    embed.add_field(name="+socks5", value="Sends fresh socsk5 proxy list", inline=False)
    embed.add_field(name="+all", value="Sends fresh http, https, socks4 and socks5 proxy list", inline=False)
    embed.add_field(name="+email", value="Format - +email [count] [email] [message] - e.g +email 10 email@email.com lol!", inline=False)
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
    await client.change_presence(activity = discord.Streaming(name="MultiBot", url="https://www.twitch.tv/egirlraper"))
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
        embed=discord.Embed(title=f"{counting}/{count}", url="https://github.com/egirlraper", color=0xff0000)
        embed.set_author(name="Email sent!", url="https://github.com/egirlraper")
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
        embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
        msg = await ctx.send(embed=embed)
        for i in range(x):
            mail = smtplib.SMTP('smtp.gmail.com',587,)
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
            embed=discord.Embed(title=f"{counting}/{count}", url="https://github.com/egirlraper", color=0xff0000)
            embed.set_author(name="Email sent!", url="https://github.com/egirlraper")
            embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
            embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
            embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
            await msg.edit(embed=embed)
        embed=discord.Embed(title="Please consider following!", url="https://github.com/egirlraper", color=0xff0000)
        embed.set_author(name="Done spamming!", url="https://github.com/egirlraper")
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/gmail-30-722694.png")
        await msg.edit(embed=embed)
        
  
             
client.run(token)