from src.messagestructure import message
from src.goldenrules import all_rules
import smtplib
import random
import multiprocessing
import time
from tkinter import *
from PIL import Image, ImageTk


def mail(list_of_contacts):
    email_address = 'npgprojektzlotemysli@outlook.com'
    email_password = 'ProjektNPG2022'

    smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_address, email_password)

    for elem in list_of_contacts:
        goldenrule = random.choice(all_rules)
        while goldenrule == elem.usedrules_:
            goldenrule = random.choice(all_rules)

        msg = message("Zlote mysli", goldenrule, "images/jestessuper.jpg")
        smtp.sendmail(from_addr=email_address, to_addrs=elem.get_contact(), msg=msg.as_string())

    smtp.quit()


class Contact:
    def __init__(self, contact_):
        self.contact_ = contact_
        self.usedrules_ = []

    def get_usedrules(self):
        return self.usedrules_

    def get_contact(self):
        return self.contact_

    def expand_usedrules(self, string):
        self.usedrules_.append(string)


class MyButton:
    def __init__(self, source_file, passed_root, passed_command, passed_relx, passed_rely):
        self.source_file_ = source_file
        self.root_ = passed_root
        self.command_ = passed_command
        self.relx_ = passed_relx
        self.rely_ = passed_rely
        self.add_button_pre = Image.open(self.source_file_)
        self.add_button_pre = self.add_button_pre.resize((200, 27), )
        self.add_button_pre = ImageTk.PhotoImage(self.add_button_pre)

    def create_my_button(self):

        self.add_button = Button(self.root_, image=self.add_button_pre, bg='#4898d0', borderwidth=0, command=self.command_, height=27, width=200)
        self.add_button.place(relx=self.relx_, rely=self.rely_, anchor="center")


class MyEntry:
    def __init__(self, passed_root, passed_relx, passed_rely):
        self.root_ = passed_root
        self.relx_ = passed_relx
        self.rely_ = passed_rely
        self.input_entry_ = Entry(self.root_)

    def create_my_entry(self):
        self.input_entry_.place(relx=self.relx_, rely=self.rely_, relwidth=0.7, anchor="center")

    def get_input_entry(self):
        return self.input_entry_


class Application:
    def __init__(self):
        self.root_ = Tk()
        self.root_.title('NPG zlote mysli')
        self.root_.geometry('436x772')
        self.root_.resizable(False, False)
        self.root_.configure(bg='white')

    def run(self):
        # add button
        buttonadd = MyButton('images/add_button.png', self.root_, None, 0.5, 0.65)
        buttonadd.create_my_button()

        # delete button
        buttondel = MyButton('images/delete_button.png', self.root_, None, 0.5, 0.72)
        buttondel.create_my_button()

        # exit button
        buttonexit = MyButton('images/exit_button.png', self.root_, self.root_.quit, 0.5, 0.79)
        buttonexit.create_my_button()

        self.root_.iconify()
        self.root_.update()
        self.root_.deiconify()
        self.root_.mainloop()


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
