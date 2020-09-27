# -*- coding: utf-8 -*-
"""
Version:    V1.0
Time:       2020.09.27
Author:     Gaozhl
Attention:  需要先配置好tesseract才能处理
"""

import os
from PIL import Image
import pytesseract


def verify_code(filename):
    """
    验证码处理
    :param filename:    需要处理的文件
    :return:            返回处理的验证码结果
    """
    # global text
    f1, f2 = os.path.splitext(filename)
    try:
        im = Image.open(filename)

        # 切掉四周的黑边
        # 此处假定黑边大小为4个单位
        width = im.size[0]
        height = im.size[1]
        left = 4
        top = 4
        right = width - 4
        bottom = height - 4
        box = (int(left), int(top), int(right), int(bottom))
        im = im.crop(box)
        im = im.resize((width * 4, height * 4), Image.BILINEAR)
        im.save(f1 + '_step1' + f2)
        # 转为灰度图
        imgry = im.convert('L')
        imgry.save(f1 + '_step2' + f2)
        # 去噪
        threshold = 140
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        out = imgry.point(table, '1')
        out.save(f1 + '_step3' + f2)
        # 调用pytesseract的图像识别监测数字
        # 相当于调用如下的这行命令
        # tesseract temp_step3.png result -l eng
        # 只识别数字可以改为如下的命令/代码
        # tesseract temp_step3.png result -psm 7
        # text = pytesseract.image_to_string(out, config='-psm 7')
        text = pytesseract.image_to_string(out, config='-l eng')
        print('text: ', text)

    except Exception as e:
        print(e)

    return text


if __name__ == '__main__':
    # 默认安装的路径
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    num_code = verify_code("temp.png")
