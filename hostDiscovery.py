from time import time
from pythonping import ping
import sys
import argparse
import ip
import discover


def CLI():
    # Definition of arguments
    parser = argparse.ArgumentParser(f'Host discover with python type {str(sys.argv[0])}')
    # Add first argument to parse wich will define if the positional argument is Interface or network
    parser.add_argument(
        '-m','--mode_interface',
        default=True,
        help= 'By default is true, so you need to specifi Interface argument. If is set to false, you neet specifi Network argument',
        type=bool
        )
    

    parser.add_argument(
        '-i','--interface',
        help='The network interface you want to discover',
        )

    parser.add_argument(
        '-n','--network',
        nargs= 2,
        help='Two arguments: Network_ID Netmask --> 10.10.10.1 255.255.0.0'
        )

    parser.add_argument(
        '-d','--timeout',
        help= 'Set the the limit duration of the ping (timeout)',
        default= 0.1,
        type= float
        )

    parser.add_argument(
        '-t','--threads',
        help= 'Number of threads to run',
        default= 1,
        type= int
    )

    parser.add_argument(
        '-v','--verbose',
        help= 'By default is True, shows host founds. If is set to false you should export the results (-o)',
        default= True,
        type= bool
    )


    parser.add_argument(
        '-o','--export',
        help= f'Two value argument <exportaton_mode> <exportation/Path>. Exportation modes:\nDiccionari\nBoolean',
        nargs= 2
    )

    return parser.parse_args()


def main():
    args = CLI()
    print(args)
    if args.mode_interface:
  
        Network_info = ip.Interfaces()
        interfaces_info = Network_info.get_interfaces_info()
        interface_ip_mask = interfaces_info[args.interface]
        
        Network, Broadcast = ip.get_network_ID(interface_ip_mask[0],interface_ip_mask[1])
        Decimal_mask = ip.subnet_2_decimal(interface_ip_mask[1])
        loop = ip.get_loops(Decimal_mask)

        discover.discovery(Network=Network, timeout=args.timeout, loop= loop)


        #Inicia modo interface
    elif args.mode_interface == False:
        pass
        #Iniica modo Manual
    else:
        pass
        # Lanza error

if __name__ == "__main__":
    main()


