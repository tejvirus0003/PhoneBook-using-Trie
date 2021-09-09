# TEJUS KAW
class Node:
    def __init__(self):
        self.contacts = {}
        self.isend = False
        self.numbers = []


class Trie():
    def __init__(self):
        self.head = Node()

    def insert(self, name, number):
        temp = self.head
        for i in range(len(name)):
            if not temp.contacts.get(name[i]):
                temp.contacts[name[i]] = Node()
            temp = temp.contacts[name[i]]
        temp.isend = True
        if type(number) is list:
            for i in number:
                temp.numbers.append(i)
        else:
            temp.numbers.append(number)
        temp.numbers = list(set(temp.numbers))

    def find(self, name):
        temp = self.head
        for i in range(len(name)):
            if not temp.contacts.get(name[i]):
                return False
            temp = temp.contacts.get(name[i])
        if temp.isend:
            return temp
        return False

    def updatenumber(self, name, prevnumber, newnumber):
        res = self.find(name)
        if res is False:
            print("Sorry such contact doesnot exist")
            return
        res.numbers.remove(prevnumber)
        res.numbers.append(newnumber)

    def updatecontactname(self, prevname, newname):
        result = self.find(prevname)
        if result is False:
            print('Sorry such name doesnot exist , you can instead make new contact')
            response = input('Do you want to make new contact ? (Y,y) OR NO')
            if response == 'Y' or response == 'y':
                numb = input('Enter the number plz ')
                self.insert(newname, numb)
            return
        result.isend = False
        store = result.numbers.copy()
        result.numbers.clear()
        self.insert(newname, store)

    def deletecontact(self, name):
        res = self.find(name)
        if res is False:
            print('No such contact exist to delete')
            return
        res.isend = False
        res.numbers.clear()

    def dfs(self, temp, s):
        if temp.isend is True:
            print(s, temp.numbers)
        for key, value in temp.contacts.items():
            if value is not None:
                self.dfs(value, s+key)

    def searchbyname(self, name):

        temp = self.head
        for i in range(len(name)):
            if not temp.contacts.get(name[i]):
                print('No such contact exist nor any starts with it')
                return False
            temp = temp.contacts.get(name[i])
        self.dfs(temp, name)


