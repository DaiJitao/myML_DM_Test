import sys

if __name__ == "__main__":
    if len(sys.argv) > 0:
        for i in sys.argv:
            print(i)
    else:
        tmp = sys.exit(1)
        print(tmp)