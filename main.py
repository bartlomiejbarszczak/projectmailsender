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
    def __init__(self, source_file, ):
        self.source_file_ = source_file

    def create_mybutton(self):
        pass



class Application:
    def __init__(self):
        pass

    def run(self):
        pass


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
