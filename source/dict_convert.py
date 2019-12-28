import logging


class DictionaryConverter:

    def __init__(self, dictionary: dict):
        # logging.info('init')
        for item in dictionary:
            # logging.info('{0}-->{1}'.format(item, dictionary.get(item)))
            setattr(self, item, dictionary.get(item))