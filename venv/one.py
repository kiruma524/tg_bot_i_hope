import telebot

TOKEN = '1242505038:AAFSTM_EH0ToKos8kUNTthbcn_-m9nj-aX4'

bot = telebot.TeleBot(TOKEN)

tasks = []

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, "Привет, пользователь!")


@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, "Могу ответить на /start, /help, /new_item, /delete, /all")

@bot.message_handler(commands=['new_item '])
def task_handler(task):
    task = message.get('text')
    task = tasks.append(task)
    task_id = tasks.index(task)
    bot.send_message(message.from_user.id, "Задание "+task+" было добавлено. Его id - "+task_id)

@bot.message_handler(commands=['delete'])
def remover_handler(task_number):
    task_number=message.get('text')
    task_number=int(task_number)
    for i in range(0, len(tasks)):
        if tasks[task_number]==tasks[i]:
            tasks.remove(tasks[i])

@bot.message_handler(commands=['all'])
def look_trough_list_handler(message):
    bot.send_message(message.from_user.id, 'Вот список ваших дел - \n', tasks)


bot.polling()

