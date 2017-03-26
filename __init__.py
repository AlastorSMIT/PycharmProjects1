#!/usr/bin/env python

from parser_cls import Parser_cls
from utility_cls import Utility

date_dict = {'host_files': '', 'remote_dir': '', 'keys': [], 'username': '', 'ip': '', 'port': '', 'password': ''}

date_dict.update(Parser_cls.main())
print ('##########final dict##########')
Utility.print_dict(date_dict)