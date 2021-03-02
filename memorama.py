from tkinter import *
from tkinter import messagebox
import random


class Carta:
    def __init__(self):
        self.valor = 0
        self.posicion = 0
        self.oculto = True
        self.foto = PhotoImage(file="fondo.png")
