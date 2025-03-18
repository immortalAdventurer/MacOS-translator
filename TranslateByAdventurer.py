import tkinter as tk
import requests
from tkinter import *
from googletrans import Translator
from datetime import datetime

def validate_login():
    entered_login = login_entry.get()
    entered_password = password_entry.get()

    # if or else Login and Password
    if entered_login == "immortal" and entered_password == "12345678":
        result_label.config(text="Login Successful!")
        root.destroy()  # Closing the current window
        open_new_window()  # Open new empty window
    else:
        result_label.config(text="Login or password incorrect!,try again.")

def get_weather(): # Weather def
    api_key = "4503c1f270660db7feb81545cb1ac019"
    city = "Mytishchi"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather_info = f"weather in mytishchi: {data['weather'][0]['description']}, Температура: {data['main']['temp']}°C"
    return weather_info

def open_new_window(): # a new window will open if the password is entered correctly
    translator = Translator()

    mac = Tk()
    x = (mac.winfo_screenwidth() - mac.winfo_reqwidth()) - 1240
    y = (mac.winfo_screenheight() - mac.winfo_reqheight()) - 665
    mac.wm_geometry("+%d+%d" % (x, y))
    mac.geometry("720x760")
    mac.title("Переводчик")


    Label_Entry = Label(text="Введите текст для перевода:")
    Label_Lang = Label(text="Введите язык на который нужно перевести:")
    Label_Translate = Label(text="Перевод")
    Entry_Entry = Entry()
    Entry_Lang = Entry()

    def translate_bt():
        ent = Entry_Entry.get()
        ent_lang = Entry_Lang.get()
        translaten_message = translator.translate(ent_lang, dest=ent)
        Label_Translate.config(text=translaten_message.text)

    Button_Translate = Button(text="Перевести", command=translate_bt)

    Label_Entry.pack()
    Entry_Lang.pack()
    Label_Lang.pack()
    Entry_Entry.pack()
    Label_Translate.pack()
    Button_Translate.pack()


    # Добавление метки для погоды
    weather_label = Label(text=get_weather())
    weather_label.pack()

    mac.mainloop()

# Создание главного окна
root = tk.Tk()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) - 1240
y = (root.winfo_screenheight() - root.winfo_reqheight()) - 665
root.wm_geometry("+%d+%d" % (x, y))
root.geometry("720x760")
root.title("Login window")

alex_label=Label(text="Enter login and password: ")
alex_label.pack()

login_label = tk.Label(root, text="Enter your login: ")
login_label.pack()
login_entry = tk.Entry(root)
login_entry.pack()

password_label = tk.Label(root, text="Enter your password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="login", command=validate_login)
login_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
