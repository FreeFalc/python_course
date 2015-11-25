from console_wrappers import ask_create_contacts, ask_find_contact, ask_delete_contact, ask_update_contact
from pickle_model import save_contacts


controller = {
    'c': ask_create_contacts,
    'f': ask_find_contact,
    'd': ask_delete_contact,
    'u': ask_update_contact,
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
        save_contacts()