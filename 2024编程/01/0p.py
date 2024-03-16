import socket
import struct

def get_ip_list(subnet):
    # 提取子网信息
    network_address = subnet.split('/')[0]
    netmask = socket.inet_ntoa(struct.pack('>I', 0xFFFFFFFF << (32 - int(subnet.split('/')[1])))[2:])

    # 创建一个空列表来存储IP地址
    ip_list = []

    # 遍历IP地址范围并添加到列表中
    for i in range(1, 256):
        ip = socket.inet_ntoa(struct.pack('>I', int(network_address) | i << (32 - int(subnet.split('/')[1])))[2:])
        ip_list.append(ip)

    return ip_list


subnet = "192.168.1.0/24"  # 修改为你的子网
ip_list = get_ip_list(subnet)
print(ip_list)