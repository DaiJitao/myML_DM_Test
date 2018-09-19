def demo(src_str, sub_str):
    src_len = len(src_str)
    sub_len = len(sub_str)
    if src_len == 0 or sub_len == 0:
        return False
    _sum = 2 * src_str
    if sub_str in _sum:
        return True
    else:
        return False


d = demo('ABCD', 'CDA')
print(d)

"""page230"""


def solution(str1, str2):
    if len(str1) == 0 and len(str2) == 0:
        return -1
    else:
        if len(str1) == len(str2):
            if str1 == str2:
                return 1
            else:
                for i in str1:
                    pass
        if len(str2) > len(str1):
            pass


def delete_char(string, index):
    """ 删除指定字符"""
    if index < 0 or index > len(string) - 1:
        print("index error")
    if index == 0:
        return string[1:]
    if index == len(string) - 1:
        return string[:-1]
    else:
        return string[:index] + string[index + 1:]

print(delete_char('adcf', 2))
