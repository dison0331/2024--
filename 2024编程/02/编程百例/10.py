# 10.暂停一秒输出并格式化当前10秒时间

import time as t

for s in range(0, 10):  # 循环变更
    print(t.strftime('%Y-%m-%d,%H-%M-%S', t.localtime()))  # 转换
    #    print(t.ctime())
    t.sleep(1)  # 等待
