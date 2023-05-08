import os

# 要执行的命令
command = "python generate_image_pairs.py --data-dir train/ --outputtxt train.txt --num-samepairs 600"

# 执行命令100次
for i in range(2000):
    os.system(command)

