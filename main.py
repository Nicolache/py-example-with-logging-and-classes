#!/usr/bin/python
import logging
import external_module

# create logger with 'NEW_application'
logger = logging.getLogger('NEW_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('total.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(processName)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of external_module.external_class')
a = external_module.external_class()
logger.info('created an instance of external_module.external_class')
logger.info('calling external_module.external_class.do_something')
a.do_something()
logger.info('finished external_module.external_class.do_something')
logger.info('calling external_module.some_function()')
external_module.some_function()
logger.info('done with external_module.some_function()')
