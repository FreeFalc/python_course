import pickle

from abstract_contacts import AbstractModel


def key_exists(f):
    def wrapper(self, name, *args):
        if name not in self.contacts:
            raise ValueError("Name doesn't exist")
        return f(self, name, *args)
    return wrapper


class PickleContacts(AbstractModel):
    FILENAME = 'contacts.dat'

    def __init__(self):
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.FILENAME, 'r') as f:
                return pickle.load(f)
        except (IOError, EOFError):
            return {}

    def save_contacts(self):
        with open(self.FILENAME, 'w') as f:
            pickle.dump(self.contacts, f)
        print "Contacts saved"

    def create_contact(self, name, phone):
        if name in self.contacts:
            raise ValueError("Name exists")
        self.contacts[name] = phone

    @key_exists
    def find_contact(self, name):
        return self.contacts[name]

    @key_exists
    def delete_contact(self, name):
        del self.contacts[name]

    @key_exists
    def update_contact(self, name, phone):
        self.contacts[name] = phone

    def list_contacts(self):
        return tuple(self.contacts.items())
