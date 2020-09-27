import telebot


TOKEN = <token>

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет, пользователь! Чтобы увидеть список всех команд напиши /help")


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, "/help - вывод набора всех команд \n /new_item - добавление нового задания \n /delete (?) - удаление задания под индексом (?) \n /all - вывод списка всех заданий")

@bot.message_handler(commands=['new_item'])
def task_handler(message):
    sent = bot.send_message(message.chat.id, 'Какое новое задание?')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    text = str(message.text)
    open('tasks.txt', 'a').write(text+' \n')

    read_object = open('tasks.txt', 'r+')
    write_object = open('tasks.txt', 'a')
    for idx, line in enumerate(read_object, start=1):
        write_object.write('{} {}'.format(str(idx) + '.', str(line)))
        read_object.truncate(0)

    bot.send_message(message.chat.id, 'Задание добавлено. Его номер -' + str(idx) + '.')
    read_object.close()



@bot.message_handler(commands=['delete'])
def remover_handler(message):
    sent = bot.send_message(message.chat.id, 'Напишите номер с точкой (между номером и точкой не должно быть пробела) того задания, которое хотите удалить')
    bot.register_next_step_handler(sent, hi)

def hi(message):
    str_0 = message.text

    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    with open("tasks.txt", "w") as f:
        for line in lines:
            if str_0 not in line:
                f.write(line)

    bot.send_message(message.chat.id, 'Задание удалено')
    f.close()

@bot.message_handler(commands=['all'])
def look_trough_list_handler(message):
    f = open('tasks.txt')
    if f !='':
        bot.send_message(message.chat.id, 'Вот список ваших дел - \n' +str(f.read()))
    else:
        bot.send_message(message.chat.id, 'Заданий нет')

bot.polling()




