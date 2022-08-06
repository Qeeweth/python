import telebot
import connection_db
from telebot import types
import queries
import save

bot = telebot.TeleBot('2087360344:AAE96QsdOR3Kv_uUCWhsBE9CIsQToKTmP-s')
pool = connection_db.init_connection_pool()
connection_db.create_tables(pool)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Slack Info')
    item2 = types.KeyboardButton('Confluence')
    item3 = types.KeyboardButton('SQL Requests')
    item4 = types.KeyboardButton('Servers')
    item5 = types.KeyboardButton('Other')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_messages(message):
    txt: str = message.text
    if txt.startswith('/add'):
        tag = txt[txt.index('/tag:’')+6: txt.index('’,')]
        info = txt[txt.index('/info:’')+7: len(txt)-2]
        save.save(pool, tag, info)
        bot.send_message(message.chat.id, "Успешно сохранено")
    else:
        info = queries.get_by_tag(pool, txt)
        for row in info:
            bot.send_message(message.chat.id, row[1])


bot.polling(none_stop=True)











