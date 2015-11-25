def ask_name():
    return raw_input('name?')
    
def ask_phone():
    return raw_input('phone?')
        
def ask_create_contacts(contacts):
    name = ask_name()
    phone = ask_phone()
    try:
         contacts.create_contact(name, phone)
    except ValueError as e:
         print e

def ask_find_contact(contacts):
    name = name = ask_name()
    try:
        print name, contacts.find_contact(name)
    except ValueError as e:
        print e
        
def ask_delete_contact(contacts):
    name = ask_name()
    try:
        contacts.delete_contact(name)
    except ValueError as e:
        print e
        
def ask_update_contact(contacts):
    name = ask_name()
    phone = ask_phone()
    try:
        contacts.update_contact(name, phone)
    except ValueError as e:
        print e



