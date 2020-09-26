import telebot


TOKEN = '1242505038:AAFSTM_EH0ToKos8kUNTthbcn_-m9nj-aX4'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) #rabotaet
def start_handler(message):
    bot.send_message(message.chat.id, "Привет, пользователь! Чтобы увидеть список всех команд напиши /help")


@bot.message_handler(commands=['help']) #rabotaet
def help_handler(message):
    bot.send_message(message.from_user.id, "/help - вывод набора всех команд \n /new_item - добавление нового задания \n /delete (?) - удаление задания под индексом (?) \n /all - вывод списка всех заданий")

@bot.message_handler(commands=['new_item'])
def task_handler(message):
    sent = bot.send_message(message.chat.id, 'Какое новое задание?') #rabotaet
    bot.register_next_step_handler(sent, hello)

def hello(message):
    text = message.text
    open('tasks_1.txt', 'a').write(text+' \n')
    read_object = open('tasks_1.txt', 'r')
    write_object = open('tasks_2.txt', 'a')
    for idx, line in enumerate(read_object, start=1):
        write_object.write('{} {}'.format(str(idx)+'.', line))
    bot.send_message(message.chat.id, 'Задание добавлено. Его номер -'+str(idx)+'.')
    read_object.close()



@bot.message_handler(commands=['delete'])
def remover_handler(message):
    sent = bot.send_message(message.chat.id, 'Напишите номер с точкой (между номером и точкой не должно быть пробела) того задания, которое хотите удалить')
    bot.register_next_step_handler(sent, hi)

def hi(message):
    str_0 = message.text
    with open("tasks_2.txt", "r") as f:
        lines = f.readlines()
    with open("tasks_2.txt", "w") as f:
        for line in lines:
            if line[0:len(str_0)] != str_0:
                f.write(line)
    bot.send_message(message.chat.id, 'Задание удалено')
    f.close()

@bot.message_handler(commands=['all'])     #normal'no rabotaet
def look_trough_list_handler(message):
    f = open('tasks_2.txt')
    bot.send_message(message.from_user.id, 'Вот список ваших дел - \n' + f.read())



bot.polling()




















