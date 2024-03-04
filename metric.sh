#!/bin/bash

# 执行nvidia-smi命令并获取输出
output=$(nvidia-smi --query-gpu=index,memory.total,memory.used,utilization.gpu,utilization.memory,temperature.gpu,power.draw --format=csv,noheader,nounits)

# 将输出按行分割为数组
IFS=$'\n' read -rd '' -a lines <<<"$output"

# 遍历每一行并打印指标信息
for line in "${lines[@]}"; do
    IFS=',' read -ra metrics <<<"$line"
    gpu_index=${metrics[0]}
    memory_total=${metrics[1]}
    memory_used=${metrics[2]}
    gpu_utilization=${metrics[3]}
    memory_utilization=${metrics[4]}
    temperature=${metrics[5]}
    power=${metrics[6]}

    echo "GPU $gpu_index:"
    echo "  Memory Total: $memory_total MB"
    echo "  Memory Used: $memory_used MB"
    echo "  GPU Utilization: $gpu_utilization %"
    echo "  Memory Utilization: $memory_utilization %"
    echo "  Temperature: $temperature ℃"
    echo "  Power: $power W"
    echo
done
