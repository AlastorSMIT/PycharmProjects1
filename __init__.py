from parser_cls import Parser_cls
from utility_cls import Utility

def main():
    data_dict = (Parser_cls.main())
    print ('##########final dict##########')
    Utility.print_dict(data_dict)
    Utility.print_client(data_dict['client'])
    Utility.rsync_all(data_dict)
