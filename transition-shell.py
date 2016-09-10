# -*- coding: utf-8 -*-

import locale
import time
import os
import re

from dialog import Dialog

locale.setlocale(locale.LC_ALL, '')


class MainDialog():
    def __init__(self, auto_run=True):
        self.d = Dialog(dialog="dialog", autowidgetsize=True, DIALOGRC='rc')
        self.d.set_background_title("ATILLA - Transition shell")
        if auto_run:
            self.run()

    def check_address(self, address):
        ip_regex = re.compile("^192.168.(10|253).\d{1,3}$")
        address_regex = re.compile("^([a-zA-Z0-9-]*\.){0,4}atilla\.org$")
        return ip_regex.match(address) or address_regex.match(address)

    def check_user(self, user):
        user_regex = re.compile("^[a-zA-Z0-9-]{0,255}$")
        return user_regex.match(user)

    def input_ssh_hostname(self):
        while True:
            code, address = self.d.inputbox("Enter the server FQDN / IP : ",
                                            width=35)

            if code == self.d.OK:
                if self.check_address(address):
                    return address
                else:
                    self.d.msgbox("Invalid address, plase make sure that you"
                                  " are trying to reach an ATILLA server",
                                  width=50, height=10)
            else:
                return None

    def input_ssh_user(self):
        while True:
            code, user = self.d.inputbox("Enter the username : ",
                                         init="root")
            if code == self.d.OK:
                if self.check_user(user):
                    return user
                else:
                    self.d.msgbox("Invalid user name")
            else:
                return None

    def ssh(self):
        hostname = self.input_ssh_hostname()
        if hostname is not None:
            user = self.input_ssh_user()
            if user is not None:
                os.system('clear')
                os.system('ssh ' + user + '@' + hostname)

    def learn_more(self):
        text = ("This application is meant to provide a user-friendly "
                "interface for SSH bouncing into ATILLA network.\n\n"
                "Source code available at :\n"
                "https://gitlab.atilla.org/adminsys/transition-shell")
        self.d.msgbox(text)

    def main_menu(self):
        main_menu_choices = [("#1", "Connect to another SSH server"),
                             ("#2", "Learn more about this application"),
                             ("#3", "Quit the program")]
        while True:
            code, tag = self.d.menu(("Welcome to ATILLA transition server, "
                                     "please choose one of the following "
                                     "options :"),
                                    choices=main_menu_choices)
            if code == self.d.OK:
                if tag == "#1":
                    self.ssh()
                elif tag == "#2":
                    self.learn_more()
                elif tag == "#3":
                    return
            else:
                return

    def run(self):
        self.main_menu()
        self.d.infobox("Goodbye !")
        time.sleep(0.25)
        os.system('clear')

if __name__ == "__main__":
    MainDialog()
