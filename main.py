from src.messagestructure import message
from src.goldenrules import all_rules
import smtplib
import random
# import multiprocessing
# import time
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


def add_contact(entry_label, root, contacts):
    value = entry_label.get_input_entry()
    print(value)
    if_include = value.find("@")
    if if_include == -1:
        show_this_on_screen = Label(root, text="Niepoprawny adres email")
        show_this_on_screen.place(relx=0.5, rely=0.56, relwidth=0.65, anchor="center")
    else:
        temp = Contact(value)
        contacts.append(temp)
        show_this_on_screen = Label(root, text="Dodano adres email: " + value)
        show_this_on_screen.place(relx=0.5, rely=0.56, relwidth=0.65, anchor="center")
        entry_label.my_entry_delete()


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
        self.add_button = Button(self.root_, image=self.add_button_pre, bg='#4898d0', borderwidth=0,
                                 command=self.command_, height=27, width=200)

    def create_my_button(self):
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
        return self.input_entry_.get()

    def my_entry_delete(self):
        self.input_entry_.delete(0, END)


class Application:
    def __init__(self):
        self.root_ = Tk()
        self.root_.title('NPG zlote mysli')
        self.root_.geometry('436x772')
        self.root_.resizable(False, False)
        self.root_.configure(bg='white')

        self.background_pre_ = Image.open('images/tlo.png')
        self.background_pre_ = self.background_pre_.resize((432, 768), )
        self.background_pre_ = ImageTk.PhotoImage(self.background_pre_)
        self.background_ = Label(self.root_, image=self.background_pre_)
        self.background_.place(x=0, y=0, relwidth=1, relheight=1)

        self.contacts_ = [
            Contact("b.barszczak35@gmail.com"),
            Contact("bbarszczak@student.agh.edu.pl")
            # Contact("brzanad@gmail.com"),
            # Contact("brzanad@student.agh.edu.pl"),
            # Contact("gabrielabergiel@gmail.com"),
            # Contact("jakbu@student.agh.edu.pl"),
            # Contact("jakbu8@gmail.com"),
            # Contact("lukaszbogacz@student.agh.edu.pl"),
            # Contact("nataliia@agh.edu.pl")
        ]

    def run(self):
        # entry label
        entry_label = MyEntry(self.root_, 0.5, 0.592)
        entry_label.create_my_entry()

        # add button
        button_add = MyButton('images/add_button.png', self.root_,
                              lambda: add_contact(entry_label, self.root_, self.contacts_), 0.5, 0.65)
        button_add.create_my_button()

        # delete button
        button_del = MyButton('images/delete_button.png', self.root_, None, 0.5, 0.72)
        button_del.create_my_button()

        # exit button
        button_exit = MyButton('images/exit_button.png', self.root_, self.root_.quit, 0.5, 0.79)
        button_exit.create_my_button()

        self.root_.iconify()
        self.root_.update()
        self.root_.deiconify()
        self.root_.mainloop()


def main():
    apps = []
    for i in range(0, 1):
        apps.append(Application())

    for app in apps:
        app.run()


if __name__ == "__main__":
    main()
