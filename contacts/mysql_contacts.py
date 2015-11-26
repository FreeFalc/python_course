# coding=utf-8
import MySQLdb
from abstract_contacts import AbstractModel


class MysqlContacts(AbstractModel):
    db = MySQLdb.connect(host='localhost', user='root', passwd='1', db='phones')

    def __init__(self):
        self.cursor = self.db.cursor()

    def load_contacts(self):
        pass

    def find_contact(self, name):
        if not self.cursor.execute("select phone from contacts where name='{}'".format(name)):
            raise ValueError(self.NOT_EXIST_MESSAGE)
        return self.cursor.fetchone()[0]

    def delete_contact(self, name):
        if not self.cursor.execute("delete from contacts where name='{}'".format(name)):
            raise ValueError(self.NOT_EXIST_MESSAGE)
        self.cursor.execute("commit")

    def save_contacts(self):
        pass

    def update_contact(self, name, phone):
        if not self.cursor.execute("update contacts set phone='{}' where name='{}'".format(phone, name)):
            raise ValueError(self.NOT_EXIST_MESSAGE)
        self.cursor.execute("commit")

    def create_contact(self, name, phone):
        try:
            self.find_contact(name)
        except ValueError:
            pass
        else:
            raise ValueError("Name exists")
        self.cursor.execute("insert into contacts (name, phone) values ('{}', '{}')".format(name, phone))
        self.cursor.execute("commit")
