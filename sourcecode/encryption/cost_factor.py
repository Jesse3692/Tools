# -*- encoding: utf-8 -*-
'''
@File    : cost_factor.py
@Time    : 2020/04/13 16:10:40
@Author  : Jesse Chang
@Contact : jessechang2358@gmail.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : None
'''

import time
import bcrypt

start = time.time()

password = b'@scret123'
salt = bcrypt.gensalt(rounds=17)
hashed = bcrypt.hashpw(password, salt)
end = time.time()

print(end - start)
print(hashed)