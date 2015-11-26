# coding=utf-8
class ConsoleReader(object):
    @staticmethod
    def ask_name():
        return raw_input('name?')

    @staticmethod
    def ask_phone():
        return raw_input('phone?')

    @staticmethod
    def ask_action():
        return raw_input("Action?")

    def close(self):
        pass
