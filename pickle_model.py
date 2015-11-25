import pickle

FILENAME = 'contacts.dat'


def load_contacts():
    try:
        with open(FILENAME, 'r') as f:
            return pickle.load(f)
    except IOError, EOFError:
        return {}
        

def save_contacts():
    with open(FILENAME, 'w') as f:
        pickle.dump(contacts, f)


def create_contact(name, phone):
    if name in contacts:
        raise ValueError("Name exists")
    contacts[name] = phone
    

def key_exists(f):
    def wrapper(name, *args):
        if name not in contacts:
            raise ValueError("Name doesn't exist")
        return f(name, *args)
    return wrapper
    

@key_exists
def find_contact(name):
    return contacts[name]
    

@key_exists
def delete_contact(name):
    del contacts[name]
    

@key_exists
def update_contact(name, phone):
    contacts[name] = phone


contacts = load_contacts()