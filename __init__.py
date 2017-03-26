#!/usr/bin/env python

from parser_cls import Parser_cls
from utility_cls import Utility


date_dict = (Parser_cls.main())
print ('##########final dict##########')
Utility.print_dict(date_dict)
Utility.print_client(date_dict['client'])
for item in Utility.gen(date_dict['client']):
    item.rsync_cmd(date_dict['keys'],date_dict['host_files'])
