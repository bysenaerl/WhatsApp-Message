from book import Book
import pywhatkit


class Member:
    def __init__(self, name):
        self.name = name 
        self.persons = []

    def add_person(self, person, number):
        person = Book(person, number)
        self.persons.append(person)
        self.personumber = person.number

    def sendmsg_person(self, name):
        for person in self.persons:
            if person.name == name:
                pywhatkit.sendwhatmsg_instantly(self.personumber, "message",7,True,3)
                
                
    