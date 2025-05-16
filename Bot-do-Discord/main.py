import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print('Bot inicializado com sucesso')

@bot.event
async def on_message(msg:discord.Message):
    if.msg.author.bot:
        return
    await msg.reply(f"O usuário {msg.author.metion} enviou uma mensagem no canaç {msg.channel.name}") 

@bot.commands()
async def ola(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Olá, {nome}! Tudo bem?")

"""

async def falar(ctx:commands.Context, *,texto):
    await ctx.send(texto)    
repete todo o texto que o usuario diz apos o comando ".falar"

ou 

async def falar(ctx:commands.Context, texto, argumento_2):
    await ctx.send(texto)   
    await ctx.send(argumento_2)
repete as duas primeiras silabas que o usuario diz apos o comando ".falar" uma abaixo da outra

"""
async def somar(ctx:commands.Context, num1:float, num2:float):
    resultado = num1 + num2
    await ctx.reply(f"A soma entre {num1} e {num2} é igual a {resultado}")

bot.run("")
