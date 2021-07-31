from pythonping import ping
import sys

class Subneet_Error(Exception):
    def __init__(self,subnet,HELP):
        print(f'Subnet "{subnet}" is undefined or not an integer number')
        print(HELP)
        sys.exit(1)


def get_timeout(timeout= timeout]):
    try:
        return int(sys.argv[2])
    except IndexError:
        return 0.1



# ip = ip.split('.')
# ip = ip[0:-1]
# ip = '.'.join(ip) + '.'


def scanHost(ip,loop_range,timeout):
    for i in range(1,loop_range):

        host = f'{ip}{i}'
        response = ping(host, verbose= False, timeout= timeout, count= 1)
        sys.stdout.write(f'\rPinging --> {host} ')

        if 'Reply' in str(response):
            sys.stdout.flush()
            sys.stdout.write('HOST FOUND!')
            print('')
        else:
            sys.stdout.flush()
            sys.stdout.write('FAILED!!')