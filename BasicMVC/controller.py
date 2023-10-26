# Controller interacts with model through the getAll() method
# which fetches all the records displayed to the end user.

from model import Person

import view


def showAll():
    # gets the list of all person objects
    people_in_db = Person.getAll()
    # call the view
    return view.showAllView(people_in_db)


def start():
    view.startView()
    raw_input = input()
    if raw_input == 'y':
        return showAll()
    else:
        return view.endView()


if __name__ == '__main__':
    # running controller function
    start()