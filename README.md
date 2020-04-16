# Python functional code snippet

> 常用的 python 功能性代码片段

## 1. 日志相关

### 1.1 使用print函数实现

#### 1.1.1 使用 print("string", file="")实现

先使用 with 上下文以及 open 函数打开一个文件句柄，然后在使用 print 函数时将输出流重定向到之前的句柄文件。

[具体实现](https://github.com/Jesse3692/tools/blob/4fc85738181a32bd344b12443a9de72d10b43bff/log/print_file.py)

#### 1.1.2 通过修改标准输出流实现（sys）

先使用 with 上下文以及 open 函数打开一个文件句柄，然后通过 sys 模块将系统的标准输出重定向到之前的句柄文件，之后 print 打印的东西都会重定向到文件中，使用完成后不要忘了将系统的标准输出复原。

[具体实现](./log/sys_stdout.py)

## 2. 文件操作

### 2.1 输出大文件的前几行

先使用 with 上下文以及 open 函数打开一个文件句柄，使用文件句柄的 readlines 方法，然后将得到的可迭代对象进行迭代在

[具体实现](./file/head_file.py)

## 3. 对象占用的内存空间

使用 sys 模块的 getsizeof()方法，查看一个对象所占用的内存空间

[具体实现](./memory/object_of_memory_size.py)

## 4. 字符串的拼接

### 4.1 来自 C 语言的`%`方式

％号格式化字符串的方式继承自古老的 C 语言，这在很多编程语言都有类似的实现。`%s`是一个占位符，它仅代表一段字符串，并不是拼接的实际内容。实际的拼接内容在一个单独的%号后面，放在一个元组中。

类似的占位符还有：%d（整数）、%f（浮点数）、%x（十六进制数）...

### 4.2 format()拼接方式

这种方式是使用花括号｛｝做占位符，在 format 方法中再传入实际的拼接值。容易看出，它实际上是对%号拼接方式的改进，这种方式在 python2.6 中开始引入。

### 4.3 （）类似元组方式

### 4.4 面向对象模版拼接

### 4.5 常用的+号拼接

### 4.6 join()拼接方式

str 对象自带的 join()方法，接受一个序列参数，可以实现拼接。拼接时，元素若不是字符串，需要先转换一下。可以看出，这种方法比较适用与连接序列对象中（例如列表）的元素，并设置统一的间隔符。

当拼接长度超过 20 时，这种方式基本上是首选。不过，它的缺点就是：不适合进行零散片段的、不处于序列集合的元素拼接。

### 4.7 f-string 方式

f-string 方式出自 PEP 498（Literal String Interpolation，字面字符串插值）

[参考资料](https://kandianshare.html5.qq.com/v2/news/2669455806451996994?url=http%3A%2F%2Fkuaibao.qq.com%2Fs%2F20200328A0P72100&cardmode=1&dataSrc=96&docId=2669455806451996994&pid=45&queryId=1585447886181&sh_sid=5__21570c683d3cb00e__b17b121e58985d2f0b41567f1d3188cb&subjectId=1090319&zimeitiId=qeh_5408094&target_app=kb#)

## 5. Python调用其他语言的库

### 5.1 python调用C库

Python中的`ctypes`模块提供了和C语言兼容的数据类型和函数来加载DLL文件，因此在调用时不需对源文件做任何的修改。

#### 将C文件编译为动态链接库文件

在linux和MAC下面为`.so`文件，windows为`.dll`文件

```shell
# Linux
$ gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c
# Mac
$ gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c
# Windows
$ gcc -shared -Wl,-soname,adder -o adder.dll -fPIC add.c
```

在这个例子中，C文件时自解释的，它包含两个函数，分别实现了整型求和和浮点型求和。

```c
// sample C file to add 2 numbers - int and float
#include <stdio.h>

int add_int(int, int);
float add_float(float, float);

int add_int(int num1, int num2)
{
    return num1 + num2;
}

float add_float(float num1, float num2)
{
    return num1 + num2;
}
```

在python文件中，一开始先导入ctypes模块，然后使用CDLL函数来加载我们创建的库文件。这样我们就可以通过变量adder来使用C类库中的函数了。当adder.add_int()被调用时，内部将发起一个对C函数add_int的调用。ctypes接口允许我们在调用C函数时使用原生Python中默认的字符串型和整型。

```python
from ctypes import *

#load the shared object file
adder = CDLL('./c/adder.so')

# Find sum of integers
res_int = adder.add_int(4, 5)
print('Sum of 4 and 5 = ' + str(res_int))

# Find sum of floats
a = c_float(5.5)
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
print('Sum of 5.5 and 4.1 = ' + str(add_float(a, b)))
```

而对于其他类似布尔型和浮点型这样的类型，必须要使用正确的ctypes类型才可以。如向adder.add_float()函数传参时，我们要先将python中的十进制值转化为c_float类型，然后才能传送给C函数。这种方法虽然简单，清晰，但是却很受限。例如，并不能在C中对对象进行操作。

## 6. 安全加密方式

### 1. 加密

加密是对消息或信息进行编码的过程，以使只有授权人员才能使用相应的键读取消息或信息，而未经授权的人员则不能。预期的消息或信息，称为纯文本，使用加密算法-密码-加密，生成密文，只有解密后才能读取。加密是一种双向功能。当我们加密某些东西时，我们这样做是为了以后对其进行解密。加密用于传输时保护数据，例如在SSH通信时。

### 2. 散列

哈希是使用算法将任意大小的数据映射到固定长度的过程，这称为哈希值。加密是一种双向功能，而散列是一种单向功能。尽管在技术上可以反向散列值，但是有些哈希函数所需要的计算力远超硬件设备。加密是为了保护传输中的数据，而散列是为了验证数据没有被更改并且是真实的。

密码不是以纯文本格式存储在数据库中，而是以散列值存储。

### 3. 盐

盐是固定长度的加密强度强的随机值，将其添加到哈希函数的输入中以为每个输入创建唯一的哈希。添加盐值可以使密码哈希输出唯一，即使对于采用通用密码的用户也是如此。

### 4. bcrypt函数

bcrypt是基于Blowfish密码涉及的密码哈希功能。bcrypt函数是OpenBSD的默认密码哈希算法。有针对C，C++，C#，Java，JavaScript，PHP，Python和其他语言的bcrypt实现。

bcrypt算法使用强大的加密技术为我们创建哈希并加盐。该算法的计算成本是参数化的，因此随着计算机变得越来越快，它可能会增加。计算成本被成为工作因子或成本因子。它减慢了散列的速度，使暴力破解的尝试越来越难。随着计算机变得越来越快，最佳成本因数会随着时间而变化。高成本因素的缺点是增加了系统资源的负载并影响了用户体验。

### 5. Python bcrypt创建哈希密码

使用bcrypt创建一个salt和hash密码

```python
import bcrypt

passwd = b's@cret123'

salt = bcrypt.gensalt()  # 生成盐
hashed = bcrypt.hashpw(passwd, salt)  # 生成hash值
```

请注意，盐是生成的哈希值的第一部分。还要注意，每次生成的唯一的salt和hash值。

使用bcrypt检查密码

```python
import bcrypt

passwd = b's@cret123'

salt = bcrypt.gensalt()  # 生成盐
hashed = bcrypt.hashpw(passwd, salt)

if bcrypt.checkpw(passwd, hashed): # 检查密码
    print('match')
else:
    print('not match')
```

bcrypt成本因子

成本因子通过减慢散列来提高安全性。

```python
import time
import bcrypt

start = time.time()

password = b'@scret123'
salt = bcrypt.gensalt(rounds=17)  # 设置成本因子
hashed = bcrypt.hashpw(password, salt)
end = time.time()

print(end - start)
print(hashed)
```

## 7. 继承

### 7.1 super的使用

通常super()有两个使用的地方：

- 1. 可以访问父类中的构造方法。
- 2. 子类方法想调用父类（MRO）中的方法。

super是调用父类中的方法，如果加上参数类，则调用下一个类中的方法

[具体代码](https://github.com/Jesse3692/tools/blob/master/super/exec_father_func.py)

这两个写法是一样的

```python
super(Bar, self).eat()
super().eat()
```

查看MRO继承顺序（`print(Bar.__mro__)`）