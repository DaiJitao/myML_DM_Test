import pickle


def save_data_pkl(file_path, data):
    with open(file_path, "wb") as file:
        if pickle.dump(data, file=file) == None:
            print("data save success")


def load_data_pkl(file_path):
    with open(file_path, 'rb+') as file:
        return pickle.load(file)


def save_data_txt(path, data):
    with open(path, 'wb') as file:
        file.write(data)


if __name__ == "__main__":
    d = 12

