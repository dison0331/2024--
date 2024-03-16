import scapy.all as scapy


def subnet_scanner(subnet_cidr):
    """扫描指定子网并输出所有可用的IP地址"""
    # 拆分CIDR表示法以获取基础IP地址和子网掩码
    subnet_ip, subnet_mask = subnet_cidr.split('/')
    subnet_ip = scapy.IP(dst=subnet_ip)
    subnet_last_octet = int(subnet_ip.dst.split('.')[-1])

    # 遍历子网中的所有可能IP地址
    for i in range(1, 256):
        ip_address = f"{'.'.join(subnet_ip.dst.split('.')[:-1])}.{i}"
        arp = scapy.ARP(pdst=ip_address)

        # 发送ARP请求并检查响应
        if scapy.srp1(scapy.Ether() / arp, timeout=2, verbose=False):
            print(f"Active IP: {ip_address}")

        # 扫描本地网段


local_subnet = "192.168.1.0/24"
subnet_scanner(local_subnet)