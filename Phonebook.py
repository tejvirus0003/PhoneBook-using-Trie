import colorama
from answer import Trie
import os
import time


def clear():
    # check and make call for specific operating system
    _ = os.system('clear' if os.name == 'posix' else 'cls')

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


def main():
    Phonebook = Trie()
    while True:
        print(colorama.Fore.BLUE+'This is a phone book directory for u')
        print('To insert a new contact or add number to existing name, press 1')
        print('To delete a contact, press 2')
        print('To update an existing contact , press 3 ')
        print('To search an existing contact by prefix name, press 4')
        print('If you want to exit , press any other key')
        response = input(colorama.Style.BRIGHT +
                         colorama.Fore.GREEN+'Press your response : ')
        if response == '1':
            name = input(colorama.Fore.YELLOW +
                         colorama.Style.NORMAL+'Enter the name plz.. : ')
            print(colorama.Fore.YELLOW +
                  colorama.Style.NORMAL+'ENter the phone number plz (can give any number of phone numbers at a time , splitted by spaces) : ')
            number = input().split()
            Phonebook.insert(name=name, number=number)
        elif response == '2':
            name = input('Enter the name plz : ')
            Phonebook.deletecontact(name)
        elif response == '3':
            print('Do you want to update name or update number ? ')
            print('Press 1 for name updatation')
            print('Press 2 for number updation')
            num = input('Enter plz : ')
            if num == '1':
                pass
                prevname = input(colorama.Fore.WHITE+'Enter already existing name : ')
                newname = input(colorama.Fore.WHITE+'Enter the new to be updated name : ')
                Phonebook.updatecontactname(prevname, newname)
            elif num == '2':
                name = input(colorama.Fore.WHITE+'Enter contact name : ')
                prevnumber = input(colorama.Fore.WHITE+'Enter the previous number : ')
                newnumber = input(colorama.Fore.WHITE+'Enter the new number : ')
                Phonebook.updatenumber(name, prevnumber, newnumber=newnumber)
            else:
                break
        elif response == '4':
            name = input(colorama.Fore.RED+'Enter the prefix name for searching plx : ')
            Phonebook.searchbyname(name)
        else:
            break
        time.sleep(2)
        clear()


if __name__ == '__main__':
    main()
