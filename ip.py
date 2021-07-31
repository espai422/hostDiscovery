import psutil

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

            iface_info = data[interface][1][1:3]
            info[interface] = iface_info
        return info

    
if __name__ == '__main__':
    x = Interfaces()
    x.get_interfaces()
    print(x.get_interfaces_info())
