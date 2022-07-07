import random


def random_str(randomlength=16):  # 这块是随机数生成
    rand_str = ''
    base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        rand_str += base_str[random.randint(0, length)]
    return rand_str
