#!/usr/bin/env python
# -*- coding: utf-8 -*-

from connector_misp import MispMySQLConnector

if __name__ == '__main__':
    connector = MispMySQLConnector()
    connector.import_auth()
    connector.cache_attributes()
