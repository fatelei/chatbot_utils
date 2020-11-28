# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   ner_utils.py
 
@Time    :   2020/7/20 11:20 下午
 
@Desc    :   实体提取工具类，

             调用实体提取接口
 
"""

from time_convert import TimeNormalizer

tc = TimeNormalizer()


def get_time(msg):
    """
    提取时间信息
    :param msg:
    :return:
    """
    result = tc.parse(msg)
    print(result)

    return result

if __name__ == '__main__':
    msg = '天气'
    get_time(msg)

