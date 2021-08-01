from pythonping import ping
import sys

def discovery(Network:str, loop:int, timeout:int):
    network_list = Network.split('.')[0:-1]

    counter_block_1 = 0
    counter_block_2 = 0
    counter_block_3 = 0
    counter_block_4 = 0


    for i in range(loop):
        
        IP = '.'.join(network_list) + f'.{counter_block_1}'
        response = ping(IP, verbose= False, timeout= timeout, count= 1)
        sys.stdout.write(f'\rPinging --> {IP} ')

        if 'Reply' in str(response):
            sys.stdout.flush()
            sys.stdout.write('HOST FOUND!')
            print('')
        else:
            sys.stdout.flush()
            sys.stdout.write('FAILED!!')

        if counter_block_1 >= 255:
            network_list[2] = str(int(network_list[2])+1)
            counter_block_1 =  0
            counter_block_2 += 1

        if counter_block_2 >= 255:
            network_list[1] = str(int(network_list[1])+1)
            network_list[2] = '0'
            counter_block_2 =  0
            counter_block_3 += 1

        if counter_block_3 >= 255:
            network_list[0] = str(int(network_list[0])+1)
            network_list[1] = '0'
            counter_block_3 = 0
            counter_block_4 += 1

        counter_block_1 += 1