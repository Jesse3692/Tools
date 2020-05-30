import os        
os.chdir("./log")   
k=50     
with open("hello.txt") as f: # f -> <class '_io.TextIOWrapper'>  用来处理文本输入输出操作的类。
    n=0
    for line in f.readlines(): # f.readlines() -> list
        print(type(line))  # line -> str
        n+=1
        print(line.replace("\n",""))
        if n==k:
            break