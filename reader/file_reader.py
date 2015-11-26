# coding=utf-8
class FileReader(object):
    def __init__(self, filename='session.txt'):
        try:
            self.file = open(filename, 'r')
        except IOError:
            raise

    def read_action(self):
        command = self.file.readline()[:-1]
        if not command:
            command = 'q'
        print command
        return command

    def __getattr__(self, item):
        assert item in ('ask_action', 'ask_name', 'ask_phone')
        return self.read_action

    def close(self):
        self.file.close()