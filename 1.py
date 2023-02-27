import telebot as tb
import turtle as tr
import random as rd
from telebot import types 
Token = '6138040690:AAEDnK8ntamcKR0d4KZLfQwXWVO6YceEqc0'
bot = tb.TeleBot(Token)
@bot.message_handler(commands=['Design'])
def turtle_1():
    wn=tr.Screen()
    wn.setup(600,600)
    s=tr.Turtle()

    r=10
    for i in range(200):
        s.circle(r+i,45)
        j=rd.random()
        k=rd.random()
        l=rd.random()
        s.pencolor((j,k,l))
    s.penup()
    s.home()
    s.pendown()

    m=20
    for i in range(200):
        s.circle(m+i,45)
        j=rd.random()
        k=rd.random()
        l=rd.random()
        s.pencolor((j,k,l))
    s.penup()
    s.home()
