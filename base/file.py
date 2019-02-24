filename = "../file/test.txt"
# 文件写入 'w'模式会覆盖源文件
with open(filename, 'w', encoding='utf-8') as myfile:
    myfile.write('你好, Python!\n')

# 文件读入
with open(filename, 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    print(content)
