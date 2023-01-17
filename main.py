import telebot
from telebot import types
import parser
import parser_cat
import token


bot = telebot.TeleBot(token.token)

current = 0
current_cat = ""
products = []


def next_elem():
    print(f"products- {products}")
    if current >= 0:
        return products[current]
    # products = []


def prev_elem():
    print(f"products- {products}")
    if current <= len(products):
        return products[current]
    # products = []



def message_create(message, args):
    markup = types.InlineKeyboardMarkup(row_width=2)
    prev = types.InlineKeyboardButton('Previous', callback_data="previous")
    next = types.InlineKeyboardButton("Next", callback_data="next")
    back = types.InlineKeyboardButton("Select category", callback_data="category")
    markup.add(prev, next, back)
    bot.send_photo(message.chat.id, args[1], args[0], reply_markup=markup)


@bot.message_handler(commands=["starts"])
def start(message):
    categories(message)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    global current
    if call.message:
        if call.data == "previous":
            current -= 1
            message_create(call.message, prev_elem())
        if call.data == "next":
            current += 1
            message_create(call.message, next_elem())
        if call.data == "category":
            categories(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.message_handler(content_types=["text"])
def messages(message):
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Here', reply_markup=a)
    global products
    # print(current_cat)
    products = parser.pars(current_cat.get(message.text))
    message_create(message, next_elem())

def categories(message):
    current = 0
    products = []
    print(f"Products categories - {products}")
    current_cat = parser_cat.buttons()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.InlineKeyboardButton(text=x, callback_data=x) for _, x in enumerate(current_cat)]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, text="Select category", reply_markup=keyboard)

bot.polling()


