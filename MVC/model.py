# Calls for a method, which fetches all the records of the Person table in database.
# The records are presented in JSON format.

import json


class Person(object):
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

        # returns Person name eg "John Smith"
        # NOTE: so many variations of the same function!!
    def name(self):
        # return self.first_name + " " + self.last_name
        # return "{} {}".format(self.first_name, self.last_name)
        # return f"{self.first_name} {self.last_name}"
        # return " ".join([self.first_name, self.last_name])
        return ("%s %s" % (self.first_name, self.last_name))

    # def to_dict(self):
    #     return {'first_name': self.first_name, 'last_name': self.last_name}

    @classmethod
    # returns all people inside db.txt as list of Person objects
    def getAll(self):
        database = open('db.txt', 'r')
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            item = json.loads(item)
            person = Person(item['first_name'], item['last_name'])
            result.append(person)
        return result


# people = {
#     "first_name": "John",
#     "last_name": "Doe"
# }, {
#     "first_name": "Jane",
#     "last_name": "Doe"
# }, {
#     "first_name": "Bob",
#     "last_name": "Smith"
# }

# with open('db.txt', 'w') as f:
#     json.dump([p.to_dict() for p in people], f)

# print(Person.getAll())