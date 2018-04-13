import discord
import asyncio
import requests
import apiai, json
import random




BTC_PRICE_URL_coinmarketcap = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=RUB'
commands = ['!btcprice','!cube','!newgame','!addpers','!print']

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event

async  def output(message,text):
    await client.send_message(message.channel, text)

async def on_message(message):
    print(message)
    myname = '<@' +client.user.id +'> '
    if message.content.startswith(myname + '!btcprice'):
        print('[command]: btcprice ')
        btc_price_usd, btc_price_rub = get_btc_price()
        msg = 'USD: ' + str(btc_price_usd) + ' | RUB: ' + str(btc_price_rub)
        await client.send_message(message.channel, msg)
    elif message.content.startswith(myname + '!cube'):
        msg = str(random.randint(1, 32))
        await client.send_message(message.channel, msg)
    elif message.content.startswith(myname):
        msg = str(message.content)
        msg = msg.replace('!','')
        print(msg[msg.index('>')+1:])
        msg = blabla(str(msg)[msg.index('>')+1:])
        await client.send_message(message.channel, msg)




def get_btc_price():
    r = requests.get(BTC_PRICE_URL_coinmarketcap)
    response_json = r.json()
    usd_price = response_json[0]['price_usd']
    rub_rpice = response_json[0]['price_rub']
    return usd_price, rub_rpice

def blabla(text):
    request = apiai.ApiAI('9b668a0f80e4447aba99ee0e2f73adf1').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = 'BatlabAIBot' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = text # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        return (response)
        #bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        return ('Я Вас не совсем понял!')
        #bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')

print('input token:')
DISCORD_BOT_TOKEN = input()
client.run(DISCORD_BOT_TOKEN)