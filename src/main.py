from src.Pig import Pig


def main():
    pigs = []
    for i in range(0,8,1):
        for j in range(1,3,2):
            for k in range(1,4,1):
                pig = Pig(j, k)
                pigs.append(pig)


if __name__ == "__main__":
    main()
