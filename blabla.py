import apiai, json

def speak(text):
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

