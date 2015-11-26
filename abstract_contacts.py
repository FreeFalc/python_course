# coding=utf-8
import abc


class AbstractModel(object):
    __metaclass__ = abc.ABCMeta
    NOT_EXIST_MESSAGE = "Name doesn't exist"

    @abc.abstractmethod
    def load_contacts(self):
        pass

    @abc.abstractmethod
    def save_contacts(self):
        pass

    @abc.abstractmethod
    def create_contact(self, name, phone):
        pass

    @abc.abstractmethod
    def find_contact(self, name):
        pass

    @abc.abstractmethod
    def delete_contact(self, name):
        pass

    @abc.abstractmethod
    def update_contact(self, name, phone):
        pass
