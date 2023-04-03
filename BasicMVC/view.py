# Displays all the records fetched within the model.
# View never interacts with model; controller does this work (communicating with model and view).

from model import Person


def showAllView(list):
    # print('in our db we have %i users. Here they are: ' % len(Person.getAll()))
    print('in our db we have %i users. Here they are: ' % len(list))
    for item in list:
        print(item.name())


def startView():
    print("MVC - the simplest example")
    print('Do you want to see all the records in the db? [y/n]')


def endView():
    print('Goodbye!')