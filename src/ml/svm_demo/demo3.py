place_code_path = './place.code'
code2city = dict()
city2code = dict()

with open(place_code_path, 'r', encoding='utf-8') as f:
    print(f.readlines())
    lines = [(line.strip()) for line in f.readlines()]
    for line in lines:
        # print(line)
        lst = line.split(' ')
        code = int(lst[0])
        city = lst[-1]
        code2city[code] = city

        if city not in city2code.keys():
            code_lst = [int(code)]
            city2code[city] = code_lst
        else:
            city2code[city].append(code)

print(city2code)
print(code2city)