import pickle


def save_data(file_path, data):
    with open(file_path, "wb") as file:
        if pickle.dump(data, file=file) == None:
            print("data save success")


def load_data(file_path):
    with open(file_path, 'rb+') as file:
        return pickle.load(file)


def save_detail_index(url):
    pass


if __name__ == "__main__":
    d = 12
    save_data("./test.pkl", d)
    load_data("./test.pkl")
