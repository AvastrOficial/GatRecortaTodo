import telebot
import requests
from bs4 import BeautifulSoup as bs4
from telebot import types

#--------------------------------------------------------------------------
TOKEN = input("[•]Ingresa El Token: ")
#-------------------------------------------------------------------------
bot = telebot.TeleBot(TOKEN)
#------------------------------------------------------------------------#
#    • Telegram:                                                      #
#                                                                              #
# • Canal : @BoxPrey                                           #
#                                                                             #
# • By : @PreBoyx                                                #
#----------------------------------------------------------------------#


def acortar_url(original_url, personalization=None):
    api_url = f'https://is.gd/create.php?format=json&url={requests.utils.quote(original_url)}'

    if personalization:
        api_url += f'&shorturl={requests.utils.quote(personalization)}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()

        if 'shorturl' in data:
            return data["shorturl"]
        else:
            return "💢𝐄𝐫𝐫𝐨𝐫 𝐚𝐥 𝐚𝐜𝐨𝐫𝐭𝐚𝐫 𝐥𝐚 𝐔𝐑𝐋. 𝐃𝐞𝐭𝐚𝐥𝐥𝐞𝐬:", data
    except requests.exceptions.RequestException as e:
        return f"💢𝐄𝐫𝐫𝐨𝐫 𝐞𝐧 𝐥𝐚 𝐬𝐨𝐥𝐢𝐜𝐢𝐭𝐮𝐝: {e}"
    except ValueError as e:
        return f"💢𝐄𝐫𝐫𝐨𝐫 𝐚𝐥 𝐩𝐫𝐨𝐜𝐞𝐬𝐚𝐫 𝐥𝐚 𝐫𝐞𝐬𝐩𝐮𝐞𝐬𝐭𝐚: {e}"
    

@bot.message_handler(commands=['start'])
def start(message):
    
    keyboard = types.InlineKeyboardMarkup()
    button_github = types.InlineKeyboardButton("𝐆𝐢𝐭𝐡𝐮𝐛 🌑", url="https://github.com/Preboyx") 
    button_telegram = types.InlineKeyboardButton("𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 🌪", url="https://t.me/Preboyx")
    keyboard.add(button_github, button_telegram)

    
    image_url = "https://telegra.ph/file/27903c92e662da443763c.jpg"
    bot.send_photo(message.chat.id, image_url, caption=''' » 𝐄𝐧𝐦𝐚𝐬𝐜𝐚𝐫𝐨 𝐔𝐑𝐋𝐬 𝐲 𝐭𝐞 𝐝𝐨𝐲 𝐞𝐥 𝐜𝐨𝐧𝐭𝐫𝐨𝐥 𝐩𝐚𝐫𝐚 𝐩𝐞𝐫𝐬𝐨𝐧𝐚𝐥𝐢𝐳𝐚𝐫𝐥𝐚𝐬. 🖇

» 𝐄𝐥𝐢𝐠𝐞 𝐮𝐧 𝐧𝐨𝐦𝐛𝐫𝐞 𝐨 𝐭𝐞𝐱𝐭𝐨 𝐩𝐚𝐫𝐚 𝐭𝐮 𝐔𝐑𝐋 𝐞𝐧𝐦𝐚𝐬𝐜𝐚𝐫𝐚𝐝𝐚.🪄''', reply_markup=keyboard)
    bot.reply_to(message, "💨𝐄𝐧𝐯𝐢́𝐚𝐦𝐞 𝐮𝐧𝐚 𝐔𝐑𝐋 𝐩𝐚𝐫𝐚 𝐚𝐜𝐨𝐫𝐭𝐚𝐫𝐥𝐚:")
    bot.register_next_step_handler(message, pedir_personalizacion)

def pedir_personalizacion(message):
    original_url = message.text
    if original_url.startswith("https://") or original_url.startswith("http://"):
        bot.reply_to(message, "🥀𝐈𝐧𝐠𝐫𝐞𝐬𝐞 𝐞𝐥 𝐧𝐨𝐦𝐛𝐫𝐞 𝐩𝐞𝐫𝐬𝐨𝐧𝐚𝐥𝐢𝐳𝐚𝐝𝐨 𝐩𝐚𝐫𝐚 𝐥𝐚 𝐔𝐑𝐋 (𝐨𝐩𝐜𝐢𝐨𝐧𝐚𝐥):")
        bot.register_next_step_handler(message, acortar_url_con_personalizacion, original_url)
    else:
        bot.reply_to(message, "📌𝐏𝐨𝐫 𝐟𝐚𝐯𝐨𝐫, 𝐞𝐧𝐯𝐢́𝐚 𝐮𝐧𝐚 𝐔𝐑𝐋 𝐯𝐚́𝐥𝐢𝐝𝐚.")

def acortar_url_con_personalizacion(message, original_url):
    personalization = message.text.strip()
    short_url = acortar_url(original_url, personalization)
    if isinstance(short_url, str):
        bot.reply_to(message, f"𝐔𝐫𝐥 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥𝐢𝐳𝐚𝐝𝐚 🪄: \n\n{short_url}\n\n✯ @PreyBox • @BoxPrey")
    else:
        bot.reply_to(message, short_url)

bot.polling(none_stop=True)