# -*- coding: utf-8 -*-
"""
Version:    V1.1
Time:       2020.08.21
Author:     Gaozhl
"""
import os
import base64
from random import Random
from hashlib import md5

def decode_base64(passwd_base64):
    """
    解密base64秘钥
    :param passwd_base64:   加密后的字符
    :return:                解密后的字符
    """
    # 原始版本
    # passwd = str(bytes.decode(base64.b64decode((passwd_base64).encode('utf-8'))))
    # return passwd

    # # V1.1
    # # 改进为通过获取秘钥长度
    # passwd_tmp = str(bytes.decode(base64.b64decode((passwd_base64).encode('utf-8'))))
    # # 获取salt的长度,由于可能在密码中存在=因此取最后一位
    # # 转为int类型
    # salt_len = passwd_tmp.split('=')[-1]
    # salt_len = int(salt_len)
    # # 获取秘钥，通过截取=之前的字符
    # # 生成的是list，取list[0]，再去掉salt的长度，得到最终结果
    # passwd = passwd_tmp.split('=')[:-1][0][salt_len:]
    # return passwd

    # V1.2
    # 改进为通过获取秘钥长度来分割,获取得到的格式salt+passwd+salt+salt长度
    passwd_tmp = str(bytes.decode(base64.b64decode((passwd_base64).encode('utf-8'))))
    salt_len = int(passwd_tmp.split('=')[-1])
    salt = passwd_tmp[:salt_len]
    passwd = passwd_tmp.split(salt)[1]
    return passwd

print(str(decode_base64('WWlQQ3RwPWZhc2Q9c2RnYXNkZ3M9WWlQQ3RwPTc=')))