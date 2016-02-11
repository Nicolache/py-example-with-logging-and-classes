#!/usr/bin/python
import logging

# create logger
module_logger = logging.getLogger('NEW_application.external_module')

class external_class:
    def __init__(self):
        self.logger = logging.getLogger('NEW_application.external_module.external_class')
        self.logger.info('creating an instance of external_class')
    def do_something(self):
        self.logger.info('doing something')
        a = 1 + 1
        self.logger.info('done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')
