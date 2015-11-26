

def ask_name():
    return raw_input('name?')
    
def ask_phone():
    return raw_input('phone?')
        
def ask_create_contacts(f_contacts):
    name = ask_name()
    phone = ask_phone()
    try:
         f_contacts.create_contact(name, phone)
    except ValueError as e:
         print e

def ask_find_contact(f_contacts):
    name = ask_name()
    try:
        print name, f_contacts.find_contact(name)
    except ValueError as e:
        print e
        
def ask_delete_contact(f_contacts):
    name = ask_name()
    try:
        f_contacts.delete_contact(name)
    except ValueError as e:
        print e
        
def ask_update_contact(f_contacts):
    name = ask_name()
    phone = ask_phone()
    try:
        f_contacts.update_contact(name, phone)
    except ValueError as e:
        print e



