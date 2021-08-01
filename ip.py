import psutil
import sys


class Interfaces():

    def get_data(self):
        data = psutil.net_if_addrs()
        return data
    
    def get_interfaces(self):
        data = self.get_data()
        return [interface for interface in data]

    def get_interfaces_info(self):
        data = self.get_data()
        interfaces = self.get_interfaces()
        info = {}

        for interface in interfaces:

            iface_info = data[interface][1][1:3] # Arreglar per linux
            info[interface] = iface_info
        return info


def check_correct_subnet(subnet:list):
    past = None
    for current in subnet:
        current = int(current)
        if past == None:
            past = current
            continue

        if past < current:
            print('Subnet error: Incorrect format')
            sys.exit(1)
            # Create error

        past = current

def subnet_2_decimal(subnet:str):
    subnet = subnet.split('.')
    check_correct_subnet(subnet)
    decimal_subnet = []
    for block in subnet:
        binary= bin(int(block))
        length = binary.count('1')
        decimal_subnet.append(length)
    
    return sum(decimal_subnet)

def get_loops(decimal_subnet):
    host_bits = 32 -decimal_subnet
    loops = 2 ** host_bits
    
    return loops


def get_network_ID(addr:str , mask:str):

    addr = [int(x) for x in addr.split(".")]
    mask = [int(x) for x in mask.split(".")]

        
    netw = [addr[i] & mask[i] for i in range(4)]
    bcas = [(addr[i] & mask[i]) | (255^mask[i]) for i in range(4)]

    Network = '.'.join(map(str, netw))
    Broadcast = '.'.join(map(str, bcas))

    return Network, Broadcast




if __name__ == '__main__':
    x = get_loops(subnet_2_decimal('255.128.0.0'))
    print(x)
