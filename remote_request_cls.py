import os


class Remote_request_cls():
    """ Produces objects for each remotehost machine """
    ind = 0
    inst_array = list()

    def __init__(self, data_dict):
        """Constructor"""
        self.username = data_dict['username']
        self.adress = data_dict['ip']
        self.port = data_dict['port']
        self.rem_dir = data_dict['remote_dir']
        self.password = data_dict['password']
        self.ind = Remote_request_cls.ind
        Remote_request_cls.ind += 1
        self.full_adress = (self.username + '@' + self.adress + ':' + self.rem_dir)

    def self_print(self):
        print (('###Request object number {}.\n'
                'Attributes:\n'
                '   username: {}\n'
                '   remote adress: {}\n'
                '   remote dir: {}\n'
                '   password: {}\n'
                '   port: {}').format(Remote_request_cls.ind, self.username, self.adress, self.rem_dir, self.password,
                                      self.port))

    def ping_meth(self):
        pass

    def passwordless_con(self):
        pass

    def rsync_cmd(self, keys, files):
        os.system('rsync' + ' ' + ' '.join(keys) + ' ' + ' '.join(files) + ' ' + self.full_adress)

    @classmethod
    def self_create(cls, data_dict):
        Remote_request_cls.inst_array.append(Remote_request_cls(data_dict))
