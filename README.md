# Python functional code snippet

常用的python功能性代码片段



## 1. 日志相关



### print函数



#### 1. 使用print("string", file="")实现

先使用with上下文以及open函数打开一个文件句柄，然后在使用print函数时将输出流重定向到之前的句柄文件。

[具体实现](./log/print_file.py)



#### 2. 通过修改标准输出流实现（sys）

先使用with上下文以及open函数打开一个文件句柄，然后通过sys模块将系统的标准输出重定向到之前的句柄文件，之后print打印的东西都会重定向到文件中，使用完成后不要忘了将系统的标准输出复原。

[具体实现](./log/sys_stdout.py)



## 2. 文件操作



#### 1. 输出大文件的前几行

先使用with上下文以及open函数打开一个文件句柄，使用文件句柄的readlines方法，然后将得到的可迭代对象进行迭代在

[具体实现](./file/head_file.py)



## 3. 对象占用的内存空间

使用sys模块的getsizeof()方法

[具体实现](./memory/object_of_memory_size.py)