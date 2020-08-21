# -*- coding: utf-8 -*-
"""
Version:    V1.2
Time:       2020.08.21
Author:     Gaozhl
"""
import base64

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

# 测试base64解密
# print(str(decode_base64('NlZ4ekc4dz1GRkNTLWphdmEzNlZ4ekc4dz04')))

def decode_md5(passwd_md5):
    """
    md5单向的，因此只能判断是否正确
    :param passwd_md5:  输入md5加密的密码
    :return:            1为正确，0为错误
    """
    # 获取存在数据库中或者这里写好的密码
    passwd = "xxx"
    if (passwd == passwd_md5):
        print("密码正确")
    else:
        print("密码错误")

# 测试md5
# decode_md5("xxx")

def decode_sha1(passwd_sha1):
    """
    sha1单向的，因此只能判断是否正确
    :param passwd_sha1: 输入sha1加密的密码
    :return:            1为正确，0为错误
    """
    # 获取存在数据库中或者这里写好的密码
    passwd = "xxx"
    if (passwd == passwd_sha1):
        print("密码正确")
        return 1
    else:
        print("密码错误")
        return 0

# 测试md5
# decode_sha1("xxx")

def decode_sha256(passwd_sha256):
    """
    sha256单向的，因此只能判断是否正确
    :param passwd_sha256:   输入sha256加密的密码
    :return:                1为正确，0为错误
    """
    # 获取存在数据库中或者这里写好的密码
    passwd = "xxx"
    if (passwd == passwd_sha256):
        print("密码正确")
        return 1
    else:
        print("密码错误")
        return 0

# 测试md5
# decode_sha256("xxx")