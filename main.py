import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

organik = ["daun", "sayur", "kulit pisang ambon", "kertas"]
anorganik = ["plastik", "besi", "kabel"]

@bot.command()
async def pilih(ctx):
    await ctx.send("masukkan sampah")

    msg = await bot.wait_for("message")
    
    if msg.content in organik:
        await ctx.send("masukkan kedalam sampah organik")
    else:
        await ctx.send("masukkan ke dalam sampah anorganik")

bot.run("MTExMDU2MDE3MDY3ODk0Mzg0Ng.G1A0H3.NvXrQXKrVY4xsytnj_EpZrmQgefUaHI9YihcJY")