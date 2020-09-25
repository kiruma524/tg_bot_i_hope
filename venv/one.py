import telebot

TOKEN = '1242505038:AAFSTM_EH0ToKos8kUNTthbcn_-m9nj-aX4'

bot = telebot.TeleBot(TOKEN)

tasks_1 = []
tasks_2=[]

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет, пользователь!")


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, "Могу ответить на /start, /help, /new_item, /delete, /all")

@bot.message_handler(commands=['new_item '])
def task_handler(message):
    task = message.text
    tasks_1 = tasks_1.append(task)
    task_id = tasks_1.index(task)
    if len(tasks_1)>len(tasks_2):
        bot.reply_to_message(message.from_user.id, "Задание " + task + " было добавлено. Его id - " + task_id)
        tasks_2=tasks_1
    elif len(tasks_1)==len(tasks_2):
        bot.reply_to_message(message.from_user.id, "Ничего не было добавлено")


@bot.message_handler(commands=['delete'])
def remover_handler(message):
    task_number=message.get('text')
    task_number=int(task_number)
    for i in range(0, len(tasks)):
        if tasks[task_number]==tasks[i]:
            tasks.remove(tasks[i])

@bot.message_handler(commands=['all'])     #normal'no rabotaet
def look_trough_list_handler(message):
    if len(tasks)==0:
        bot.send_message(message.from_user.id, 'Заданий нет')
    else:
        bot.send_message(message.from_user.id, 'Вот список ваших дел - \n', tasks)



bot.polling()

