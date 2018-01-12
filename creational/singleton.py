#!/usr/bin/env python
"""
SINGLETON

Use the Singleton pattern when:
    1. there must be exactly one instance of a class, and it must be
       accessible to clients from a well-known access point.
    2. the sole instance should be extensible by subclassing, and clients
       should be able to use an extended instance without modifying their code.
"""
import logging


class Connection(object):
    """
    Singleton
    1. Defines an Instance operation that lets clients access its unique
       instance.
    2. May be responsible for creating its own unique instance.
    """
    def __new__(type):
        if not '_connection' in type.__dict__:
            type._connection = object.__new__(type)
            logging.basicConfig(level=logging.INFO)
            logging.info('New database connection created!')

        logging.info('Connection established.')
        return type._connection


if __name__ == "__main__":
    c = Connection()
    d = Connection()
