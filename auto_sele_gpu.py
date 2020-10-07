import os
import sys
import time
 
cmd = 'python ~/mytrain.py'  # 运行代码命令
 
# 获取GPU状态信息
def gpu_info():
    gpu_status = os.popen('nvidia-smi -i 3 | grep %').read().split('|')  # 指定gpu
    gpu_memory = int(gpu_status[2].split('/')[0].split('M')[0].strip())
    gpu_power = int(gpu_status[1].split('   ')[-1].split('/')[0].split('W')[0].strip())
    return gpu_power, gpu_memory
 

def auto_train(interval=2):
    gpu_power, gpu_memory = gpu_info()
    i = 0
    while gpu_memory > 1000 or gpu_power > 20:  # 根据GPU的显存和功率设置等待条件
        gpu_power, gpu_memory = gpu_info()
        i = i % 5
        symbol = 'monitoring: ' + '>' * i + ' ' * (10 - i - 1) + '|'
        gpu_power_str = 'gpu power:%d W |' % gpu_power
        gpu_memory_str = 'gpu memory:%d MiB |' % gpu_memory
        sys.stdout.write('\r' + gpu_memory_str + ' ' + gpu_power_str + ' ' + symbol)
        sys.stdout.flush()  # 打印当前gpu状态
        time.sleep(interval)
        i += 1
    print('\n' + cmd)
    os.system(cmd)
 
 
if __name__ == '__main__':
    auto_train()
