import re
from argparsev2 import Inputparser
from utility_cls import Utility

class Parser_cls(Inputparser):
    """Second stage parser. Parsing unknown for 'argparse' parameters 
        and splits 'username:port@hostname:/dir' into pieces.
        :returns dict """

    @staticmethod
    def keys_parse(input_list):
        """ fill the key_list with parameters for rsync. """
        SINGLE_PARAM = tuple('PavSzqi')
        key_set = set()

        for item in Parser_cls.gen(input_list):
            if (item.startswith('-')):
                if (all(ch in SINGLE_PARAM for ch in Parser_cls.gen(item[1:]))):
                    key_set.update([('-' + char) for char in item[1:]])

        return (list(key_set))

    @staticmethod
    def hostrequest_parse(hostname):
        """ username:port@ip_address:/dir parsing """
        delim_ind = re.search("[.,:@]", hostname)
        username = hostname[:delim_ind.start()]
        port = ''
        if (hostname[delim_ind.start()] is not '@'):
            hostname = hostname[delim_ind.end():]
            delim_ind = re.search("[.,:@]", hostname)
            port = hostname[: delim_ind.start()]
        if ('/' in hostname):
            id_end = hostname.rfind(':')
            remote_dir = hostname[id_end + 1:]
        else:
            id_end = len(hostname)
            remote_dir = '/' + username
        host_id = hostname[delim_ind.end():id_end]

        data_dict_host = {'remote_dir': remote_dir,
                          'username': username, 'ip': host_id,
                          'port': port}

        return data_dict_host

    @staticmethod
    def port_to_keys(date_dict_port):
        """ Add '-p port' to a -e params, if port exist """
        port = date_dict_port['port']
        if (port):
            ind = 0
            keys_list = date_dict_port['keys']
            key_str = '-e \'ssh -p {}\''.format(port)

            if (any(item.startswith('-e') for item in Parser_cls.gen(keys_list))):
                for item in keys_list:
                    if (item.startswith('-e')):
                        ind = keys_list.index(item)
                keys_list[ind] = key_str
            else:
                keys_list.append(key_str)
            date_dict_port['keys'] = keys_list

        return date_dict_port

    @staticmethod
    def find_hostrequest(some_lis):
        """ Looks for last non key item in list (without '-')
            saves it as class variable """
        if (len(some_lis) > 1):
            hostrequest = some_lis[-1]
        else:
            print ('No File/directories or \'username@hostname:/dir\' parameter')
            exit(1)
            hostrequest = ''

        some_lis.remove(hostrequest)
        return some_lis, str(hostrequest)

    @staticmethod
    def gen(some_list):
        for item in some_list:
            yield item

    @staticmethod
    def main():
        """ Head method of the Parser class. Calls all its method to modify and parse dictionary date.
            :returns dict """
        # date_dict = {'host_files': '', 'remote_dir': '', 'keys': [], 'username': '', 'ip': '', 'port': '',
        #              'password': ''}

        date_dict, unknownlist = Parser_cls.inputparse()
        # date_dict.update(tmp_dict)
        date_dict['host_files'], hostname = Parser_cls.find_hostrequest(date_dict['host_files'])
        # date_dict['keys'] += Parser_cls.keys_parse(unknownlist)
        date_dict.update(Parser_cls.hostrequest_parse(hostname))
        date_dict.update(Parser_cls.port_to_keys(date_dict))
        print ('###########Parser.main() worked out.##########')
        Utility.print_dict(date_dict)
        return date_dict
        #
        # # Data for check.
        # data_dict = {'host_files': '', 'remote_dir': '', 'keys': [], 'username': '', 'ip': '', 'port': '', 'password': ''}
        # unknown_list = ['some', 'str', '-SPi', '-P', 'username:90@hostname:/dir']
        # Parser_cls.main(data_dict, unknown_list)
