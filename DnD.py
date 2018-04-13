import random

commands = ['!btcprice','!cube','!newgame','!addpers','!print']

char = ['Имя','Класс','hp','Сила','Ловкость','Красноречие','Интеллект']
chars =[] #персонажи с классами
players = [] #имена игроков

def newgame(msg):
    return ('Создайте персонажей, указав через запятую Имя,Класс,hp,Силу,Ловкость,Красноречие,Интеллект')
def cube(msg):
    msg = str(random.randint(1, 32))
    return (msg)

def newPlayer(msg):

    msg = msg.split(',')
    player=[]
    for i in range(len(msg)):
        player.append(msg[i])
    chars.append(player)
    players.append(msg[0])
    return ('персонаж создан')

def outChar(msg):
    i = players.index(msg)
    print(players[i])
    return ('Имя: '+ chars[i][0] + '\nКласс: '+ chars[i][1] + '\nhp: '+
            chars[i][2] + '\nСила: '+ chars[i][3] + '\nЛовкость: '+
            chars[i][4] + '\nКрасноречие: '+ chars[i][5] + '\nИнтеллект: '+ chars[i][6])

def addChar(msg):
    msg = msg.split(',')
    name = msg[0]
    word = msg[1]
    delta = msg[2]
    i = players.index(name)
    j = char.index(word)
    chars[i][j]= str(int(chars[i][j]) + int(delta))
    return(word +' = ' + chars[i][j])

def heroes(msg):
    msg = ''
    for i in range(len(players)):
        msg+=players[i]+' - ' + chars[i][1]+ '\n'
    print(msg)
    return msg

def end(msg):
    players.clear()
    chars.clear()
    return ('Игра окончена')
def help(msg):
    print(msg)
    if msg == '!btcprice':
        return ('!bcprice сообщит вам цену биткоина')
    elif msg == '!cube':
        return ('!cube [бросить кубик]')
    elif msg == '!newgame':
        return ('!newgame [создаст новую игру]')
    elif msg == '!addpers':
        return ('!addpers.Имя,Класс,hp,Сила,Ловкость,Красноречие,Интеллект [Добавит персонажа]')
    elif msg == '!heroes':
        return ('!heroes [выведет список персонажей]')
    elif msg == '!char':
        return ('!char [выведет характеристики персонажа]')
    elif msg == '!change':
        return ('!change.hp-5 [изменит hp на -5]')
    elif msg == '!exit':
        return ('!exit [завершит игру]')
    else:
        return ('Мой список команд: \n!btcprice - стоимость биткоина\n!cube - бросить кубик\n!newgame - новая игра\n'
           '!addpers - добавить нового персонажа\n!char - показать характеристики персонажа\n'
           '!change - изменить характеристику персонажа\n!exit - завершить игру\n'
                'Параметры команд передаются через запятую\n Команда, содержащая параметры заканчивается точкой')




    
