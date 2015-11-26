# coding=utf-8
class ConsoleReader(object):
    @staticmethod
    def validate(message):
        if "'" in message or " " in message:
            raise ValueError("SQL Injection")
        return message

    @staticmethod
    def ask_name():
        return ConsoleReader.validate(raw_input('name?'))

    @staticmethod
    def ask_phone():
        return ConsoleReader.validate(raw_input('phone?'))

    @staticmethod
    def ask_action():
        return raw_input("Action?")

    def close(self):
        pass
