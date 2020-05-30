# -*- encoding: utf-8 -*-
'''
@File    : exec_father_func.py
@Time    : 2020/04/16 16:29:34
@Author  : Jesse Chang
@Contact : jessechang2358@gmail.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : None
'''


class Base1:
    def eat(self):
        print("我是可怜的Base1")


class Base2:
    def eat(self):
        print("我是可怜的Base2")


class Base3:
    def eat(self):
        print("我是可怜的Base3")


class Bar(Base1, Base2, Base3):
    def eat(self):
        print("我是Bar里面的吃1")
        super(Bar, self).eat()
        super().eat()
        super().eat()
        print("我是Bar里面的吃2")


b = Bar()
b.eat()

print(Bar.__mro__)
