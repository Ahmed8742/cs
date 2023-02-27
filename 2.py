import telebot as tb
import turtle as tr
import random as rd
from telebot import types 
def turtle_2():
    wn=tr.Screen()
    wn.setup(600,600)
    wn.bgcolor("white")
    s=tr.Turtle()
    r=10

    for i in range(20):
        s.circle(r*i)
        s.penup()
        s.sety(r*i*-1)
        s.setx(r*i*-1)
        s.pendown()
        j=rd.random()
        k=rd.random()
        l=rd.random()
        s.pencolor((j,k,l))
    s.penup()
    s.home()
    s.pendown()

    for i in range(20):
        s.circle(r*i)
        s.penup()
        s.setx(r*i)
        s.sety(r*i*-1)
        s.pendown()
        j=rd.random()
        k=rd.random()
        l=rd.random()
        s.pencolor((j,k,l))
    s.hideturtle()
    tr.done()
