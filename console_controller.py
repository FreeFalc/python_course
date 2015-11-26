import functools

from console_wrappers import ask_create_contacts, ask_find_contact, ask_delete_contact, ask_update_contact
from pickle_model import Contacts
import settings
if settings.READER == 'Console':
    from console_reader import ConsoleReader as DefaultReader
else:
    from file_reader import FileReader as DefaultReader

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