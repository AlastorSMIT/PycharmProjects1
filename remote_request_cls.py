import subprocess


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

    def pinger(self):
        ping_check = subprocess.Popen(["ping", '-c','2', self.adress],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        # ping_check = subprocess.check(["ping -c1 {} ".format(self.adress)])
        out,err = ping_check.communicate()
        print out
        if out:
            print("Host {} is alive!".format(self.adress))
        else:
            print("Host {} is dead!".format(self.adress))

    def passwordless_con(self):
        pass

    def rsync_cmd(self, keys, files):
        keys_str = ' '.join(keys)
        files_str =  ' '.join(files)
        rsync_cmd = subprocess.Popen(['rsync','-r'] + keys + files + [self.full_adress,],
                          stdout=subprocess.PIPE)
        out,err = rsync_cmd.communicate()
        print out

    @classmethod
    def self_create(cls, data_dict):
        Remote_request_cls.inst_array.append(Remote_request_cls(data_dict))
