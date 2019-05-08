import csv


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
            if len(line) == 10: # 该行可能为空
                uid = line[0]
                content = line[3]
                if uid not in result:
                    result[uid] = [content]
                elif uid in result:
                    result[uid].append(content)
            else:
                pass

    return result


def num_users(dict_):
    res_num_review = dict()  # 发帖数量
    for key, value in dict_.items():
        num = str(len(value))
        if num not in res_num_review:
            res_num_review[num] = [key]
        elif num in res_num_review:
            res_num_review[num].append(key)
    return res_num_review


def data_desc(file):
    sum_ = 0
    result = user_reviews(file)
    res_num_review = num_users(result)
    print("用户总数量", len(result))
    print("评论数-用户ID ", res_num_review)
    for key in res_num_review.keys():
        int_key = int(key)
        if int_key >= 7:
            # print(key + ": ", len(res_num_review[key]))
            sum_ += len(res_num_review[key])
        else:
            print(key + ": ", len(res_num_review[key]))
    print("大于6的总数", sum_)


def main():
    file = r'F:\scrapy\sina_data\fuChouZhe\parsedData\all_data.csv'
    data_desc(file)

if __name__ == '__main__':
    main()
