# utility
from remote_request_cls import Remote_request_cls

class Utility:
    @staticmethod
    def gen(it_obj):
        for item in it_obj:
            yield item

    @staticmethod
    def print_dict(some_dict):
        for key in Utility.gen(some_dict):
            print ('{} = {}'.format(key, some_dict[key]))

    @staticmethod
    def print_client(clientlist):
        for item in Utility.gen(clientlist):
            item.self_print()
