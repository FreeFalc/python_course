# coding=utf-8
import os
from xml.dom.minidom import parse


def parse_xml_config():
    print "XML Configuration..."
    dom = parse('settings.xml')
    database = dom.getElementsByTagName('database')[0].firstChild.nodeValue
    reader = dom.getElementsByTagName('reader')[0].firstChild.nodeValue
    return database.strip(), reader.strip()

if os.path.isfile('settings.xml'):
    DATABASE, READER = parse_xml_config()
else:
    from settings import DATABASE, READER

if DATABASE == "Pickle":
    from contacts.pickle_contacts import PickleContacts as Contacts
elif DATABASE == "Redis":
    from contacts.redis_contacts import RedisContacts as Contacts
elif DATABASE == "MySQL":
    from contacts.mysql_contacts import MysqlContacts as Contacts
elif DATABASE == "SQLAlchemy":
    from contacts.sqlalchemy_contacts import SQLAlchemyContacts as Contacts
else:
    print "Invalid database"
    exit()

if READER == 'Console':
    from reader.console_reader import ConsoleReader as DefaultReader
else:
    from reader.file_reader import FileReader as DefaultReader

contacts = Contacts()
reader = DefaultReader()
