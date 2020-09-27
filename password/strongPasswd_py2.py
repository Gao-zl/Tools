#/user/bin/python
# -*- coding: utf-8 -*-
"""
Version:    V1.0
Time:       2020.08.21
Author:     Gaozhl
使用的是Python2来运行
"""
import os
import random

# 去掉#防止出现密码被注释的情况
char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
             'nums': '0123456789',
             'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'special': '^!\$%&/()=?{[]}+~-.:,;<>|'
            }


def generate_pass(length=21):
    """
    Function to generate a password
    强密码生成器
    修改：以大写字母开头，防止某些时刻的特殊要求
    :param length:  生成密码长度
    :return:        生成的密码结果
    """
    password = []
    # 先从24字母中获取一个值
    i = random.randint(0, 25)
    password.append(char_set['big'][i])

    while len(password) < length:
        key = random.choice(char_set.keys())
        a_char = os.urandom(1)
        if a_char in char_set[key]:
            if check_prev_char(password, char_set[key]):
                continue
            else:
                password.append(a_char)
    return ''.join(password)


def check_prev_char(password, current_char_set):
    """
    Function to ensure that there are no consecutive
    UPPERCASE/lowercase/numbers/special-characters.
    确保两个字符不是属于相同的类型
    :param password:            输入的密码
    :param current_char_set:    当前的密码字符的种类
    :return:                    放回True或False
    """
    index = len(password)
    if index == 0:
        return False
    else:
        prev_char = password[index - 1]
        if prev_char in current_char_set:
            return True
        else:
            return False

# 测试
# print((generate_pass(24)))