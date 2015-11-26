import functools

from console_wrappers import ask_create_contacts, ask_find_contact, ask_delete_contact, ask_update_contact
from pickle_model import Contacts

my_contacts = Contacts()

controller = {
    'c': functools.partial(ask_create_contacts, my_contacts),
    'f': functools.partial(ask_find_contact, my_contacts),
    'd': functools.partial(ask_delete_contact, my_contacts),
    'u': functools.partial(ask_update_contact, my_contacts),
}



def default():
    print "Invalid action"
    
if __name__ == '__main__':
    try:
        while True:
            action = raw_input("Action?")
            if action in "Qq":
                break
            controller.get(action.lower(), default)()
    finally:
        my_contacts.save_contacts()