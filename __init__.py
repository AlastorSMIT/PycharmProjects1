#!/usr/bin/env python

from argparsev2 import inputparse
from parser_cls import Parser_cls

date_dict = {'host_files': '', 'remote_dir': '', 'keys': [], 'username': '', 'ip': '', 'port': '', 'password': ''}

tmp_dict,unknownlist =inputparse()
date_dict.update(tmp_dict)
date_dict.update(Parser_cls.main(date_dict,unknownlist))
print ('final dict')
print(date_dict)
