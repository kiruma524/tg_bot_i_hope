# Телеграм-бот 'What to do?'


## Что это такое?

'What to do?' - простенький телеграм-бот, выполняющий функцию to-do листа. 

## Какие функции?

1) /start - самая первая команда, с которой начинается работа бота.
2) /help - набрав эту команду, выведится список всех функций, которые может выполнить бот.
3) /new_item - команда, с помощью которой юзер может добавить новый пункт в список дел.
4) /all - вывод всего списка дела пользователя.
5) /delete - функция 'вычеркивания' из списка задания, которое пользователь выполнил/не успел сделать/другое.

## Как работает?

Общий концепт работы такой: пользователь отправляет сообщения с заданиями для себя. Эти сообщения в определенном формате сохраняются в текстовом файле tasks.txt. 
Позже, по команде юзера, список всех дел может выводиться целиком или же редактироваться.

## Какие минусы в моей работе, в моем коде?

1) Индекс, после несколько добавлений новых заданий, начинает 'вливаться' в строку.
2) Очень важно, чтобы пользователь удалял здания, начиная с конца списка, иначе последующие удаления каких-либо задач из списка будут работать неправильно (следствие из первого пункта).
3) Нет базы данных, из-за чего задания нескольких пользователей могут смешиваться, если код запускается для двоих юзеров с одного устройства.
4) Часто приходится удалять и заново делать файл tasks.txt
