from pythonping import ping
import sys
import argparse
import ip

"""
argumetns:
--netID -n 
--timeout -t
--mask -m

--threads -

"""




def CLI():
    parser = argparse.ArgumentParser(f'Host discover with python type {str(sys.argv[0])}')
    parser.add_argument('-n','--netID', help='Network ID such as 192.168.1.0')



    return parser.parse_args()
def main():
    args = CLI()
    print(args)
    print(ip.get_info())

if __name__ == "__main__":
    main()


