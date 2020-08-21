# -*- coding: utf-8 -*-
"""
Version:    V1.2
Time:       2020.08.21
Author:     Gaozhl
"""
import os
import base64
from random import Random
from hashlib import md5
from hashlib import sha1
from hashlib import sha256

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
    return salt+'='

# 测试
# print(create_salt(12))

def encrypt_base64(passwd):
    """
    使用base64加密字符串，有解密方式
    加密串放回格式为：salt+passwd+salt+salt长度，这种方式在加密串中隐藏了重复部分(密码加salt不为偶数)
    :param passwd:  原始密码
    :return:        passwd_base64返回的加密串
    """
    # 原始版本-直接加密
    # passwd_base64 = str(bytes.decode(base64.b64encode((passwd).encode('utf-8'))))
    # return passwd_base64

    # # V1.1
    # # 新增salt，通过添加salt的内容以及长度来加密字符串
    # salt = create_salt(12)
    # passwd_base64 = str(bytes.decode(base64.b64encode((salt + passwd + "=" +str(len(salt))).encode('utf-8'))))
    # return passwd_base64

    # V1.2
    # 由于可能密码中存在多个=导致后续的取数会发生错误，因此改进
    # 密码为salt+passwd+salt+salt长度，这种方式在加密串中隐藏了重复部分
    salt = create_salt(Random().randint(0, 12))
    passwd_base64 = str(bytes.decode(base64.b64encode((salt + passwd + salt + str(len(salt))).encode('utf-8'))))
    return passwd_base64

# 测试base64加密
print(encrypt_base64('FFCS-java3'))

def encrpty_md5(passwd):
    """
    md5加密方式：这是单向的，无法解密，也能加salt，此处无。
    :param passwd:  原始密码
    :return:        md5加密后的密码串
    """
    passwd_md5 = md5(passwd.encode(encoding='UTF-8')).hexdigest()
    return passwd_md5

# 测试md5加密
# print(encrpty_md5('FFCS-java3'))

def encrpty_sha1(passwd):
    """
    sha1加密方式：这是单向的，无法解密，也能加salt，此处无。
    可以参考sha256的写法（简单）
    :param passwd:  原始密码
    :return:        加密密码
    """
    passwd_sha1 = sha1()
    passwd_sha1.update(passwd.encode())
    passwd_sha1 = passwd_sha1.hexdigest()
    return passwd_sha1

# 测试sha1加密
# print(encrpty_sha1("FFCS-java3"))

def encrpty_sha256(passwd):
    """
    sha256加密方式：这是单向的，无法解密，也能加salt，此处无。
    可以参考sha1的写法（复杂）
    :param passwd:  原始密码
    :return:        加密密码
    """
    passwd_sha256 = sha256(passwd.encode("utf-8")).hexdigest()
    return passwd_sha256

# 测试sha1加密
# print(encrpty_sha256("FFCS-java3"))