# -*- encoding: utf-8 -*-
'''
@File    : create_hashed_password.py
@Time    : 2020/04/13 16:01:51
@Author  : Jesse Chang
@Contact : jessechang2358@gmail.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : None
'''


import bcrypt

passwd = b's@cret123'

salt = bcrypt.gensalt()  # 生成盐
hashed = bcrypt.hashpw(passwd, salt)

print(salt)
print(hashed)

"""
b'$2b$12$NnCeuRku0j8IjRBOIYLxre'
b'$2b$12$NnCeuRku0j8IjRBOIYLxreIsExSSkFtVjrboYbdqDFp6Ii02fjUjG'
"""
