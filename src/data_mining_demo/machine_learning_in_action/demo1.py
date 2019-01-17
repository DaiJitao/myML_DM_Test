import numpy as np
def demo(d):
    d = [12, 134]

def demo2(x = 4, lamda = .1, error = .01):
    while True:
        x = x - lamda * 2 * x
        print(x)
        if np.abs(np.square(x) - 5) <= error:
            break
    return x



if __name__ == "__main__":
    d = []
    demo(d)
    print(d)
    print("===============>")
    print(demo2())