import csv
from matplotlib import pyplot as plt

# 在我的 notebook 里，要设置下面两行才能显示中文
plt.rcParams['font.family'] = ['sans-serif']
# 如果是在 PyCharm 里，只要下面一行，上面的一行可以删除
plt.rcParams['font.sans-serif'] = ['SimHei']

def save_data_to_csv(path, file_name, content):
    with open(path + file_name, mode='a', newline='') as csvfile:
        csv_write = csv.writer(csvfile, dialect="excel")
        # csv_write.writerow(["name", "age"])
        for data in content:
            try:
                csv_write.writerow(data)
            except UnicodeEncodeError as e:
                print(e)


def user_reviews(file):
    """
    # 统计每一个用户的发表评论 {'5771320003': ['帅的', '一直在']}
    :param file:
    :return:
    """
    result = dict()  # 每个用户的发帖数量
    with open(file, 'r', encoding='gbk') as csvfile:
        lines = csv.reader(csvfile)
        for line in lines:
            if len(line) == 10:  # 该行可能为空
                uid = line[0]
                content = line[3]
                if uid not in result:
                    result[uid] = [content]
                elif uid in result:
                    result[uid].append(content)
            else:
                pass

    return result


def length_reviews(file):
    """
    # 统计每一个用户的发表评论长度 {'length': ['uid', 'uid']} :{'2': ['1516116588', '1516116588']}
    # x：length 代表文本长度；len(['uid', 'uid'])代表文本长度为x评论数量；
    :param file:
    :return:
    """
    result = dict()  # 每个用户的发帖数量
    with open(file, 'r', encoding='gbk') as csvfile:
        lines = csv.reader(csvfile)
        for line in lines:
            if len(line) == 10:  # 该行可能为空
                uid = line[0]
                content = line[3]
                length = str(len(content))
                if length not in result:
                    result[length] = [uid]
                elif length in result:
                    result[length].append(uid)
            else:
                pass

    return result


def sort_dict(dict_, by_key=True):
    result = sorted(dict_.items(), key=lambda x: int(x[0]))
    return result


def main():
    input_path = 'F:/scrapy/sina_data1.0.0/fuChouZhe/parsedData/all_data.csv'
    result = length_reviews(input_path)

    reviews_length = []
    reviews_num = []
    result = sort_dict(result)
    result_num_length = {} # { 用户数量: [评论长度] } : { 130: [1， 12] }, 评论长度为1的用户共有130个，评论长度为12的用户共有13个
    for item in result:
        print("评论长度%s-评论数量%d" %(item[0], len(item[1]) ))
        reviews_length.append(item[0])
        reviews_num.append(len(item[1]))
        length = item[0] # 评论长度
        user_nums = str(len(item[1])) # 用户数量
        if user_nums not in result_num_length:
            result_num_length[user_nums] = [length]
        elif user_nums in result_num_length:
            result_num_length[user_nums].append(length)


    result_num_length = sort_dict(result_num_length)
    count = 0
    print("=======")
    print(result_num_length)
    for i in result_num_length[::-1]:
        count += 1
        if count == 10:
            break
    return reviews_length, reviews_num





if __name__ == "__main__":
    x, y =  main()
    plt.plot(x, y, linewidth=3)
    plt.axvline(1, color="red")
    plt.axvline(33, color="red")
    plt.title("复仇者联盟事件", size=26)
    plt.autumn()
    plt.xticks(x[:])
    plt.ylabel("评论数量")
    plt.xlabel("评论长度")
    plt.show()
