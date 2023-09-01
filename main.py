# -*- coding: utf-8 -*-
"""
New project

Date: 13/08/2023

Name of project: Krill lotin bot

Created by Sardorbek Khamrakulov
"""
from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "API_TOKEN"
bot = telebot.TeleBot(TOKEN, parse_mode=None) 


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Hi user welcome to Крилл-Lotin bot🤖🤖🤖"
    javob += "\nEnter the word:"
    bot.reply_to(message, javob)

@bot.message_handler(commands=['help'])
def send_help(message):
    question = """ 
    Hi👋 I'm Крилл-Lotin bot!!!\nIf you include words in the krill\nAlphabet in me I will turn it into the\nLatin alphabet if you send me a word in the\nLatin alphabet I will turn it into the krill Alphabet🤖🌐🤖
    """
    bot.reply_to(message, question)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)  
    bot.reply_to(message, f"Translation: {javob(msg)}")

bot.polling()