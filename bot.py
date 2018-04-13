import discord
import asyncio
from blabla import speak
from bitcoin import btcprice
import DnD



commands = ['btcprice','cube','newgame','addpers','heroes','char','change','exit','help']
dictionary = {
    'btcprice': btcprice,
    'cube': DnD.cube,
    'newgame': DnD.newgame,
    'addpers':DnD.newPlayer,
    'heroes':DnD.heroes,
    'char': DnD.outChar,
    'change':DnD.addChar,
    'exit': DnD.end,
    'help': DnD.help
    }

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event



async def on_message(message):
    myname = '<@' +client.user.id +'> '
    msg = str(message.content)
    if msg.startswith(myname):
        if '.' in msg:
            com = msg[msg.index('!') + 1: msg.index('.')]
            msg = msg[msg.index('.') + 1:]
        elif '!' in msg:
            com = msg[msg.index('!') + 1:]
        else:
            com = msg[msg.index('>') + 1:]
        if com in commands:
            try:
                oper = dictionary[com]
                text = oper(msg)
            except:
                text = speak(com)
        else:
            text = speak(com)
        await client.send_message(message.channel, text)




print('input token:')
DISCORD_BOT_TOKEN = input()
client.run(DISCORD_BOT_TOKEN)