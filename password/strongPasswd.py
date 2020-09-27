# -*- coding:utf-8 -*-
'''
Version:    V1.0
Time:       2020.08.21
Author:     Gaozhl
'''
import string
import random

char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
             'nums': '0123456789',
             'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'special': '^!\$%&/()=?{[]}+~-.:,;<>|'
            }

def GenPassword(length=21, chars=string.ascii_letters + string.digits):
    """
    Function to generate a password
    强密码生成器
    :param length:  选定长度
    :param chars:   默认值即可
    :return:        生成的复杂密码
    """
    passwd = []
    # 首字母先确定为大写字母，预防特殊要求
    i = random.randint(0, 25)
    passwd.append(char_set['big'][i])
    while len(passwd) < length:
        # 得到一个随机的key
        key = random.choice(list(char_set.keys()))
        # 获取这个key中的长度，选取其中的一个字母
        choice = random.randint(0, len(char_set[key]) - 1)
        # 前后字符是否相同进行判断，防止简单密码
        if check_prev_char(passwd, char_set[key][choice]):
            continue
        else:
            passwd.append(char_set[key][choice])
    return ''.join(passwd)

def check_prev_char(passwd, current_char_set):
    """
    检查前后两个字符是否相同，保证密码不出现简单密码
    :param passwd:              输入的密码
    :param current_char_set:    当前选取的字符种类
    :return:                    返回True或者False
    """
    index = len(passwd)
    if index == 0:
        return False
    else:
        prev_char = passwd[index - 1]
        if prev_char in current_char_set:
            return True
        else:
            return False

print(GenPassword())