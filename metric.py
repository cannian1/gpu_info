# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import subprocess


# nvidia-smi --query-gpu=index,name,memory.total,memory.used,utilization.gpu,utilization.memory,temperature.gpu,power.draw --format=csv,noheader,nounits
def get_gpu_info():
    # 调用nvidia-smi命令并获取输出
    result = subprocess.run(['/usr/bin/nvidia-smi',
                             '--query-gpu=index,name,memory.total,memory.used,utilization.gpu,utilization.memory,temperature.gpu,power.draw',
                             '--format=csv,noheader,nounits'], stdout=subprocess.PIPE)
    # 将输出解码为字符串
    output = result.stdout.decode('utf-8')
    # 按行分割输出
    lines = output.strip().split('\n')
    # 解析每一行并创建一个字典列表
    gpu_info = []
    for line in lines:
        # 按逗号分割每行的信息
        info = line.split(', ')
        gpu_info.append({
            'index': info[0],
            'name': info[1],
            'total_memory': info[2],
            'used_memory': info[3],
            'gpu_utilization': info[4],
            'memory_utilization': info[5],
            'temperature': info[6],
            'power_draw': info[7]
        })

    return gpu_info


if __name__ == '__main__':
    final_info = get_gpu_info()
    final_info_json = json.dumps(final_info, indent=4)

    print(final_info_json)
