# 打开文件并读取内容
with open('train.txt', 'r') as file:
    content = file.readlines()

# 去除空行
content = [line.strip() for line in content if line.strip()]

# 输出文件行数
print("文件行数：", len(content))

# 将处理后的内容写回文件
with open('train.txt', 'w') as file:
    file.write('\n'.join(content))

