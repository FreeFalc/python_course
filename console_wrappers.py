
def ask_create_contacts(contacts, reader):
    name = reader.ask_name()
    phone = reader.ask_phone()
    try:
        contacts.create_contact(name, phone)
    except ValueError as e:
        print e


def ask_find_contact(contacts, reader):
    name = reader.ask_name()
    try:
        print name, contacts.find_contact(name)
    except ValueError as e:
        print e
        

def ask_delete_contact(contacts, reader):
    name = reader.ask_name()
    try:
        contacts.delete_contact(name)
    except ValueError as e:
        print e


def ask_update_contact(contacts, reader):
    name = reader.ask_name()
    phone = reader.ask_phone()
    try:
        contacts.update_contact(name, phone)
    except ValueError as e:
        print e



