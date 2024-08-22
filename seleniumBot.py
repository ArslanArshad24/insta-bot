from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
large_font = ('Arial', 20)

class insta_bot:
    def __init__(self,em,pa):
        self.email=em
        self.password=pa
        self.url='https://www.instagram.com/'

    def insta_login(self):
        self.driver=webdriver.Chrome()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(url=self.url)
        time.sleep(10)
        email_box = self.driver.find_element(By.NAME, "username")
        time.sleep(2)
        passw_box = self.driver.find_element(By.NAME, "password")
        email_box.clear()
        passw_box.clear()
        email_box.send_keys(self.email)
        passw_box.send_keys(self.password)
        time.sleep(2)
        passw_box.send_keys(Keys.ENTER)
        time.sleep(10)


window = tk.Tk()
window.config(padx=10, pady=10,bg=YELLOW,)
window.geometry("800x400")

email = tk.Label(text='Email:',font=(FONT_NAME, 20, "bold"), fg=RED,padx=15,pady=5,)
email.grid(row=0,column=0)
email_entery = tk.Entry(window,width=30,font=large_font)
email_entery.grid(row=0,column=2,padx=30, pady=30)

passw = tk.Label(text='Password:',font=(FONT_NAME, 20, "bold"), fg=RED,padx=15,pady=5,)
passw.grid(row=1,column=0)
passw_entery = tk.Entry(window,width=30,font=large_font)
passw_entery.grid(row=1,column=2,padx=30, pady=30)

def get_login():
    email = email_entery.get()
    password = passw_entery.get()
    bot = insta_bot(email,password)
    bot.insta_login()

button = tk.Button(window,text=' Go ',command=get_login,width=3,font=large_font,bg=GREEN)
button.grid(row=3,column=2,)

window.mainloop()



