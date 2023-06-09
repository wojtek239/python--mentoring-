import copy


class Box:
    def __init__(self):
        self.elements_quantity = 4


def main():
    p1 = Box()
    p2 = Box()
    p2.elements_quantity = p1.elements_quantity
    p2.elements_quantity = 8
    print(p2.elements_quantity)

    p3 = copy.copy(p1)
    p3.elements_quantity = 8
    print(p1.elements_quantity)


if __name__ == "__main__":
    main()
