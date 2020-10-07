#!/bin/bash
echo 'download dataset'
wget https://xxxxxxxxx.tar.gz    # script 1
sleep 7200 &  # 设置睡眠时间，单位s, 执行script 1 7200s后执行 script 2
wait
echo 'unzip dataset'
tar -xzf xxxx.tar.gz             # script 2
sleep 300 &
wait
echo 'training'
python train.py                  # script 3
