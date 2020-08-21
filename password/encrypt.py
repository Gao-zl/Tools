# -*- coding: utf-8 -*-
"""
Version:    V1.0
Time:       2020.08.21
Author:     Gaozhl
"""
import os
import base64
from random import Random
from hashlib import md5

def create_salt(length):
    """
    生成随机salt用于加密
    :param length:  自己定义需要多少位的加密秘钥
    :return:        返回salt值
    """
    salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    len_chars = len(chars) - 1
    random = Random()
    # 随机从chars中取出length长度的秘钥
    for i in range(length):
        salt += chars[random.randint(0, len_chars)]
    return salt

# 测试
# print(create_salt(12))

def encrypt_base64(passwd):
    """
    使用base64加密字符串
    :param passwd:  原始密码
    :return:        passwd_base64返回的加密串
    """
    # 原始版本-直接加密
    # passwd_base64 = str(bytes.decode(base64.b64encode((passwd).encode('utf-8'))))
    # return passwd_base64

    # V1.1
    # 新增salt，通过添加salt的内容以及长度来加密字符串
    salt = create_salt(12)
    passwd_base64 = str(bytes.decode(base64.b64encode((salt + passwd + "=" +str(len(salt))).encode('utf-8'))))
    return passwd_base64

print(encrypt_base64('fasd=sdgasdgs='))