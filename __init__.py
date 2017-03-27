#!/usr/bin/env python

from parser_cls import Parser_cls
from utility_cls import Utility


data_dict = (Parser_cls.main())
print ('##########final dict##########')
Utility.print_dict(data_dict)
Utility.print_client(data_dict['client'])
for item in Utility.gen(data_dict['client']):
    item.rsync_cmd(data_dict['keys'], data_dict['host_files'])
