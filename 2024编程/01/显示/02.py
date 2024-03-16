import tkinter as tk
from tkinter import ttk

import psutil

# 创建主窗口
root = tk.Tk()
root.title("设备进程信息")

# 创建标签
cpu_label = ttk.Label(root, text="CPU信息:")
cpu_label.pack(pady=10)

# 创建文本框并设置滚动条
cpu_text = tk.Text(root, width=50, height=10)
cpu_text.pack(pady=10)


# 获取CPU信息并显示在文本框中
def get_cpu_info():
    cpu_info = psutil.cpu_times()
    cpu_text.delete(1.0, tk.END)
    cpu_text.insert(tk.END, f"CPU使用率: {psutil.cpu_percent()}%\n")
    for info in cpu_info:
        cpu_text.insert(tk.END, f"{info}\n")
    root.after(1000, get_cpu_info)  # 每秒更新一次CPU信息


get_cpu_info()

# 创建内存标签和文本框
memory_label = ttk.Label(root, text="内存信息:")
memory_label.pack(pady=10)
memory_text = tk.Text(root, width=50, height=10)
memory_text.pack(pady=10)


def get_memory_info():
    memory = psutil.virtual_memory()
    memory_text.delete(1.0, tk.END)
    memory_text.insert(tk.END, f"总内存: {memory.total} GB\n")
    memory_text.insert(tk.END, f"可用内存: {memory.available} GB\n")
    memory_text.insert(tk.END, f"内存使用率: {memory.percent}%\n")
    root.after(1000, get_memory_info)  # 每秒更新一次内存信息


get_memory_info()

# 创建磁盘标签和文本框
disk_label = ttk.Label(root, text="磁盘信息:")
disk_label.pack(pady=10)
disk_text = tk.Text(root, width=50, height=10)
disk_text.pack(pady=10)


def get_disk_info():
    disk = psutil.disk_usage('/')
    disk_text.delete(1.0, tk.END)
    disk_text.insert(tk.END, f"总磁盘空间: {disk.total} GB\n")
    disk_text.insert(tk.END, f"可用磁盘空间: {disk.free} GB\n")
    disk_text.insert(tk.END, f"磁盘使用率: {disk.percent}%\n")
    root.after(1000, get_disk_info)  # 每秒更新一次磁盘信息


get_disk_info()

# 创建网络标签和文本框
net_label = ttk.Label(root, text="网络信息:")
net_label.pack(pady=10)
net_text = tk.Text(root, width=50, height=10)
net_text.pack(pady=10)


def get_net_info():
    net = psutil.net_io_counters()
    net_text.delete(1.0, tk.END)
    net_text.insert(tk.END, f"总接收量: {net.bytes_recv} bytes\n")
    net_text.insert(tk.END, f"总发送量: {net.bytes_sent} bytes\n")
    root.after(1000, get_net_info)  # 每秒更新一次网络信息


get_net_info()

# 创建退出按钮
exit_button = ttk.Button(root, text="退出", command=root.quit)
exit_button.pack()

# 运行主循环
root.mainloop()