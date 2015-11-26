# coding=utf-8
import redis

from abstract_contacts import AbstractModel


class RedisContacts(AbstractModel):

    rc = redis.StrictRedis()

    def load_contacts(self):
        pass

    def find_contact(self, name):
        phone = self.rc.get(name)
        if phone is None:
            raise ValueError(self.NOT_EXIST_MESSAGE)
        return phone

    def delete_contact(self, name):
        if not self.rc.delete(name):
            raise ValueError(self.NOT_EXIST_MESSAGE)

    def save_contacts(self):
        pass

    def update_contact(self, name, phone):
        if not self.rc.exists(name):
            raise ValueError(self.NOT_EXIST_MESSAGE)
        self.rc.set(name, phone)

    def create_contact(self, name, phone):
        self.rc.set(name, phone)
