import argparse
from utility_cls import Utility


class Inputparser:
    """ First stage parser. Using 'argparse' module to pull out all valid parameters."""

    @staticmethod
    def inputparse():
        """ Static method which draws out all valid parameters. Based on 'argparse' module.
            :returns dict,list """

        SINGLE_PARAM = tuple('PavSzqi')

        filesgarbage = []
        known = []

        parser = argparse.ArgumentParser(description='\'rsync\' wrapper')
        parser.add_argument('-process', action='store_true', default=False)
        parser.add_argument('-pass', action="store", dest="userpass", type=str)
        parser.add_argument('-e', action="store", dest="connection", type=str)
        parser.add_argument('files', type=str, help='list of files and dirrs to copy', nargs='*')
        # Fill arguments in group
        single_args = parser.add_argument_group('Valid single letter arguments')
        for item in SINGLE_PARAM:
            single_args.add_argument('-{}'.format(item), action='store_true', default=False)

        args, unknown = parser.parse_known_args()
        # ['-PavSzqi', '-RsQz', '-e ssh', '-pass=No1LiveS4ever', '-kaka', '/abba', 'krek',
        #  'root.22@hostname:/junk', '-kek', '-i', '-P', '-process']
        for i in args.files:
            filesgarbage.append(i)

        if args.process:
            known.append('-process')

        for item in SINGLE_PARAM:
            if (eval('args.{} is True'.format(item))):
                known.append('-' + item)

        if args.connection == 'ssh':
            known.append('-e ssh')
        elif args.connection == 'rsh':
            known.append('-e rsh')

        output_dict = {'host_files': filesgarbage, 'keys': known, 'password': args.userpass}

        print ('###########Inputrser() worked out.##########')
        Utility.print_dict(output_dict)

        return (output_dict, unknown)
