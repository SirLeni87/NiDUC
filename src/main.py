from src.Pig import Pig
from src.Farmer import Farmer


def main():
    pigs = []
    for i in range(0,8,1):
        for j in range(1,3,2):
            for k in range(1,4,1):
                pig = Pig(j, k)
                pigs.append(pig)
    farmer = Farmer(3,0)


if __name__ == "__main__":
    main()
