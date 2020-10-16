import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.'.format(
                         message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def print_message(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
