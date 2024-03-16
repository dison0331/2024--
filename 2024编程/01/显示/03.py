import tkinter as tk
from tkinter import ttk
import psutil

# 创建主窗口
root = tk.Tk()
root.title("设备信息查看器")

# 设置窗口初始大小
root.geometry("600x400")

# 创建框架来分组按钮和文本框
button_frame = tk.Frame(root)
info_frame = tk.Frame(root)

# 将框架放置到主窗口中
button_frame.pack(fill='x', padx=10, pady=10)
info_frame.pack(fill='both', expand=True, padx=10, pady=10)


# 创建按钮
def show_cpu_info():
    cpu_info = "CPU使用率: {}%".format(psutil.cpu_percent())
    update_info_text(cpu_info)


def show_memory_info():
    memory = psutil.virtual_memory()
    memory_info = "总内存: {:.2f} GB\n可用内存: {:.2f} GB\n内存使用率: {}%".format(
        memory.total / (1024 ** 3), memory.available / (1024 ** 3), memory.percent)
    update_info_text(memory_info)


def show_disk_info():
    disk = psutil.disk_usage('/')
    disk_info = "总磁盘空间: {:.2f} GB\n可用磁盘空间: {:.2f} GB\n磁盘使用率: {}%".format(
        disk.total / (1024 ** 3), disk.free / (1024 ** 3), disk.percent)
    update_info_text(disk_info)


def show_net_info():
    net_io = psutil.net_io_counters()
    net_info = "总接收量: {:.2f} MB\n总发送量: {:.2f} MB".format(
        net_io.bytes_recv / (1024 ** 2), net_io.bytes_sent / (1024 ** 2))
    update_info_text(net_info)


def update_info_text(new_info):
    info_text.config(state='normal')
    info_text.delete(1.0, tk.END)
    info_text.insert(tk.END, new_info)
    info_text.config(state='disabled')


# 创建按钮并放置在按钮框架上
cpu_button = ttk.Button(button_frame, text="CPU信息", command=show_cpu_info)
cpu_button.pack(side='left', padx=5, pady=5)

memory_button = ttk.Button(button_frame, text="内存信息", command=show_memory_info)
memory_button.pack(side='left', padx=5, pady=5)

disk_button = ttk.Button(button_frame, text="磁盘信息", command=show_disk_info)
disk_button.pack(side='left', padx=5, pady=5)

net_button = ttk.Button(button_frame, text="网络信息", command=show_net_info)
net_button.pack(side='left', padx=5, pady=5)

exit_button = ttk.Button(button_frame, text="退出", command=root.quit)
exit_button.pack(side='left', padx=5, pady=5)

# 创建文本框来显示信息
info_text = tk.Text(info_frame, width=50, height=10)
info_text.pack(fill='both', expand=True)
info_text.config(state='disabled')  # 设置文本框为只读

# 运行主循环
root.mainloop()
