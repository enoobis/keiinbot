import os
import logging
import telebot
from telebot import types
from keep_alive import keep_alive

# Your lesson schedule data
schedule = {
    "monday": [
        "1) 09:10 - 10:30: Software Development by Prof. Tonoeva (Room 401)",
        "2) 10:40 - 12:00: Software Development by Prof. Tonoeva or Database by Prof. Beisheev (Room 401)",
        "3) 12:30 - 13:50: Database by Prof. Beisheev (Room 401)",
        "4) 14:00 - 15:20: No Lesson",
    ],
    "tuesday": [
        "1) 09:10 - 10:30: No Lesson",
        "2) 10:40 - 12:00: No Lesson",
        "3) 12:30 - 13:50: Life Safety by Prof. Usenkanov (Room 304)",
        "4) 14:00 - 15:20: Computer Networks by Prof. Beisheev (Room 411)",
    ],
    "wednesday": [
        "1) 09:10 - 10:30: JAVA Programming by Prof. Musaev (Room 411)",
        "2) 10:40 - 12:00: Operating Systems by Prof. Musaev (Room 411)",
        "3) 12:30 - 13:50: Operating Systems by Prof. Musaev or Metrology by Prof. Alykulova (Room 401)",
        "4) 14:00 - 15:20: Metrology by Prof. Alykulova (Room 104)",
    ],
    "thursday": [
        "1) 09:10 - 10:30: No Lesson",
        "2) 10:40 - 12:00: No Lesson",
        "3) 12:30 - 13:50: No Lesson",
        "4) 14:00 - 15:20: No Lesson",
    ],
    "friday": [
        "1) 09:10 - 10:30: Mobile Development by Prof. Tonoeva (Room 401)",
        "2) 10:40 - 12:00: No Lesson or Software Quality Assurance by Prof. Tonoeva (Room 401)",
        "3) 12:30 - 13:50: OOP by Prof. Park Youngho (Room 401)",
        "4) 14:00 - 15:20: No Lesson",
    ],
    "monday@keiin_bot": [
        "1) 09:10 - 10:30: Software Development by Prof. Tonoeva (Room 401)",
        "2) 10:40 - 12:00: Software Development by Prof. Tonoeva or Database by Prof. Beisheev (Room 401)",
        "3) 12:30 - 13:50: Database by Prof. Beisheev (Room 401)",
        "4) 14:00 - 15:20: No Lesson",
    ],
    "tuesday@keiin_bot": [
        "1) 09:10 - 10:30: No Lesson",
        "2) 10:40 - 12:00: No Lesson",
        "3) 12:30 - 13:50: Life Safety by Prof. Usenkanov (Room 304)",
        "4) 14:00 - 15:20: Computer Networks by Prof. Beisheev (Room 411)",
    ],
    "wednesday@keiin_bot": [
        "1) 09:10 - 10:30: JAVA Programming by Prof. Musaev (Room 411)",
        "2) 10:40 - 12:00: Operating Systems by Prof. Musaev (Room 411)",
        "3) 12:30 - 13:50: Operating Systems by Prof. Musaev or Metrology by Prof. Alykulova (Room 401)",
        "4) 14:00 - 15:20: Metrology by Prof. Alykulova (Room 104)",
    ],
    "thursday@keiin_bot": [
        "1) 09:10 - 10:30: No Lesson",
        "2) 10:40 - 12:00: No Lesson",
        "3) 12:30 - 13:50: No Lesson",
        "4) 14:00 - 15:20: No Lesson",
    ],
    "friday@keiin_bot": [
        "1) 09:10 - 10:30: Mobile Development by Prof. Tonoeva (Room 401)",
        "2) 10:40 - 12:00: No Lesson or Software Quality Assurance by Prof. Tonoeva (Room 401)",
        "3) 12:30 - 13:50: OOP by Prof. Park Youngho (Room 401)",
        "4) 14:00 - 15:20: No Lesson",
    ],
}

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the bot with your API token
my_secret = os.environ['TOKEN']
bot = telebot.TeleBot(my_secret)

# Create a custom keyboard menu
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.row(types.KeyboardButton('/monday'),
                  types.KeyboardButton('/tuesday'))
menu_keyboard.row(types.KeyboardButton('/wednesday'),
                  types.KeyboardButton('/thursday'))
menu_keyboard.row(types.KeyboardButton('/friday'))
menu_keyboard.row(types.KeyboardButton('/current'))
menu_keyboard.row(types.KeyboardButton('/all'))


# Handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(
      message.chat.id,
      "This bot was made by '@enoobis' - '@enoobis_org'. Powered by Telegram Bot API.\nfull code : https://replit.com/@enoobis1/keiinbot",
      reply_markup=menu_keyboard)


# Handle menu button clicks
@bot.message_handler(
    commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
def show_lessons(message):
  day = message.text[1:]  # Remove the slash from the command
  if day in schedule:
    lessons = "\n".join(schedule[day])
    bot.send_message(
        message.chat.id,
        f"Here are the lessons for {day.capitalize()}:\n{lessons}")
  else:
    bot.send_message(message.chat.id,
                     "Invalid day. Please choose a valid day of the week.")


# Handle menu button clicks
@bot.message_handler(commands=[
    'monday@keiin_bot', 'tuesday@keiin_bot', 'wednesday@keiin_bot',
    'thursday@keiin_bot', 'friday@keiin_bot'
])
def show_lessons2(message):
  day = message.text[1:]  # Remove the slash from the command
  if day in schedule:
    lessons = "\n".join(schedule[day])
    bot.send_message(
        message.chat.id,
        f"Here are the lessons for {day.capitalize()}:\n{lessons}")
  else:
    bot.send_message(message.chat.id,
                     "Invalid day. Please choose a valid day of the week.")


# Handle the /current command (hardcoded for simplicity)
@bot.message_handler(commands=['current'])
def show_current_lesson(message):
  # You can implement logic to determine the current lesson based on the current time.
  current_lesson = "No lesson currently."
  bot.send_message(message.chat.id, current_lesson)


# Handle the /all command to send an image
@bot.message_handler(commands=['all'])
def send_image(message):
  image_url = "https://media.discordapp.net/attachments/1042466060349222912/1150806093199581295/image.png?width=627&height=630"
  bot.send_photo(message.chat.id, image_url)


keep_alive()
# Start the bot
if __name__ == '__main__':
  bot.polling(none_stop=True)
