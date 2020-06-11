# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:36:48 2020

@author: User
"""

from telegram.ext import Updater, InlineQueryHandler, CommandHandler,MessageHandler, Filters
import requests
import logging

token = '1207250218:AAEDAQ82sE5MkbDDTk9R4-yzSMgfPIsEjhI'

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

#def bop(bot, update):
def bop(update, context):
#    url = get_url()
#    chat_id = update.message.chat_id
#    bot.send_photo(chat_id=chat_id, photo=url)
#    bot.send
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=get_url())
    
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry can speakerh Engrish? Or maybe it is just not true...")
    
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me! \n Available Functions are: \n\n 1) /start \n 2) /bop \n 3) /caps <- type this first then type your msg for eg. type this -> \n    /cap i am cool!   > \n\n 4) /iamcool \n\n\n\n 5) /clickthislast ")
    for i in range(600):
        print(None)
    context.bot.send_message(chat_id=update.effective_chat.id, text="This bot is still beta so help me test out the functions! THANKS")
    
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def birthdays(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welfaries' Birthday Dates: \n joekee 5 jan \n gorden 6 jan \n bao 14 jan \n xinmin 7 feb \n charlotte 19 feb \n  \n eleana 23 feb \n ben 27 feb \n xinyi 7 march \n suying 9 april \n jun an 22 april \n paulie & nadia 26 may \n harry 27 may\n rachel 6 june \n gabriel 1 sep \n zhiwei 9 oct \n siti 4 nov \n wellace 29 nov \n kenzie 4 dec \n erika 31 dec ")

def clickthislast(update, context):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="The other msgs were just a scam")
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is the real msg wait for it....")
    for i in range(1000):
        print(None)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('cake.jpg', 'rb'))
    for i in range(500):
        print(None)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('HappyBirthday.jpg', 'rb'))
    for i in range(200):
        print(None)
    context.bot.send_message(chat_id=update.effective_chat.id, text="A Big Happy Birthday from Welfare Comm to Nadia and Paulie!!!!!!!!!!!!!")
    contents = requests.get('https://random.dog/woof.json').json()    
    for i in range(700):
        print(None)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=contents['url'])
    for i in range(1000):
        print(None)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pls Don't share this bot with the others cause its supposed to be a surprise for the rest")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pls rmbr/remind me of these peep's birthday: \n joekee 5 jan \n gorden 6 jan \n bao 14 jan \n xinmin 7 feb \n charlotte 19 feb \n eleana 23 feb \n ben 27 feb \n xinyi 7 march \n suying 9 april \n jun an 22 april \n paulie & nadia 26 may \n harry 27 may\n rachel 6 june \n gabriel 1 sep \n zhiwei 9 oct \n siti 4 nov \n wellace 29 nov \n kenzie 4 dec \n erika 31 dec ")
    for i in range(1000):
        print(None)
    context.bot.send_message(chat_id=update.effective_chat.id, text="if you wanna see the dates again next time just type in /birthdays")
    context.bot.send_message(chat_id=update.effective_chat.id, text="FULL AVAILABLE Functions are: \n\n 1) /start \n 2) /bop \n 3) /caps <- type this first then type your msg for eg. type this -> \n <   '/cap i am cool!'   > \n 4) /iamcool \n 5) /clickthislast \n 6) /birthdays ")
    
def main():
    updater = Updater(token, use_context = True)
    dp = updater.dispatcher
    ########Start
    dp.add_handler(CommandHandler('start', start))
    ########BOP    
    dp.add_handler(CommandHandler('bop',bop))
    #######Caps
    dp.add_handler(CommandHandler('caps', caps))
    ########last
    dp.add_handler(CommandHandler('clickthislast',clickthislast))
    ########Birthdays
    dp.add_handler(CommandHandler('birthdays',birthdays))

    ##########Unknown
    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)
#    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    