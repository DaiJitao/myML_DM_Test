
def to_one_hot_code(value):
    if value == 1:
        return [1, 0, 0]
    if value == 3:
        return [0, 1, 0]
    if value == 4:
        return [0, 0, 1]
    else:
        print("没有该状态%s" %(str(value)))
        return None

def one_hot_to_value(code_list):
    if code_list == [1, 0, 0]:
        return 1
    if [0, 1, 0] == code_list:
        return 3
    if [0, 0, 1] == code_list:
        return 4
    else:
        print("独热码转标签错误%s" %str(code_list))
        return None

