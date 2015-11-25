from pickle_model import create_contact, find_contact, delete_contact, update_contact

def ask_name():
    return raw_input('name?')
    
def ask_phone():
    return raw_input('phone?')
        
def ask_create_contacts():
    name = ask_name()
    phone = ask_phone()
    try:
         create_contact(name, phone)
    except ValueError as e:
         print e

def ask_find_contact():
    name = name = ask_name()
    try:
        print name, find_contact(name)
    except ValueError as e:
        print e
        
def ask_delete_contact():
    name = ask_name()
    try:
        delete_contact(name)
    except ValueError as e:
        print e
        
def ask_update_contact():
    name = ask_name()
    phone = ask_phone()
    try:
        update_contact(name, phone)
    except ValueError as e:
        print e



