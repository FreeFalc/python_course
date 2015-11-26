# coding=utf-8
from abstract_contacts import AbstractModel

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


class SQLAlchemyContacts(AbstractModel):
    engine = create_engine('mysql://root:1@localhost/phones')

    def __init__(self):
        self.session = Session(self.engine)
        Base = automap_base()
        Base.prepare(self.engine, reflect=True)
        self.Contacts = Base.classes.contacts

    def create_contact(self, name, phone):
        self.session.add(self.Contacts(name=name, phone=phone))
        self.session.commit()

    def delete_contact(self, name):
        if not self.session.query(self.Contacts).filter_by(name=name).delete():
            raise ValueError(self.NOT_EXIST_MESSAGE)
        self.session.commit()

    def find_contact(self, name):
        contacts = self.session.query(self.Contacts).filter_by(name=name).all()
        if contacts:
            return contacts[0].phone
        raise ValueError(self.NOT_EXIST_MESSAGE)

    def save_contacts(self):
        pass

    def load_contacts(self):
        pass

    def update_contact(self, name, phone):
        if not self.session.query(self.Contacts).filter_by(name=name).update({'phone': phone}):
            raise ValueError(self.NOT_EXIST_MESSAGE)
        self.session.commit()
