import psutil

# 获取CPU核心数
cpu_count = psutil.cpu_count()
print(f"CPU核心数: {cpu_count}")

# 获取CPU使用率
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU使用率: {cpu_percent}%")

# 获取内存信息
memory = psutil.virtual_memory()
print(f"总内存: {memory.total} MB")
print(f"可用内存: {memory.available} MB")
print(f"内存使用率: {memory.percent}%")

# 获取磁盘信息
disk = psutil.disk_usage('/')
print(f"总磁盘空间: {disk.total} GB")
print(f"可用磁盘空间: {disk.free} GB")
print(f"磁盘使用率: {disk.percent}%")

# 获取网络信息
net_io = psutil.net_io_counters()
print(f"总接收量: {net_io.bytes_recv} bytes")
print(f"总发送量: {net_io.bytes_sent} bytes")