

def demo(src_str, sub_str):
    src_len = len(src_str)
    sub_len = len(sub_str)
    if src_len ==0 or sub_len == 0:
        return False
    _sum = 2 * src_str
    if sub_str in _sum:
        return True
    else:
        return False


d = demo('ABCD', 'CDA')
print(d)





