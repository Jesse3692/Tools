"""
首先打开一个文件句柄，然后将print打印的内容重定向到文件中而不是标准输出中

"""
with open('./sourcecode/log/hello.txt', 'wt') as f:
    for i in range(19):
        print("chr{0}\t{1}\t{2}".format(1, i*500, (i+1)*500), file=f)