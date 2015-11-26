import functools

import settings
from console_wrappers import ask_create_contacts, ask_find_contact, ask_delete_contact, ask_update_contact

if settings.DATABASE == "Pickle":
    from contacts.pickle_contacts import PickleContacts as Contacts
elif settings.DATABASE == "Redis":
    from contacts.redis_contacts import RedisContacts as Contacts
elif settings.DATABASE == "MySQL":
    from contacts.mysql_contacts import MysqlContacts as Contacts
else:
    print "Invalid database"
    exit()

if settings.READER == 'Console':
    from reader.console_reader import ConsoleReader as DefaultReader
else:
    from reader.file_reader import FileReader as DefaultReader

contacts = Contacts()
reader = DefaultReader()

controller = {
    'c': ask_create_contacts,
    'f': ask_find_contact,
    'd': ask_delete_contact,
    'u': ask_update_contact,
}

controller = {key: functools.partial(value, contacts, reader) for key, value in controller.items()}


def default():
    print "Invalid action"


if __name__ == '__main__':
    try:
        while True:
            action = reader.ask_action()
            if action in "Qq":
                break
            controller.get(action.lower(), default)()
    finally:
        contacts.save_contacts()
        reader.close()