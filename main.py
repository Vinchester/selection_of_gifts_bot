import telebot
from telebot import types
import parser_prod
import parser_cat
import token_bot


bot = telebot.TeleBot(token_bot.token)
categories = parser_cat.buttons()

current_position = 0
products = []
chosen_category = ""


@bot.message_handler(commands=["start"])
def start(message):
    """Start function, when user sends '/start'"""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.InlineKeyboardButton(text=x, callback_data=x)
               for _, x in enumerate(categories)]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, text="Select category", reply_markup=keyboard)


def card_create(message):
    """Function for creation of card(responding message)"""
    elem = products[current_position]
    markup = types.InlineKeyboardMarkup(row_width=2)
    prev_but = types.InlineKeyboardButton('Previous', callback_data="previous")
    next_but = types.InlineKeyboardButton("Next", callback_data="next")
    back_but = types.InlineKeyboardButton("Select category", callback_data="category")
    markup.add(prev_but, next_but, back_but)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_photo(message.chat.id, elem[1], elem[0], reply_markup=markup)


@bot.message_handler(content_types=["text"])
def message_(message):
    """Function to process any text sent by the user"""
    global products
    if message.text in [x for _, x in enumerate(categories)]:
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id, 'Here you are', reply_markup=a)
        products = parser_prod.parsing(categories.get(message.text))
        card_create(message)
    else:
        bot.send_message(message.chat.id, text="You have typed something wrong!")


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    """Function to process 'callback_data' from InlineKeyboardButtons"""
    global current_position
    if call.message:
        match call.data:
            case "previous":
                current_position -= 1
                card_create(call.message)
            case "next":
                current_position += 1
                card_create(call.message)
            case "category":
                start(call.message)


bot.polling()
#DeFakto
