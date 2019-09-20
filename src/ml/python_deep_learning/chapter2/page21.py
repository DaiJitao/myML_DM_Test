from keras.datasets import mnist


def demo():
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    from keras import models
    from keras import layers

    network = models.Sequential()  #
    network.add(layers.Dense(512, input_dtype=(28 * 28,)))
    network.add(layers.Dense(10, activation="softmax"))
    network.compile(optimizer='rmsprop',
                    loss='categorical_crossentropy',
                    metrics=['accuracy'])

    # 数据的标准化处理
    train_images = train_images.reshape((60000, 28 * 28))
    train_images = train_images.astype('float32') / 255
    test_images = test_images.reshape((10000, 28 * 28))
    test_images = test_images.astype('float32') / 255

    # 准备标签
    from keras.utils import to_categorical

    print(train_labels)
    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)
    print(train_labels)

    # 训练
    network.fit(train_images, train_labels, epochs=15, batch_size=128)

    # 测试
    test_loss, test_acc = network.evaluate(test_images, test_labels)
    print(test_acc)
    print(test_loss)


if __name__ == "__main__":
    demo()
