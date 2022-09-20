"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, settings
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Привет! Будь добр введи команду /planet и любое название планеты на английском'
    print(text)
    update.message.reply_text(text)


def planet_user(update, context):
    user_says = update.message.text
    planet = user_says.split()
    top_planet = getattr(ephem,planet[1].capitalize())()
    print(top_planet)
    mars = ephem.Mars(date.today())
    print(mars)
    b = ephem.constellation(mars)
    print (b)
    a = ephem.constellation(top_planet)
    print (a)
    update.message.reply_text(a)




    

def main():
    mybot = Updater(settings.APY_KEY, use_context=True)
    
    dp = mybot.dispatcher
    print('https://t.me/planet_ephem1_bot')
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_user))
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
